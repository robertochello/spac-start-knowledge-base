#!/usr/bin/env python3
"""Audit public documentation and downloadable SQLite DBs for sensitive data.

The script reports only the location and type of a finding, never the matched
value, so CI logs do not leak the data being detected.
"""

from __future__ import annotations

import hashlib
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = Path(__file__).resolve()
DOWNLOADS = ROOT / "docs" / "assets" / "downloads"

TEXT_EXTENSIONS = {
    ".md", ".yml", ".yaml", ".css", ".js", ".txt", ".csv", ".json", ".py"
}
SKIP_DIRS = {".git", ".venv", "site", ".worktrees", "node_modules"}

# High-confidence patterns only. Customer/project names and licensing still
# require human review because they cannot be recognized reliably by regex.
PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "mac-address": re.compile(r"\b(?:[0-9A-F]{2}[:-]){5}[0-9A-F]{2}\b", re.I),
    "windows-user-path": re.compile(r"\b[A-Z]:\\Users\\[^\\\s]+", re.I),
    "unix-home-path": re.compile(r"/home/[^/\s]+"),
    "unc-path": re.compile(r"\\\\[^\\\s]+\\[^\\\s]+"),
    "credential-assignment": re.compile(
        r"\b(?:password|passwd|token|secret|api[_-]?key)\s*[:=]\s*[^\s<>{}]+",
        re.I,
    ),
}

ALLOWED_EMAILS = {
    "41898282+github-actions[bot]@users.noreply.github.com",
}

# Exact/bounded names only: avoid false positives on legitimate SPAC columns
# that merely contain fragments such as "user" inside another identifier.
SUSPICIOUS_SQLITE_NAMES = re.compile(
    r"^(?:customers?|clients?|clienti?|commess[ae]|projects?|orders?|ordini?|"
    r"users?|credentials?|passwords?|secrets?)$",
    re.I,
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if path.resolve() == SCRIPT_PATH:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def check_text(value: str, location: str, findings: list[str]) -> None:
    for name, pattern in PATTERNS.items():
        for match in pattern.finditer(value):
            if name == "email" and match.group(0).lower() in ALLOWED_EMAILS:
                continue
            findings.append(f"{location}: {name}")
            break


def scan_text_files(findings: list[str]) -> None:
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        check_text(text, str(path.relative_to(ROOT)), findings)


def scan_sqlite(path: Path, findings: list[str]) -> None:
    relative = path.relative_to(ROOT)
    try:
        con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    except sqlite3.Error as exc:
        findings.append(f"{relative}: sqlite-open-error ({type(exc).__name__})")
        return

    try:
        tables = [
            row[0]
            for row in con.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type='table' AND name NOT LIKE 'sqlite_%'"
            )
        ]
        for table in tables:
            if SUSPICIOUS_SQLITE_NAMES.fullmatch(table):
                findings.append(f"{relative}: suspicious-table-name ({table})")

            quoted_table = '"' + table.replace('"', '""') + '"'
            try:
                columns = [row[1] for row in con.execute(f"PRAGMA table_info({quoted_table})")]
                cursor = con.execute(f"SELECT * FROM {quoted_table}")
            except sqlite3.Error as exc:
                findings.append(
                    f"{relative}: sqlite-read-error ({table}, {type(exc).__name__})"
                )
                continue

            for column in columns:
                if SUSPICIOUS_SQLITE_NAMES.fullmatch(column):
                    findings.append(
                        f"{relative}: suspicious-column-name ({table}.{column})"
                    )

            for row_no, row in enumerate(cursor, start=1):
                for col_no, value in enumerate(row):
                    if value is None:
                        continue
                    if isinstance(value, bytes):
                        value = value.decode("utf-8", errors="ignore")
                    elif not isinstance(value, str):
                        continue
                    column = columns[col_no] if col_no < len(columns) else f"col{col_no}"
                    check_text(
                        value,
                        f"{relative}:{table}.{column}:row{row_no}",
                        findings,
                    )
    finally:
        con.close()


def scan_downloads(findings: list[str]) -> list[tuple[str, str]]:
    hashes: list[tuple[str, str]] = []
    if not DOWNLOADS.exists():
        return hashes
    for path in sorted(DOWNLOADS.rglob("*")):
        if not path.is_file() or path.name == ".gitkeep":
            continue
        hashes.append((str(path.relative_to(ROOT)), sha256(path)))
        if path.suffix.lower() == ".db":
            scan_sqlite(path, findings)
    return hashes


def main() -> int:
    findings: list[str] = []
    scan_text_files(findings)
    hashes = scan_downloads(findings)

    print("PUBLICATION AUDIT")
    print("=================")
    print(f"Download files checked: {len(hashes)}")
    for path, digest in hashes:
        print(f"SHA256 {path}: {digest}")

    if findings:
        print("\nPotentially sensitive findings (values intentionally hidden):")
        for item in sorted(set(findings)):
            print(f"- {item}")
        print("\nAudit FAILED. Review or sanitize the reported locations.")
        return 1

    print("\nAudit OK: no high-confidence sensitive patterns detected.")
    print("Human review is still required for customer/project names and licensing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
