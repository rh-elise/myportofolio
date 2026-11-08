/* ==========================================================================
   form_errors.js - Error validasi form
   --------------------------------------------------------------------------
   Menampilkan error dari respons API tepat di bawah field yang bermasalah,
   sama seperti form login dan signup. Toast tetap dipakai untuk kegagalan
   jaringan atau pesan yang tidak terikat ke field tertentu.
   ========================================================================== */

(function () {
  // Key yang bukan nama field: ditampilkan sebagai satu pesan umum.
  const GENERAL_KEYS = new Set(['non_field_errors', 'detail', 'message', 'error']);

  function toMessages(value) {
    if (Array.isArray(value)) return value.flatMap(toMessages);
    if (typeof value === 'string') return [value];
    if (value && typeof value === 'object') {
      // Format DRF get_json_data: { code, message }.
      if (typeof value.message === 'string') return [value.message];
      return Object.values(value).flatMap(toMessages);
    }
    return [];
  }

  function clear(form) {
    if (!form) return;

    form.querySelectorAll('.form-error[data-js-error]').forEach((element) => {
      element.remove();
    });

    form.querySelectorAll('[aria-invalid="true"]').forEach((element) => {
      element.removeAttribute('aria-invalid');
    });
  }

  function show(form, errors) {
    if (!form || !errors) return 0;

    clear(form);

    let shown = 0;
    const general = [];

    Object.entries(errors).forEach(([name, value]) => {
      const messages = toMessages(value);
      if (!messages.length) return;

      if (GENERAL_KEYS.has(name)) {
        general.push(...messages);
        return;
      }

      // Cari input dengan nama field yang sama, lalu tempel error di grupnya.
      const field = form.querySelector(`[name="${name}"]`);
      const group = field ? field.closest('.form-group') : null;

      if (!field || !group) {
        general.push(...messages);
        return;
      }

      messages.forEach((message) => {
        const paragraph = document.createElement('p');
        paragraph.className = 'form-error';
        paragraph.dataset.jsError = 'true';
        paragraph.textContent = message;
        group.appendChild(paragraph);
      });

      field.setAttribute('aria-invalid', 'true');
      shown += 1;
    });

    if (general.length) {
      const paragraph = document.createElement('p');
      paragraph.className = 'form-error form-error--general';
      paragraph.dataset.jsError = 'true';
      paragraph.textContent = general.join(' ');

      const actions = form.querySelector('.form-actions');
      if (actions) {
        form.insertBefore(paragraph, actions);
      } else {
        form.appendChild(paragraph);
      }
      shown += 1;
    }

    const firstInvalid = form.querySelector('[aria-invalid="true"]');
    if (firstInvalid) firstInvalid.focus();

    return shown;
  }

  window.FormErrors = { show, clear };
})();
