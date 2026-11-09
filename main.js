(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Fit giant one-line words to their container width */
  const fit = () => {
    const els = [...document.querySelectorAll('[data-fit]')].filter((el) => !el.classList.contains('extras-word'));
    els.forEach((el) => { el.style.fontSize = ''; el.style.display = 'inline-block'; });
    const sizes = els.map((el) => {
      const box = el.parentElement;
      const cs = getComputedStyle(box);
      const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
      const w = el.offsetWidth;
      const size = parseFloat(getComputedStyle(el).fontSize);
      return w && avail ? Math.floor(size * (avail / w) * 0.995) : 0;
    });
    els.forEach((el, i) => { el.style.display = ''; if (sizes[i]) el.style.fontSize = sizes[i] + 'px'; });
  };
  const refit = () => requestAnimationFrame(fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(refit);
  addEventListener('resize', refit);
  fit();

  /* Mobile menu */
  const btn = document.querySelector('.menu-btn');
  const menu = document.getElementById('menu');
  if (btn && menu) {
    const close = () => { menu.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.textContent = 'Menu'; };
    btn.addEventListener('click', () => {
      const open = !menu.classList.contains('open');
      menu.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.textContent = open ? 'Fechar' : 'Menu';
    });
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) close(); });
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && menu.classList.contains('open')) { close(); btn.focus(); } });
  }

  /* Staggered entrances: mark the parts of each section */
  const groups = [
    '.hero-top > *', '.hero-foot > *', '.courses > h2', '.about-pin > *', '.hours-head > *', '.spec',
    '.extras-intro', '.bars details', '.stair span', '.mission-photos img', '.mission-note',
    '.tile', '.contact-head > *',
    '.enroll .cell', '.portrait figcaption'
  ];
  const parts = [];
  groups.forEach((sel) => {
    document.querySelectorAll(sel).forEach((el, i) => {
      el.classList.add('rv');
      el.style.setProperty('--d', String(i % 6));
      parts.push(el);
    });
  });
  if (reduce || !('IntersectionObserver' in window)) {
    parts.forEach((el) => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -40px 0px', threshold: 0 });
    parts.forEach((el) => io.observe(el));
  }

  /* Marquee: duplicate the strip once so it loops seamlessly */
  const track = document.querySelector('.strip-track');
  if (track && !reduce) {
    [...track.children].forEach((f) => {
      const c = f.cloneNode(true);
      c.setAttribute('aria-hidden', 'true');
      c.querySelector('img').alt = '';
      track.appendChild(c);
    });
  }

  const strip = document.querySelector('.strip');
  const toggle = document.querySelector('.strip-toggle');
  if (strip && toggle) {
    toggle.addEventListener('click', () => {
      const paused = strip.classList.toggle('paused');
      toggle.setAttribute('aria-pressed', String(paused));
      toggle.textContent = paused ? 'Mover fotos' : 'Pausar fotos';
    });
  }

  /* Monte a matrícula */
  const form = document.getElementById('enroll');
  const idade = document.getElementById('idade');
  const periodo = document.getElementById('periodo');
  const out = document.getElementById('enroll-result');
  const text = document.getElementById('enroll-text');
  if (form && idade && periodo && out && text) {
    const update = () => {
      const [turma, faixa] = idade.value.split('|');
      const p = periodo.value;
      out.innerHTML = 'Turma indicada: <strong>' + turma + '</strong>, ' + p.toLowerCase() + '.';
      text.value = 'Olá! Vim pelo site do Cantinho do Mel. Tenho uma criança de ' + faixa +
        ' (turma ' + turma + '). Período de interesse: ' + p.toLowerCase() +
        '. Gostaria de saber valores e agendar uma visita.';
    };
    idade.addEventListener('change', update);
    periodo.addEventListener('change', update);
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      update();
      window.open('https://wa.me/5511948714027?text=' + encodeURIComponent(text.value), '_blank', 'noopener');
    });
    update();
  }
})();
