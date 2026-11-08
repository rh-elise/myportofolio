/* toast.js - notifikasi ringan: satu stack, bisa ditutup, hilang otomatis. */

(function () {
  const DEFAULT_DURATION = 4500;
  const MAX_TOASTS = 4;
  const timers = new WeakMap();

  function getStack() {
    return document.getElementById('toast-stack');
  }

  function clearTimer(toast) {
    const timer = timers.get(toast);
    if (timer) {
      clearTimeout(timer);
      timers.delete(toast);
    }
  }

  function dismissToast(toast) {
    if (!toast || !toast.isConnected) return;

    clearTimer(toast);
    toast.classList.remove('toast--visible');
    toast.classList.add('toast--leaving');

    // Hapus dari DOM setelah animasi selesai.
    const remove = () => {
      if (toast.isConnected) toast.remove();
    };
    toast.addEventListener('transitionend', remove, { once: true });
    setTimeout(remove, 250);
  }

  function armTimer(toast, duration) {
    if (!duration) return;

    clearTimer(toast);
    const timer = setTimeout(() => dismissToast(toast), duration);
    timers.set(toast, timer);
  }

  function normalizeType(type) {
    if (type === 'success') return 'success';
    if (type === 'error' || type === 'danger') return 'error';
    if (type === 'warning') return 'warning';
    if (type === 'info') return 'info';
    return 'normal';
  }

  function buildToast(title, message, type) {
    const toast = document.createElement('div');
    toast.className = `toast toast--${normalizeType(type)}`;
    toast.setAttribute('role', 'status');

    const text = document.createElement('span');
    text.className = 'toast__text';

    // Judul dan pesan tampil dalam satu baris agar toast tetap ringkas.
    if (title) {
      const heading = document.createElement('strong');
      heading.className = 'toast__title';
      heading.textContent = title;
      text.appendChild(heading);
    }

    if (message) {
      const body = document.createElement('span');
      body.className = 'toast__message';
      body.textContent = message;
      text.appendChild(body);
    }

    const close = document.createElement('button');
    close.type = 'button';
    close.className = 'toast__close';
    close.setAttribute('aria-label', 'Dismiss notification');
    close.textContent = '\u00d7';

    toast.append(text, close);
    return toast;
  }

  function watchToast(toast, duration) {
    armTimer(toast, duration);

    // Jangan hilang saat pengguna sedang membaca atau menutupnya.
    toast.addEventListener('mouseenter', () => clearTimer(toast));
    toast.addEventListener('mouseleave', () => armTimer(toast, 2000));
    toast.addEventListener('focusin', () => clearTimer(toast));
    toast.addEventListener('focusout', () => armTimer(toast, 2000));
  }

  function showToast(title, message, type = 'normal', duration = DEFAULT_DURATION) {
    const stack = getStack();
    if (!stack) return;

    // Batasi jumlah toast agar layar tidak penuh.
    while (stack.querySelectorAll('.toast').length >= MAX_TOASTS) {
      dismissToast(stack.querySelector('.toast'));
    }

    const toast = buildToast(title, message, type);
    stack.appendChild(toast);

    // Mulai dari posisi tersembunyi, lalu tampilkan pada frame berikutnya.
    requestAnimationFrame(() => toast.classList.add('toast--visible'));
    watchToast(toast, duration);

    return toast;
  }

  // Delegasi klik untuk tombol tutup, termasuk toast dari Django messages.
  const stack = getStack();
  if (stack) {
    stack.addEventListener('click', (event) => {
      const closeButton = event.target.closest('.toast__close');
      if (closeButton) dismissToast(closeButton.closest('.toast'));
    });

    stack.querySelectorAll('.toast').forEach((toast) => {
      requestAnimationFrame(() => toast.classList.add('toast--visible'));
      watchToast(toast, 6000);
    });
  }

  // Dipakai oleh script halaman (experience, projects, form edit, dll.).
  window.showToast = showToast;
})();
