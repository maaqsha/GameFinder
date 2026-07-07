(function () {
  var STORAGE_KEY = 'gamefinder-theme';
  var html = document.documentElement;

  function getPreferredTheme() {
    var stored = localStorage.getItem(STORAGE_KEY);
    if (stored === 'dark' || stored === 'light') return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function setTheme(theme) {
    html.setAttribute('data-bs-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
    var icon = document.getElementById('theme-icon');
    var label = document.getElementById('theme-label-text');
    if (icon) icon.textContent = theme === 'dark' ? '\u2600' : '\u263E';
    if (label) label.textContent = theme === 'dark' ? 'Dark' : 'Light';
  }

  function toggleTheme() {
    var current = html.getAttribute('data-bs-theme') || 'light';
    setTheme(current === 'dark' ? 'light' : 'dark');
  }

  document.addEventListener('DOMContentLoaded', function () {
    setTheme(getPreferredTheme());
    var btn = document.getElementById('theme-toggle-btn');
    if (btn) btn.addEventListener('click', toggleTheme);
  });
})();
