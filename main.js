(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

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
    matchMedia('(min-width: 1041px)').addEventListener('change', (m) => { if (m.matches) set(false); });
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
    status.classList.toggle('open', open);
    status.classList.toggle('closed', !open);
    let when = 'amanhã';
    if (weekday && min < 390) when = 'hoje';
    else if (day === 'Fri' || day === 'Sat') when = 'segunda';
    $('.status-txt', status).textContent = open ? 'Aberto agora · até as 19h' : 'Fechado agora · abre ' + when + ' às 6h30';
  };
  updateStatus();
  setInterval(updateStatus, 60000);

  /* ---------- Abas dos cursos ---------- */
  const tabs = $$('.tabs [role="tab"]');
  if (tabs.length) {
    const select = (tab, focus) => {
      tabs.forEach((t) => {
        const on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        const p = document.getElementById(t.getAttribute('aria-controls'));
        p.hidden = !on;
        if (on && !reduce) { p.classList.remove('enter'); void p.offsetWidth; p.classList.add('enter'); }
      });
      if (focus) tab.focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t));
      t.addEventListener('keydown', (e) => {
        const k = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (k) { e.preventDefault(); select(tabs[(i + k + tabs.length) % tabs.length], true); }
        if (e.key === 'Home') { e.preventDefault(); select(tabs[0], true); }
        if (e.key === 'End') { e.preventDefault(); select(tabs[tabs.length - 1], true); }
      });
    });
    tabs.forEach((t) => { document.getElementById(t.getAttribute('aria-controls')).hidden = t.getAttribute('aria-selected') !== 'true'; });
  }

  /* ---------- Um dia no Cantinho ---------- */
  const day = [
    [390, 'Chegada e café da manhã', 'O portão abre às 6h30. Quem chega cedo toma café com calma, preparado na nossa cozinha.'],
    [465, 'Roda de conversa', 'A turma se encontra, canta, conta as novidades e combina o dia.'],
    [525, 'Atividades do Sistema Positivo', 'Hora de aprender fazendo: linguagem, números, natureza e muita mão na massa.'],
    [600, 'Lanche e parquinho', 'Fruta fresquinha e depois parquinho, para correr, subir e descer.'],
    [675, 'Almoço', 'Comida feita na hora, com o cardápio da nutricionista Aline Fregozzi.'],
    [735, 'Saída do meio período e descanso', 'Quem fica meio período vai para casa. Os outros descansam no soninho.'],
    [855, 'Atividades da tarde', 'Histórias, artes, dramatização e brincadeiras dirigidas em sala.'],
    [930, 'Lanche da tarde', 'Uma pausa gostosa antes da próxima aventura.'],
    [975, 'Aulas extras', 'Ballet, taekwondo, musicalização, futebol, inglês, artes e educação física, conforme a grade da turma.'],
    [1050, 'Jantar', 'No período integral, a criança janta antes de ir para casa.'],
    [1095, 'Saída até as 19h', 'A família busca com tranquilidade. Até amanhã!']
  ];
  const range = $('#clock-range');
  if (range) {
    const tEl = $('#clock-time'), title = $('#clock-title'), text = $('#clock-text'), now = $('.clock-now'), track = $('.clock-track');
    let last = -1;
    const show = (v) => {
      v = Number(v);
      let i = 0;
      day.forEach((d, k) => { if (v >= d[0]) i = k; });
      tEl.textContent = fmt(v);
      track.style.setProperty('--v', (v - 390) / 750);
      range.setAttribute('aria-valuetext', fmt(v) + ', ' + day[i][1].toLowerCase());
      if (i !== last) {
        title.textContent = day[i][1];
        text.textContent = day[i][2];
        if (!reduce && last !== -1) { now.classList.remove('swap'); void now.offsetWidth; now.classList.add('swap'); }
        last = i;
      }
    };
    const { day: wd, min } = brNow();
    range.value = !['Sat', 'Sun'].includes(wd) && min >= 390 && min <= 1140 ? Math.round(min / 15) * 15 : 480;
    show(range.value);
    range.addEventListener('input', () => show(range.value));
  }

  /* ---------- Acordeão das dúvidas (animado) ---------- */
  $$('.acc details').forEach((d) => {
    const sum = $('summary', d), body = $('.acc-body', d);
    sum.addEventListener('click', (e) => {
      if (reduce) return;
      e.preventDefault();
      if (d.open) {
        const a = body.animate([{ height: body.offsetHeight + 'px', opacity: 1 }, { height: '0px', opacity: 0 }], { duration: 260, easing: 'cubic-bezier(.2,.8,.2,1)' });
        a.onfinish = () => { d.open = false; };
      } else {
        d.open = true;
        body.animate([{ height: '0px', opacity: 0 }, { height: body.offsetHeight + 'px', opacity: 1 }], { duration: 340, easing: 'cubic-bezier(.2,.8,.2,1)' });
      }
    });
  });

  /* ---------- Espaços: setas do carrossel ---------- */
  const sc = $('.rooms-scroller');
  if (sc) {
    const navs = $$('.nav-btn');
    const upd = () => {
      navs.forEach((b) => {
        const dir = Number(b.dataset.dir);
        b.disabled = dir < 0 ? sc.scrollLeft <= 4 : sc.scrollLeft + sc.clientWidth >= sc.scrollWidth - 4;
      });
    };
    navs.forEach((b) => b.addEventListener('click', () => {
      const card = sc.querySelector('figure');
      sc.scrollBy({ left: Number(b.dataset.dir) * (card.offsetWidth + 16) * 2, behavior: reduce ? 'auto' : 'smooth' });
    }));
    sc.addEventListener('scroll', upd, { passive: true });
    addEventListener('resize', upd);
    upd();
  }

  /* ---------- Galeria: amplia a foto ---------- */
  const lb = $('#lightbox');
  if (lb && typeof lb.showModal === 'function') {
    const lbImg = $('img', lb), lbCap = $('.lb-cap', lb);
    $$('.zoom').forEach((z) => z.addEventListener('click', () => {
      const im = $('img', z);
      lbImg.src = im.currentSrc || im.src;
      lbImg.alt = im.alt;
      lbCap.textContent = z.dataset.cap || '';
      lb.showModal();
    }));
    $('.lb-close', lb).addEventListener('click', () => lb.close());
    lb.addEventListener('click', (e) => { if (e.target === lb) lb.close(); });
  }

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
      meta.textContent = faixa + ' · ' + p;
      if (lastTurma && turma !== lastTurma && !reduce) { cls.classList.remove('pop'); void cls.offsetWidth; cls.classList.add('pop'); }
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
    '.hero-text > *', '.hero-facts li', '.hero-photo',
    '.seals-in > *',
    '.mosaic > *', '.about-text > h2', '.about-text > .lede', '.pillars li',
    '.sec-head > *', '.tabs', '.panels',
    '.clock',
    '.act',
    '.mission-photo', '.mission-text > *',
    '.gal-grid li', '.rooms-scroller figure',
    '.faq-side > *', '.acc details',
    '.enroll-picks > *', '.ticket',
    '.contact-info', '.map',
    '.foot-cta > *'
  ];
  const parts = [];
  groups.forEach((sel) => {
    $$(sel).forEach((el, i) => {
      if (el.classList.contains('rv')) return;
      el.classList.add('rv');
      el.style.setProperty('--d', String(i % 5));
      parts.push(el);
    });
  });
  if (reduce || !('IntersectionObserver' in window)) {
    parts.forEach((el) => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0 });
    parts.forEach((el) => io.observe(el));
  }

  /* ---------- Números que contam ---------- */
  if (!reduce && 'IntersectionObserver' in window) {
    const co = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        co.unobserve(e.target);
        const el = e.target, end = Number(el.dataset.count);
        const start = end > 1000 ? end - 30 : 0;
        const t0 = performance.now(), dur = 1200;
        const tick = (t) => {
          const k = Math.min(1, (t - t0) / dur);
          el.textContent = String(Math.round(start + (end - start) * (1 - Math.pow(1 - k, 3))));
          if (k < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: .6 });
    $$('[data-count]').forEach((c) => co.observe(c));
  }

  /* ---------- Rolagem: topo, abelha, foto do topo, botão do WhatsApp ---------- */
  const top = $('#top');
  const bee = $('.progress');
  const heroImg = $('.hero-photo img');
  const fab = $('.wa-fab');
  let lastY = scrollY, ticking = false, idle;
  const onScroll = () => {
    ticking = false;
    const y = scrollY;
    const max = Math.max(1, document.documentElement.scrollHeight - innerHeight);
    top.classList.toggle('scrolled', y > 20);
    if (bee) {
      bee.style.setProperty('--p', Math.min(1, Math.max(0, y / max)).toFixed(4));
      bee.style.setProperty('--tilt', Math.max(-12, Math.min(12, (y - lastY) * .6)).toFixed(1));
      clearTimeout(idle); idle = setTimeout(() => bee.style.setProperty('--tilt', 0), 160);
    }
    if (fab) fab.classList.toggle('show', y > innerHeight * .5);
    if (heroImg && !reduce) {
      const k = Math.min(1, y / innerHeight);
      heroImg.style.transform = 'scale(' + (1.04 - k * .04).toFixed(4) + ')';
    }
    lastY = y;
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* ---------- Link ativo no menu ---------- */
  const links = $$('.menu a[href^="#"]:not(.btn)');
  const map = new Map(links.map((a) => [a.getAttribute('href').slice(1), a]));
  if ('IntersectionObserver' in window) {
    const so = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        const a = map.get(e.target.id);
        if (a && e.isIntersecting) { links.forEach((l) => l.removeAttribute('aria-current')); a.setAttribute('aria-current', 'true'); }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    map.forEach((_, id) => { const s = document.getElementById(id); if (s) so.observe(s); });
  }
})();
