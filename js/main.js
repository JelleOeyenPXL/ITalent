/**
 * Berekent 'calm' (0–1) op basis van scrollpositie.
 * Bovenaan = chaos; naarmate je naar beneden scrollt = rustiger UI.
 */
(function () {
  const root = document.documentElement;
  const prefersReduced =
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function setCalmFromScroll() {
    if (prefersReduced) {
      root.style.setProperty("--calm", "1");
      return;
    }

    const scrollable = Math.max(
      1,
      document.documentElement.scrollHeight - window.innerHeight
    );
    const y = window.scrollY;
    const raw = y / scrollable;
    // Iets sneller naar 'rust' voor leesbaarheid (calm ~ vol bij 55–60% van de pagina)
    const calm = Math.min(1, raw * 1.75);
    root.style.setProperty("--calm", calm.toFixed(4));
  }

  window.addEventListener("scroll", setCalmFromScroll, { passive: true });
  window.addEventListener("resize", setCalmFromScroll);
  setCalmFromScroll();

  const yearEl = document.querySelector("[data-year]");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
})();
