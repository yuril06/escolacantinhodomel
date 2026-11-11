/* Escola Cantinho do Mel — interações */
(() => {
  const ZAP = '5511948714027';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ano no rodapé */
  $$('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* cabeçalho: sombra ao rolar (o cabeçalho flutua sobre a página) */
  const header = $('.header');
  const onScroll = () => header && header.classList.toggle('is-scrolled', window.scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* menu no celular */
  const menuBtn = $('.menu-btn');
  const nav = $('#menu');
  if (menuBtn && nav) {
    const close = () => { nav.classList.remove('is-open'); menuBtn.setAttribute('aria-expanded', 'false'); };
    menuBtn.addEventListener('click', () => {
      const open = !nav.classList.contains('is-open');
      nav.classList.toggle('is-open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', (e) => { if (e.target.closest('a')) close(); });
    addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
    matchMedia('(min-width: 1081px)').addEventListener('change', close);
  }

  /* entradas: título, texto e foto sobem em sequência, uma vez */
  const reveal = $$('[data-reveal]');
  if ('IntersectionObserver' in window && !reduce.matches) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveal.forEach((el) => io.observe(el));
  } else {
    reveal.forEach((el) => el.classList.add('is-in'));
  }

  /* ---------- monte o dia do seu filho ---------- */
  const TURMAS = ['Berçário', 'Nível 1', 'Nível 2', 'Nível 3', 'Nível 4'];
  const TURMA_OPT = ['Berçário (4 meses a 2 anos)', 'Nível 1 (2 a 3 anos)', 'Nível 2 (3 a 4 anos)', 'Nível 3 (4 a 5 anos)', 'Nível 4 (5 a 6 anos)'];
  const PERIODO_OPT = { 5: 'Meio período (5 horas)', 8: 'Semi integral (8 horas)', 12: 'Integral (12 horas)' };
  const OPEN = 390; // 06h30
  const CLOSE = 1125; // 18h45
  const hhmm = (m) => `${String(Math.floor(m / 60)).padStart(2, '0')}h${String(m % 60).padStart(2, '0')}`;
  const ageText = (m) => {
    const y = Math.floor(m / 12), r = m % 12;
    if (y === 0) return `${r} meses`;
    const ys = `${y} ${y === 1 ? 'ano' : 'anos'}`;
    return r ? `${ys} e ${r} ${r === 1 ? 'mês' : 'meses'}` : ys;
  };
  const turmaOf = (m) => (m < 24 ? 0 : m < 36 ? 1 : m < 48 ? 2 : m < 60 ? 3 : 4);

  $$('[data-planner]').forEach((root) => {
    const age = $('[data-age]', root);
    const ageOut = $('[data-age-out]', root);
    const entry = $('[data-entry]', root);
    const fill = $('[data-fill]', root);
    const say = $('[data-say]', root);
    const times = $('[data-times]', root);
    const go = $('[data-planner-go]', root);
    const cells = $$('.comb__cell', root);
    const radios = $$('input[name="periodo"]', root);

    const update = () => {
      const months = +age.value;
      const t = turmaOf(months);
      const r = radios.find((x) => x.checked) || radios[1];
      const hours = +r.value;
      const len = hours * 60;
      const maxEntry = CLOSE - len;
      entry.max = String(Math.max(OPEN, maxEntry));
      if (+entry.value > maxEntry) entry.value = String(maxEntry);
      entry.disabled = maxEntry <= OPEN;
      const from = +entry.value;
      const to = from + len;
      const span = CLOSE - OPEN;
      fill.style.setProperty('--from', `${((from - OPEN) / span) * 100}%`);
      fill.style.setProperty('--len', `${(len / span) * 100}%`);
      ageOut.textContent = ageText(months);
      age.setAttribute('aria-valuetext', ageText(months));
      entry.setAttribute('aria-valuetext', `chega às ${hhmm(from)}`);
      cells.forEach((c, i) => c.classList.toggle('is-on', i === t));
      say.innerHTML = `Turma <b>${TURMAS[t]}</b>, no ${r.dataset.label.toLowerCase()}.`;
      times.innerHTML = `Chega às <b>${hhmm(from)}</b> e sai às <b>${hhmm(to)}</b>.`;
      const q = new URLSearchParams({ turma: String(t), periodo: String(hours), idade: ageText(months), chegada: hhmm(from) });
      go.href = `contato.html?${q}#agendar`;
    };
    [age, entry, ...radios].forEach((el) => el.addEventListener('input', update));
    update();
  });

  /* ---------- índice com prévia (aulas extras) ---------- */
  $$('.index__body').forEach((root) => {
    const frame = $('.index__frame', root);
    if (!frame) return;
    const pic = $('img', frame);
    const fine = matchMedia('(hover: hover) and (pointer: fine) and (min-width: 900px)');
    let warmed = false;
    const show = (row) => {
      if (!fine.matches) return;
      if (!warmed) { warmed = true; $$('[data-preview]', root).forEach((a) => { new Image().src = a.dataset.preview; }); }
      pic.src = row.dataset.preview;
      const y = row.offsetTop + row.offsetHeight / 2 - frame.offsetHeight / 2;
      const max = root.offsetHeight - frame.offsetHeight;
      const opening = !frame.classList.contains('is-open');
      if (opening) frame.style.transitionProperty = 'scale, opacity';
      frame.style.transform = `translateY(${Math.min(max, Math.max(0, y))}px)`;
      if (opening) { frame.getBoundingClientRect(); frame.style.transitionProperty = ''; }
      frame.classList.add('is-open');
    };
    $$('.index__row', root).forEach((row) => {
      row.addEventListener('pointerenter', () => show(row));
      row.addEventListener('focus', () => show(row));
    });
    root.addEventListener('pointerleave', () => frame.classList.remove('is-open'));
    root.addEventListener('focusout', (e) => { if (!root.contains(e.relatedTarget)) frame.classList.remove('is-open'); });
  });

  /* ---------- momentos: uma moldura, as fotos trocam ---------- */
  $$('[data-moments]').forEach((root) => {
    const imgs = $$('.moments__frame img', root);
    const btns = $$('.moments__list button', root);
    const cap = $('[data-cap-out]', root);
    const frame = $('.moments__frame', root);
    let i = 0, timer = null, visible = false;
    const set = (n) => {
      i = (n + imgs.length) % imgs.length;
      imgs.forEach((im, k) => {
        im.classList.toggle('is-on', k === i);
        if (k === i && im.loading === 'lazy') im.loading = 'eager';
      });
      btns.forEach((b, k) => b.setAttribute('aria-current', String(k === i)));
      cap.textContent = imgs[i].dataset.cap;
    };
    const play = () => { stop(); if (!reduce.matches && visible) timer = setInterval(() => set(i + 1), 3200); };
    const stop = () => { clearInterval(timer); timer = null; };
    btns.forEach((b) => b.addEventListener('click', () => { set(+b.dataset.i); play(); }));
    frame.addEventListener('click', () => { set(i + 1); play(); });
    frame.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); set(i + 1); play(); } });
    root.addEventListener('pointerenter', stop);
    root.addEventListener('pointerleave', play);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([en]) => { visible = en.isIntersecting; visible ? play() : stop(); }, { threshold: 0.3 }).observe(frame);
    }
  });

  /* ---------- formulários que viram mensagem de WhatsApp ---------- */
  const params = new URLSearchParams(location.search);
  $$('[data-zap-form]').forEach((form) => {
    const err = $('[data-error]', form);
    const turma = form.elements.turma;
    const periodo = form.elements.periodo;
    const nasc = form.elements.nascimento;

    // vindo do "monte o dia": preenche turma, período e chegada
    if (params.has('turma') && turma) turma.value = TURMA_OPT[+params.get('turma')] || '';
    if (params.has('periodo') && periodo) periodo.value = PERIODO_OPT[params.get('periodo')] || '';
    if (params.has('chegada') && form.elements.chegada) form.elements.chegada.value = params.get('chegada');

    // data de nascimento sugere a turma
    if (nasc && turma) {
      nasc.max = new Date().toISOString().slice(0, 10);
      nasc.addEventListener('change', () => {
        const d = new Date(nasc.value + 'T12:00:00');
        if (isNaN(d)) return;
        const now = new Date();
        const months = (now.getFullYear() - d.getFullYear()) * 12 + (now.getMonth() - d.getMonth()) - (now.getDate() < d.getDate() ? 1 : 0);
        const hint = $('[data-age-hint]', form);
        if (months < 4) { if (hint) hint.textContent = 'A escola recebe bebês a partir de 4 meses. Fale com a gente para planejar a entrada.'; return; }
        if (months > 83) { if (hint) hint.textContent = 'A escola atende até os 6 anos.'; return; }
        turma.value = TURMA_OPT[turmaOf(Math.min(months, 72))];
        if (hint) hint.textContent = `${ageText(months)}: sugerimos a turma ${TURMAS[turmaOf(Math.min(months, 72))]}.`;
      });
    }

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const f = form.elements;
      const missing = [...form.querySelectorAll('[required]')].filter((el) => !el.value.trim());
      if (missing.length) {
        err.textContent = 'Falta preencher: ' + missing.map((el) => form.querySelector(`label[for="${el.id}"]`).textContent.toLowerCase()).join(', ') + '.';
        err.classList.add('is-on');
        missing[0].focus();
        return;
      }
      err.classList.remove('is-on');
      const v = (name) => (f[name] && f[name].value.trim()) || '';
      const lines = [
        'Olá! Gostaria de agendar uma visita à Escola Cantinho do Mel.',
        '',
        `*Responsável:* ${v('responsavel')}`,
        `*Criança:* ${v('crianca')}`,
      ];
      if (v('nascimento')) lines.push(`*Nascimento:* ${v('nascimento').split('-').reverse().join('/')}`);
      else if (params.get('idade')) lines.push(`*Idade:* ${params.get('idade')}`);
      if (v('turma')) lines.push(`*Turma de interesse:* ${v('turma')}`);
      if (v('periodo')) lines.push(`*Período:* ${v('periodo')}`);
      if (v('chegada')) lines.push(`*Chegada pretendida:* ${v('chegada')}`);
      if (v('dia')) lines.push(`*Melhor horário para a visita:* ${v('dia')}`);
      if (v('telefone')) lines.push(`*Telefone:* ${v('telefone')}`);
      if (v('mensagem')) lines.push('', v('mensagem'));
      window.open(`https://wa.me/${ZAP}?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener');
    });
  });

  /* máscara simples de telefone */
  $$('input[type="tel"]').forEach((el) => el.addEventListener('input', () => {
    const d = el.value.replace(/\D/g, '').slice(0, 11);
    el.value = d.length > 10 ? `(${d.slice(0, 2)}) ${d.slice(2, 7)}-${d.slice(7)}`
      : d.length > 6 ? `(${d.slice(0, 2)}) ${d.slice(2, 6)}-${d.slice(6)}`
      : d.length > 2 ? `(${d.slice(0, 2)}) ${d.slice(2)}` : d;
  }));
})();
