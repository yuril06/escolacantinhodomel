(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const replay = (el, cls) => { if (reduce || !el) return; el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); };

  /* ---------- Menu ---------- */
  const btn = $('.menu-btn'), menu = $('#menu'), btnTxt = $('.menu-btn-txt');
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
    matchMedia('(min-width: 1061px)').addEventListener('change', (m) => { if (m.matches) set(false); });
  }

  /* ---------- Aberto agora? (horário de Brasília) ---------- */
  const brNow = () => {
    const parts = new Intl.DateTimeFormat('en-US', { timeZone: 'America/Sao_Paulo', weekday: 'short', hour: 'numeric', minute: 'numeric', hourCycle: 'h23' }).formatToParts(new Date());
    const get = (t) => parts.find((p) => p.type === t).value;
    return { day: get('weekday'), min: parseInt(get('hour'), 10) * 60 + parseInt(get('minute'), 10) };
  };
  const fmt = (m) => Math.floor(m / 60) + 'h' + String(m % 60).padStart(2, '0');
  const updateStatus = () => {
    $$('.status').forEach((s) => {
      const { day, min } = brNow();
      const weekday = !['Sat', 'Sun'].includes(day);
      const open = weekday && min >= 390 && min < 1140;
      s.classList.toggle('open', open);
      s.classList.toggle('closed', !open);
      let when = 'amanhã';
      if (weekday && min < 390) when = 'hoje';
      else if (day === 'Fri' || day === 'Sat') when = 'segunda';
      $('.status-txt', s).textContent = open ? 'Aberto agora' : 'Fechado · abre ' + when + ' às 6h30';
    });
  };
  updateStatus();
  setInterval(updateStatus, 60000);

  /* ---------- Períodos ---------- */
  $$('.periods').forEach((box) => {
    const tabs = $$('[role="tab"]', box), card = $('.pcard', box);
    const title = $('#p-title', box), tag = $('#p-tag', box), text = $('#p-text', box), fill = $('#p-fill', box), cta = $('#p-btn', box);
    const pos = (m) => ((m - 390) / 750) * 100;
    const select = (t, focus) => {
      tabs.forEach((x) => { x.setAttribute('aria-selected', String(x === t)); x.tabIndex = x === t ? 0 : -1; });
      title.textContent = t.dataset.title;
      tag.textContent = t.dataset.tag;
      text.textContent = t.dataset.text;
      cta.textContent = t.dataset.btn;
      fill.style.left = pos(+t.dataset.from) + '%';
      fill.style.right = (100 - pos(+t.dataset.to)) + '%';
      replay(card, 'swap');
      if (focus) t.focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t));
      t.addEventListener('keydown', (e) => {
        const k = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (k) { e.preventDefault(); select(tabs[(i + k + tabs.length) % tabs.length], true); }
      });
    });
  });

  /* ---------- Um dia no Cantinho ---------- */
  const day = [
    [390, 'Chegada e café da manhã', 'O portão abre às 6h30. Quem chega cedo toma café com calma, preparado na nossa cozinha.'],
    [465, 'Roda de conversa', 'A turma se encontra, canta, conta as novidades e combina o dia.'],
    [525, 'Atividades do Sistema Positivo', 'Hora de aprender fazendo: linguagem, números, natureza e muita mão na massa.'],
    [600, 'Lanche e parquinho', 'Fruta fresquinha e depois parquinho, para correr, subir e descer.'],
    [675, 'Almoço', 'Comida feita na hora, com o cardápio da nutricionista Aline Fregozzi.'],
    [735, 'Troca de período e descanso', 'Quem fica meio período da manhã vai para casa e chega a turma da tarde. No integral é hora do soninho.'],
    [855, 'Atividades da tarde', 'Histórias, artes, dramatização e brincadeiras em sala.'],
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
      if (i !== last) { title.textContent = day[i][1]; text.textContent = day[i][2]; if (last !== -1) replay(now, 'swap'); last = i; }
    };
    const { day: wd, min } = brNow();
    range.value = !['Sat', 'Sun'].includes(wd) && min >= 390 && min <= 1140 ? Math.round(min / 15) * 15 : 480;
    show(range.value);
    range.addEventListener('input', () => show(range.value));
  }

  /* ---------- Dúvidas: abre uma por vez, com animação ---------- */
  $$('.acc').forEach((acc) => {
    const items = $$('details', acc);
    const close = (d) => {
      const b = $('.acc-body', d);
      if (reduce) { d.open = false; return; }
      const a = b.animate([{ height: b.offsetHeight + 'px', opacity: 1 }, { height: '0px', opacity: 0 }], { duration: 240, easing: 'ease-out' });
      a.onfinish = () => { d.open = false; };
    };
    items.forEach((d) => {
      $('summary', d).addEventListener('click', (e) => {
        e.preventDefault();
        if (d.open) { close(d); return; }
        items.forEach((o) => { if (o !== d && o.open) close(o); });
        d.open = true;
        if (!reduce) { const b = $('.acc-body', d); b.animate([{ height: '0px', opacity: 0 }, { height: b.offsetHeight + 'px', opacity: 1 }], { duration: 320, easing: 'cubic-bezier(.2,.8,.2,1)' }); }
      });
    });
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
      meta.textContent = faixa + ' · ' + p;
      if (lastTurma && turma !== lastTurma) replay(cls, 'pop');
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
    '.hero-text > *', '.hero-card', '.page-hero-in > *',
    '.sec-title', '.cards > *', '.acts > *', '.partner', '.more-partners li',
    '.periods', '.clock', '.split-text > *', '.split-media',
    '.spaces > *', '.here', '.groups > *',
    '.extra', '.faq-side > *', '.acc details',
    '.enroll-picks > *', '.ticket', '.ccard', '.map', '.cta'
  ];
  const parts = [];
  groups.forEach((sel) => $$(sel).forEach((el, i) => {
    if (el.classList.contains('rv')) return;
    el.classList.add('rv'); el.style.setProperty('--d', String(i % 6)); parts.push(el);
  }));
  if (reduce || !('IntersectionObserver' in window)) parts.forEach((el) => el.classList.add('in'));
  else {
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -6% 0px' });
    parts.forEach((el) => io.observe(el));
  }

  /* ---------- Rolagem ---------- */
  const top = $('#top'), fab = $('.wa-fab');
  let ticking = false;
  const onScroll = () => {
    ticking = false;
    top.classList.toggle('scrolled', scrollY > 16);
    if (fab) fab.classList.toggle('show', scrollY > innerHeight * .45);
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();
})();
