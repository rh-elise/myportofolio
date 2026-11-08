/* star.js - tombol bintang Project/Experience lewat API, tanpa memuat ulang halaman. */

(function () {
  function getCookie(name) {
    const prefix = `${name}=`;
    const cookie = document.cookie
      .split(';')
      .map((value) => value.trim())
      .find((value) => value.startsWith(prefix));
    return cookie ? decodeURIComponent(cookie.slice(prefix.length)) : null;
  }

  function setText(root, selector, value) {
    const element = root.querySelector(selector);
    if (element) element.textContent = value;
  }

  function applyStar(button, data) {
    button.classList.toggle('is-starred', Boolean(data.is_starred));
    button.title = `${data.star_count} stars`;
    button.setAttribute(
      'aria-label',
      `${data.is_starred ? 'Unstar' : 'Star'} ${data.title || ''}`.trim()
    );

    setText(button, '[data-star-icon], .exp-star__icon', data.is_starred ? '★' : '☆');
    setText(button, '[data-star-count], .exp-star__count', data.star_count);
    setText(button, '[data-star-label]', data.is_starred ? 'Starred' : 'Star');

    // Simpan angka terbaru di kartu agar hero tetap sinkron saat kartu dipilih.
    const card = button.closest('[data-starred]')
        || document.querySelector(`[data-starred][data-id="${data.id}"]`);
    if (card) {
      card.dataset.starred = data.is_starred ? 'true' : 'false';
      card.dataset.count = data.star_count;
    }

    document.dispatchEvent(new CustomEvent('star:updated', { detail: data }));
  }

  async function toggleStar(button) {
    button.disabled = true;

    try {
      const response = await fetch(button.dataset.starUrl, {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
        },
        credentials: 'same-origin',
      });

      if (!response.ok) throw new Error(`Request failed (HTTP ${response.status}).`);

      const data = await response.json();
      applyStar(button, data);
      showToast('Success', data.is_starred ? 'Starred.' : 'Unstarred.', 'success');
    } catch (error) {
      showToast('Could not update star', error.message, 'error');
    } finally {
      button.disabled = false;
    }
  }

  document.addEventListener('click', function (event) {
    const button = event.target.closest('[data-star-url]');
    if (!button) return;

    event.preventDefault();
    toggleStar(button);
  });
})();
