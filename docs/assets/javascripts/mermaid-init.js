function renderMermaid() {
  if (typeof mermaid === "undefined") {
    return;
  }

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "strict",
    theme: "base"
  });

  mermaid.run({
    querySelector: ".mermaid"
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(renderMermaid);
} else {
  document.addEventListener("DOMContentLoaded", renderMermaid);
}
