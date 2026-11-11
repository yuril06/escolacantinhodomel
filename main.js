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
  const reveal = $$('[data-reveal], [data-stagger]');
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
    const cells = $$('.bubble', root);
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

  /* ---------- galeria com foto ampliada ---------- */
  const lb = $('[data-lightbox]');
  if (lb) {
    const lbImg = $('img', lb), lbCap = $('figcaption', lb);
    let items = [], at = 0, last = null;
    const show = (n) => {
      at = (n + items.length) % items.length;
      const it = items[at];
      lbImg.src = it.dataset.full; lbImg.alt = $('img', it).alt; lbCap.textContent = $('span', it).textContent;
      lbImg.style.animation = 'none'; void lbImg.offsetWidth; lbImg.style.animation = '';
    };
    const open = (list, n) => { items = list; last = document.activeElement; show(n); lb.classList.add('is-open'); document.body.style.overflow = 'hidden'; $('.lb-close', lb).focus(); };
    const close = () => { lb.classList.remove('is-open'); document.body.style.overflow = ''; if (last) last.focus(); };
    $$('[data-gallery]').forEach((g) => {
      const list = $$('[data-full]', g);
      list.forEach((b, n) => b.addEventListener('click', () => open(list, n)));
    });
    $('.lb-close', lb).addEventListener('click', close);
    $('.lb-prev', lb).addEventListener('click', () => show(at - 1));
    $('.lb-next', lb).addEventListener('click', () => show(at + 1));
    lb.addEventListener('click', (e) => { if (e.target === lb) close(); });
    addEventListener('keydown', (e) => {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(at - 1);
      if (e.key === 'ArrowRight') show(at + 1);
    });
    let x0 = null;
    lb.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', (e) => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) show(at + (dx < 0 ? 1 : -1)); x0 = null; });
  }

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
