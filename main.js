(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------- Ajusta palavras gigantes à largura ---------- */
  const fit = () => {
    const els = $$('[data-fit]');
    els.forEach((el) => { el.style.fontSize = ''; });
    const small = innerWidth <= 760;
    const sizes = els.map((el) => {
      if (small && el.closest('.mega')) return 0;
      const box = el.closest('.wrap') || el.parentElement;
      const cs = getComputedStyle(box);
      const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
      const w = el.offsetWidth;
      const size = parseFloat(getComputedStyle(el).fontSize);
      return w && avail ? Math.floor(size * (avail / w) * 0.992) : 0;
    });
    els.forEach((el, i) => { if (sizes[i]) el.style.fontSize = sizes[i] + 'px'; });
  };
  const refit = () => requestAnimationFrame(fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(refit);
  addEventListener('resize', refit);
  fit();

  /* ---------- Menu ---------- */
  const btn = $('.menu-btn');
  const menu = $('#menu');
  const btnTxt = $('.menu-btn-txt');
  if (btn && menu) {
    const set = (open) => {
      menu.classList.toggle('open', open);
      document.body.classList.toggle('menu-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (btnTxt) btnTxt.textContent = open ? 'Fechar' : 'Menu';
      document.documentElement.style.overflow = open ? 'hidden' : '';
    };
    btn.addEventListener('click', () => set(!menu.classList.contains('open')));
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && menu.classList.contains('open')) { set(false); btn.focus(); } });
    matchMedia('(min-width: 1081px)').addEventListener('change', (m) => { if (m.matches) set(false); });
  }

  /* ---------- Aberto agora? (horário de Brasília) ---------- */
  const brNow = () => {
    const parts = new Intl.DateTimeFormat('en-US', { timeZone: 'America/Sao_Paulo', weekday: 'short', hour: 'numeric', minute: 'numeric', hourCycle: 'h23' }).formatToParts(new Date());
    const get = (t) => parts.find((p) => p.type === t).value;
    return { day: get('weekday'), min: parseInt(get('hour'), 10) * 60 + parseInt(get('minute'), 10) };
  };
  const fmt = (m) => Math.floor(m / 60) + 'h' + String(m % 60).padStart(2, '0');
  const status = $('#status');
  const updateStatus = () => {
    if (!status) return;
    const { day, min } = brNow();
    const weekday = !['Sat', 'Sun'].includes(day);
    const open = weekday && min >= 390 && min < 1140;
    const txt = $('.status-txt', status);
    status.classList.toggle('open', open);
    status.classList.toggle('closed', !open);
    let when = 'amanhã';
    if (weekday && min < 390) when = 'hoje';
    else if (day === 'Fri' || day === 'Sat') when = 'segunda';
    txt.textContent = open ? 'Aberto agora · até as 19h' : 'Fechado agora · abre ' + when + ' às 6h30';
  };
  updateStatus();
  setInterval(updateStatus, 60000);

  /* ---------- Um dia no Cantinho ---------- */
  const day = [
    [390, 'Chegada e café da manhã', 'O portão abre às 6h30. Quem chega cedo toma café com calma, na nossa cozinha.'],
    [465, 'Roda de conversa', 'A turma se encontra, canta, conta as novidades e combina o dia.'],
    [525, 'Atividades do Sistema Positivo', 'Hora de aprender fazendo: linguagem, números, natureza e muita mão na massa.'],
    [600, 'Lanche e parquinho', 'Fruta fresquinha e depois parquinho, para correr, subir e descer.'],
    [675, 'Almoço', 'Comida feita na hora, com o cardápio da nutricionista Aline Fregozzi.'],
    [735, 'Saída do meio período e descanso', 'Quem fica no meio período da manhã vai para casa. Os outros descansam no soninho.'],
    [855, 'Atividades da tarde', 'Histórias, artes, dramatização e brincadeiras dirigidas em sala.'],
    [930, 'Lanche da tarde', 'Uma pausa gostosa antes da próxima aventura.'],
    [975, 'Aulas extras', 'Ballet, taekwondo, musicalização, futebol, inglês, artes e educação física, conforme a grade da turma.'],
    [1050, 'Jantar', 'No período integral, a criança janta antes de ir para casa.'],
    [1095, 'Saída até as 19h', 'A família busca com tranquilidade. Até amanhã!']
  ];
  const range = $('#clock-range');
  if (range) {
    const tEl = $('#clock-time'), title = $('#clock-title'), text = $('#clock-text'), now = $('.clock-now'), fill = $('#clock-fill');
    const track = $('.clock-track');
    let last = -1;
    const show = (v) => {
      v = Number(v);
      let i = 0;
      day.forEach((d, k) => { if (v >= d[0]) i = k; });
      tEl.textContent = fmt(v);
      const p = (v - 390) / (1140 - 390);
      track.style.setProperty('--v', p);
      range.setAttribute('aria-valuetext', fmt(v) + ', ' + day[i][1].toLowerCase());
      if (i !== last) {
        title.textContent = day[i][1];
        text.textContent = day[i][2];
        if (!reduce && last !== -1) { now.classList.remove('swap'); void now.offsetWidth; now.classList.add('swap'); }
        last = i;
      }
    };
    const { day: wd, min } = brNow();
    const startAt = !['Sat', 'Sun'].includes(wd) && min >= 390 && min <= 1140 ? Math.round(min / 15) * 15 : 480;
    range.value = startAt;
    show(range.value);
    range.addEventListener('input', () => show(range.value));
  }

  /* ---------- Fitas que rolam sozinhas: duplica para loop contínuo ---------- */
  ['.ribbon-track', '.strip-track'].forEach((sel) => {
    const track = $(sel);
    if (!track || reduce) return;
    [...track.children].forEach((c) => {
      const k = c.cloneNode(true);
      k.setAttribute('aria-hidden', 'true');
      k.removeAttribute('aria-label');
      k.removeAttribute('role');
      track.appendChild(k);
    });
  });
  const strip = $('.strip');
  const toggle = $('.strip-toggle');
  if (strip && toggle) {
    if (reduce) toggle.hidden = true;
    toggle.addEventListener('click', () => {
      const paused = strip.classList.toggle('paused');
      toggle.setAttribute('aria-pressed', String(paused));
      toggle.textContent = paused ? 'Mover' : 'Pausar';
    });
  }

  /* ---------- Aulas extras: abre uma por vez, com animação ---------- */
  const bars = $$('#bars details');
  bars.forEach((d) => {
    const sum = $('summary', d);
    sum.addEventListener('click', (e) => {
      e.preventDefault();
      const opening = !d.open;
      if (opening) bars.forEach((o) => { if (o !== d && o.open) collapse(o); });
      opening ? expand(d) : collapse(d);
    });
    function expand(el) {
      el.open = true;
      if (reduce) return;
      const b = $('.bar-body', el);
      const h = b.offsetHeight;
      b.animate([{ height: '0px', opacity: 0 }, { height: h + 'px', opacity: 1 }], { duration: 420, easing: 'cubic-bezier(.2,.8,.2,1)' });
    }
    function collapse(el) {
      if (reduce) { el.open = false; return; }
      const b = $('.bar-body', el);
      const a = b.animate([{ height: b.offsetHeight + 'px', opacity: 1 }, { height: '0px', opacity: 0 }], { duration: 320, easing: 'cubic-bezier(.2,.8,.2,1)' });
      a.onfinish = () => { el.open = false; };
    }
  });

  /* ---------- Monte a matrícula ---------- */
  const form = $('#enroll');
  if (form) {
    const cls = $('#ticket-class'), meta = $('#ticket-meta'), msg = $('#ticket-msg'), hidden = $('#enroll-text'), kid = $('#kid');
    let lastTurma = '';
    const update = () => {
      const [turma, faixa] = form.idade.value.split('|');
      const p = form.periodo.value.toLowerCase();
      const per = p.startsWith('meio') ? p : 'período ' + p;
      const nome = kid.value.trim();
      cls.textContent = turma;
      meta.textContent = 'Turma indicada para ' + faixa + ', ' + per;
      if (turma !== lastTurma && lastTurma && !reduce) { cls.classList.remove('pop'); void cls.offsetWidth; cls.classList.add('pop'); }
      lastTurma = turma;
      const quem = nome ? 'Gostaria de informações de matrícula para ' + nome + ', de ' + faixa : 'Tenho uma criança de ' + faixa;
      const t = 'Olá! Vim pelo site do Cantinho do Mel. ' + quem + ' (turma ' + turma + '), ' + per + '. Pode me passar os valores e um horário para visita?';
      msg.textContent = t;
      hidden.value = t;
    };
    form.addEventListener('change', update);
    kid.addEventListener('input', update);
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      update();
      window.open('https://wa.me/5511948714027?text=' + encodeURIComponent(hidden.value), '_blank', 'noopener');
    });
    update();
  }

  /* ---------- Entradas em sequência ---------- */
  const groups = [
    '.hero-lede > *', '.hero-side > *', '.hero-foot > *',
    '.about-pin > *', '.portrait',
    '.courses-head > *', '.sheet-text > *',
    '.day-head > *', '.spec', '.clock',
    '.extras-col > *', '.bars details',
    '.stair span', '.mission-photos .ph', '.mission-note',
    '.tile', '.card > *',
    '.band-grid > *',
    '.contact-head > *', '.enroll-picks > *', '.ticket', '.contact-info', '.map',
    '.foot-top > *', '.foot-call > *'
  ];
  const parts = [];
  groups.forEach((sel) => {
    $$(sel).forEach((el, i) => {
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
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0 });
    parts.forEach((el) => io.observe(el));
  }

  /* ---------- Números que contam ---------- */
  const counters = $$('[data-count]');
  if (!reduce && 'IntersectionObserver' in window) {
    const co = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        co.unobserve(e.target);
        const el = e.target, end = Number(el.dataset.count);
        const start = end > 1000 ? end - 40 : 0;
        const t0 = performance.now(), dur = 1300;
        const tick = (t) => {
          const k = Math.min(1, (t - t0) / dur);
          const ease = 1 - Math.pow(1 - k, 3);
          el.textContent = String(Math.round(start + (end - start) * ease));
          if (k < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: .6 });
    counters.forEach((c) => co.observe(c));
  }

  /* ---------- Rolagem: topo, abelha, nome que pesa, foto ---------- */
  const top = $('#top');
  const bee = $('.progress');
  const mega = $('.mega-line');
  const heroImg = $('.hero-photo img');
  const fab = $('.wa-fab');
  let lastY = scrollY, ticking = false;
  const onScroll = () => {
    ticking = false;
    const y = scrollY;
    const max = document.documentElement.scrollHeight - innerHeight;
    top.classList.toggle('scrolled', y > 24);
    if (bee) {
      bee.style.setProperty('--p', Math.min(1, Math.max(0, y / max)).toFixed(4));
      bee.style.setProperty('--tilt', Math.max(-14, Math.min(14, (y - lastY) * .8)).toFixed(1));
    }
    if (fab) fab.classList.toggle('show', y > innerHeight * .6);
    if (!reduce) {
      const k = Math.min(1, y / (innerHeight * .9));
      if (mega) mega.style.transform = 'scale(' + (1 - k * .07).toFixed(4) + ')';
      if (heroImg) heroImg.style.transform = 'scale(' + (1.08 - k * .08).toFixed(4) + ') translateY(' + (k * -3).toFixed(2) + '%)';
    }
    lastY = y;
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();
  if (bee) {
    let idle;
    addEventListener('scroll', () => { clearTimeout(idle); idle = setTimeout(() => bee.style.setProperty('--tilt', 0), 160); }, { passive: true });
  }

  /* ---------- Link ativo no menu ---------- */
  const links = $$('.menu a[href^="#"]');
  const map = new Map(links.map((a) => [a.getAttribute('href').slice(1), a]));
  if ('IntersectionObserver' in window) {
    const so = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        const a = map.get(e.target.id);
        if (!a) return;
        if (e.isIntersecting) { links.forEach((l) => l.removeAttribute('aria-current')); a.setAttribute('aria-current', 'true'); }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    map.forEach((_, id) => { const s = document.getElementById(id); if (s) so.observe(s); });
  }
})();
