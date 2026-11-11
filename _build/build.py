# Monta as páginas do site: cada arquivo em _build/pages/ recebe o mesmo
# <head>, cabeçalho, rodapé e scripts. Rode: python _build/build.py
import json, os, re, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)

ESCOLA = {
    "nome": "Escola Cantinho do Mel",
    "fone": "(11) 2677-8022",
    "fone_link": "tel:+551126778022",
    "zap": "(11) 94871-4027",
    "zap_num": "5511948714027",
    "email": "contato@escolacantinhodomel.com.br",
    "rua": "Rua Colúmbia, 438",
    "bairro": "Parque das Nações",
    "cidade": "Santo André, SP",
    "cep": "09241-000",
    "horario": "Segunda a sexta, das 06h30 às 18h45",
    "maps": "https://www.google.com/maps?ll=-23.632686,-46.525478&z=18&t=m&hl=pt-BR&gl=BR&mapclient=embed&cid=11133067005482875823",
    "instagram": "https://www.instagram.com/cantinhodomel/",
    "facebook": "https://www.facebook.com/escolacantinhodomel/",
    "youtube": "https://www.youtube.com/channel/UCcw24CynVY4-346pbGE55BQ",
    "url": "https://escolacantinhodomel.com.br/",
}

def zap(msg="Olá! Gostaria de agendar uma visita à Escola Cantinho do Mel."):
    return f"https://wa.me/{ESCOLA['zap_num']}?text=" + urllib.parse.quote(msg)

ICON = {
    "zap": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2a9.9 9.9 0 0 0-8.5 15l-1.4 5.1 5.24-1.37A9.9 9.9 0 1 0 12.04 2Zm0 18.1a8.2 8.2 0 0 1-4.18-1.15l-.3-.18-3.1.82.83-3.03-.2-.31a8.2 8.2 0 1 1 6.95 3.85Zm4.5-6.14c-.25-.12-1.46-.72-1.69-.8-.23-.08-.39-.12-.55.12-.16.25-.63.8-.78.97-.14.16-.29.18-.53.06-.25-.12-1.04-.38-1.98-1.22-.73-.65-1.23-1.46-1.37-1.7-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.15.16-.25.25-.41.08-.17.04-.31-.02-.43-.06-.13-.55-1.33-.76-1.82-.2-.48-.4-.41-.55-.42h-.47a.9.9 0 0 0-.65.31c-.23.25-.86.84-.86 2.04 0 1.2.88 2.37 1 2.53.12.17 1.73 2.64 4.2 3.7.58.26 1.04.41 1.4.52.59.19 1.12.16 1.54.1.47-.07 1.46-.6 1.66-1.17.2-.58.2-1.07.15-1.17-.06-.1-.22-.17-.47-.29Z"/></svg>',
    "tel": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8.5V6.8c0-.8.5-1 1-1h2.5V2H14c-3.4 0-4.2 2.5-4.2 4.2v2.3H7.5V12h2.3v10H14V12h3l.4-3.5H14Z"/></svg>',
    "yt": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8ZM9.8 15V9l5.8 3-5.8 3Z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>',
}

NAV = [
    ("inicio", "index.html", "Início"),
    ("escola", "a-escola.html", "A escola"),
    ("turmas", "turmas.html", "Turmas e períodos"),
    ("extras", "aulas-extras.html", "Aulas extras"),
    ("alimentacao", "alimentacao.html", "Alimentação"),
    ("contato", "contato.html", "Contato"),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">')

SCHEMA = {
    "@context": "https://schema.org",
    "@type": ["Preschool", "ChildCare"],
    "name": ESCOLA["nome"],
    "description": "Berçário e educação infantil para crianças de 4 meses a 6 anos em Santo André, desde 1992.",
    "url": ESCOLA["url"],
    "telephone": "+55-11-2677-8022",
    "email": ESCOLA["email"],
    "foundingDate": "1992",
    "image": ESCOLA["url"] + "img/fotos/fachada.webp",
    "logo": ESCOLA["url"] + "img/marcas/logo-redonda.webp",
    "address": {"@type": "PostalAddress", "streetAddress": ESCOLA["rua"], "addressLocality": "Santo André",
                "addressRegion": "SP", "postalCode": "09241-000", "addressCountry": "BR"},
    "geo": {"@type": "GeoCoordinates", "latitude": -23.632686, "longitude": -46.525478},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "06:30", "closes": "18:45"}],
    "sameAs": [ESCOLA["instagram"], ESCOLA["facebook"], ESCOLA["youtube"]],
}

def header(active):
    links = "\n".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a></li>'
        for key, href, label in NAV)
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<div class="topbar">
  <div class="wrap">
    <div class="topbar__info">
      <a href="{ESCOLA["fone_link"]}">{ICON["tel"]} {ESCOLA["fone"]}</a>
      <a class="topbar__mail" href="mailto:{ESCOLA["email"]}">{ICON["mail"]} {ESCOLA["email"]}</a>
    </div>
    <div class="topbar__social">
      <span>Seg a sex, 06h30 às 18h45</span>
      <a href="{ESCOLA["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram">{ICON["ig"]}</a>
      <a href="{ESCOLA["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook">{ICON["fb"]}</a>
      <a href="{ESCOLA["youtube"]}" target="_blank" rel="noopener" aria-label="YouTube">{ICON["yt"]}</a>
    </div>
  </div>
</div>
<header class="header" id="topo">
  <div class="wrap">
    <a class="header__logo" href="index.html" aria-label="Escola Cantinho do Mel, página inicial">
      <img src="img/marcas/logo.webp" alt="Cantinho do Mel, Educação Infantil e Berçário" width="900" height="300">
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu"><span class="bars"><i></i><i></i><i></i></span>Menu</button>
    <nav class="nav" id="menu" aria-label="Principal">
      <ul class="nav__links">
{links}
      </ul>
      <a class="btn btn--zap" href="{zap()}" target="_blank" rel="noopener" data-zap>{ICON["zap"]} Agendar visita</a>
    </nav>
  </div>
</header>'''

def footer():
    def word(w):
        return '<span class="mark__word">' + "".join(f"<i>{c}</i>" for c in w) + "</span>"
    mark = word("CANTINHO") + word("DO") + word("MEL")
    nav = "\n".join(f'<li><a href="{h}">{l}</a></li>' for _, h, l in NAV)
    return f'''<footer class="footer">
  <div class="wrap">
    <a href="index.html" class="mark" aria-label="Cantinho do Mel">{mark}</a>
    <div class="footer__grid">
      <div class="footer__col--wide footer__col">
        <img class="footer__logo" src="img/marcas/logo-redonda.webp" alt="" width="900" height="900" loading="lazy">
        <p>Berçário e educação infantil para crianças de 4 meses a 6 anos, desde 1992.</p>
        <div class="footer__social">
          <a href="{ESCOLA["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram">{ICON["ig"]}</a>
          <a href="{ESCOLA["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook">{ICON["fb"]}</a>
          <a href="{ESCOLA["youtube"]}" target="_blank" rel="noopener" aria-label="YouTube">{ICON["yt"]}</a>
        </div>
      </div>
      <div class="footer__col">
        <h2>Páginas</h2>
        <ul>{nav}</ul>
      </div>
      <div class="footer__col">
        <h2>Turmas</h2>
        <ul>
          <li><a href="turmas.html#bercario">Berçário</a></li>
          <li><a href="turmas.html#infantil">Nível 1 ao 4</a></li>
          <li><a href="turmas.html#periodos">Períodos</a></li>
          <li><a href="aulas-extras.html">Aulas extras</a></li>
        </ul>
      </div>
      <div class="footer__col--wide footer__col">
        <h2>Visite a gente</h2>
        <p><a href="{ESCOLA["maps"]}" target="_blank" rel="noopener">{ESCOLA["rua"]}<br>{ESCOLA["bairro"]}, {ESCOLA["cidade"]}<br>CEP {ESCOLA["cep"]}</a></p>
        <p>{ESCOLA["horario"]}</p>
        <p><a href="{ESCOLA["fone_link"]}">{ESCOLA["fone"]}</a> · <a href="{zap()}" target="_blank" rel="noopener">WhatsApp {ESCOLA["zap"]}</a></p>
        <p><a href="mailto:{ESCOLA["email"]}">{ESCOLA["email"]}</a></p>
      </div>
    </div>
    <div class="footer__end">
      <span>© <span data-year>2026</span> Escola Cantinho do Mel. Todos os direitos reservados.</span>
      <a class="btn btn--honey" href="#topo">{ICON["up"]} Voltar ao topo</a>
    </div>
  </div>
</footer>
<a class="zap-float" href="{zap()}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp" data-zap>{ICON["zap"]}</a>'''

# ---------- componentes reutilizados ----------
def planner(heading_level=2):
    turmas = [("Berçário", "4 meses a 2 anos"), ("Nível 1", "2 a 3 anos"), ("Nível 2", "3 a 4 anos"),
              ("Nível 3", "4 a 5 anos"), ("Nível 4", "5 a 6 anos")]
    cells = "".join(f'<div class="comb__cell" data-turma="{i}"><b>{n}</b><span>{a}</span></div>' for i, (n, a) in enumerate(turmas))
    h = f"h{heading_level}"
    return f'''<section class="section" id="monte-o-dia" aria-labelledby="planner-title">
  <div class="wrap">
    <div class="planner" data-planner>
      <div class="planner__grid">
        <div data-reveal>
          <{h} id="planner-title">Monte o dia do seu filho</{h}>
          <p class="planner__intro">Conte a idade e escolha o período. A gente mostra a turma e como fica a rotina de chegada e saída.</p>
          <label class="planner__q" for="age">Quantos anos tem seu filho?</label>
          <div class="planner__age"><output for="age" data-age-out>1 ano e 2 meses</output></div>
          <input class="range" type="range" id="age" min="4" max="72" step="1" value="14" data-age aria-describedby="age-ends">
          <div class="range__ends" id="age-ends"><span>4 meses</span><span>6 anos</span></div>
          <fieldset style="border:0;padding:0;margin:0">
            <legend class="planner__q">Qual período?</legend>
            <div class="chips">
              <label class="chip"><input type="radio" name="periodo" value="5" data-label="Meio período"><span>Meio período<small>5 horas</small></span></label>
              <label class="chip"><input type="radio" name="periodo" value="8" data-label="Semi integral" checked><span>Semi integral<small>8 horas</small></span></label>
              <label class="chip"><input type="radio" name="periodo" value="12" data-label="Integral"><span>Integral<small>12 horas</small></span></label>
            </div>
          </fieldset>
        </div>
        <div data-reveal>
          <div class="comb" aria-hidden="true">{cells}</div>
          <p class="day__say" aria-live="polite" data-say>Turma <b>Nível 1</b>, no semi integral.</p>
          <div class="day">
            <label class="planner__q" for="entry" style="margin-top:20px">Que horas ele chega?</label>
            <div class="day__bar"><div class="day__fill" data-fill></div></div>
            <div class="day__ticks"><span>06h30</span><span>09h</span><span>12h</span><span>15h</span><span>18h45</span></div>
            <input class="range" type="range" id="entry" min="390" max="645" step="15" value="420" data-entry>
            <p class="day__say" data-times>Chega às <b>07h00</b> e sai às <b>15h00</b>.</p>
            <p class="day__note">A escola abre às 06h30 e fecha às 18h45. Os horários de cada período são combinados na matrícula.</p>
          </div>
          <div class="planner__cta">
            <a class="btn btn--honey" href="contato.html#agendar" data-planner-go>Agendar visita com essas escolhas {ICON["arrow"]}</a>
            <a class="link" href="turmas.html">Conhecer as turmas</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

def turma_options(selected=""):
    opts = ["Berçário (4 meses a 2 anos)", "Nível 1 (2 a 3 anos)", "Nível 2 (3 a 4 anos)", "Nível 3 (4 a 5 anos)", "Nível 4 (5 a 6 anos)"]
    return '<option value="">Escolha a turma</option>' + "".join(f'<option>{o}</option>' for o in opts)

def periodo_options():
    opts = ["Meio período (5 horas)", "Semi integral (8 horas)", "Integral (12 horas)", "Ainda não sei"]
    return '<option value="">Escolha o período</option>' + "".join(f'<option>{o}</option>' for o in opts)

def coupon():
    return f'''<section class="section" id="agendar" aria-labelledby="coupon-title">
  <div class="wrap">
    <div class="coupon" data-reveal>
      <div class="coupon__left">
        <h2 id="coupon-title">Agende sua visita</h2>
        <p>Preencha em menos de um minuto. A mensagem chega pronta no WhatsApp da escola e você só aperta enviar.</p>
      </div>
      <form class="coupon__form" data-zap-form novalidate>
        <div class="fields-2">
          <div class="field"><label for="c-resp">Seu nome</label><input id="c-resp" name="responsavel" autocomplete="name" required placeholder="Como podemos te chamar?"></div>
          <div class="field"><label for="c-crianca">Nome da criança</label><input id="c-crianca" name="crianca" required placeholder="Nome do pequeno"></div>
        </div>
        <div class="fields-2">
          <div class="field"><label for="c-turma">Turma de interesse</label><select id="c-turma" name="turma" required>{turma_options()}</select></div>
          <div class="field"><label for="c-periodo">Período</label><select id="c-periodo" name="periodo">{periodo_options()}</select></div>
        </div>
        <p class="form-error" role="alert" data-error></p>
        <button class="btn btn--ink btn--full" type="submit">{ICON["zap"]} Enviar pelo WhatsApp</button>
      </form>
    </div>
  </div>
</section>'''

def visit():
    q = urllib.parse.quote("Escola Cantinho do Mel, Rua Colúmbia, 438, Parque das Nações, Santo André - SP")
    return f'''<section class="section" id="como-chegar" aria-labelledby="visit-title">
  <div class="wrap visit">
    <div class="visit__info" data-reveal>
      <h2 id="visit-title">Como chegar</h2>
      <p class="lead">Na Rua Colúmbia, no Parque das Nações. Procure o muro pintado com sol, grama e a abelha no telhado.</p>
      <dl class="facts">
        <div><dt>{ICON["pin"]}</dt><dd><b>{ESCOLA["rua"]}</b>{ESCOLA["bairro"]}, {ESCOLA["cidade"]}, CEP {ESCOLA["cep"]}</dd></div>
        <div><dt>{ICON["clock"]}</dt><dd><b>06h30 às 18h45</b>Segunda a sexta-feira</dd></div>
        <div><dt>{ICON["tel"]}</dt><dd><b><a href="{ESCOLA["fone_link"]}">{ESCOLA["fone"]}</a></b>Telefone fixo</dd></div>
        <div><dt>{ICON["zap"]}</dt><dd><b><a href="{zap()}" target="_blank" rel="noopener" data-zap>{ESCOLA["zap"]}</a></b>WhatsApp</dd></div>
      </dl>
    </div>
    <div class="map" data-reveal>
      <iframe title="Mapa da Escola Cantinho do Mel" src="https://maps.google.com/maps?q={q}&z=17&hl=pt-BR&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      <a class="btn btn--ink map__open" href="{ESCOLA["maps"]}" target="_blank" rel="noopener">{ICON["pin"]} Abrir no Google Maps</a>
    </div>
  </div>
</section>'''

COMPONENTS = {"planner": planner, "coupon": coupon, "visit": visit}

def render(page_path):
    raw = open(page_path, encoding="utf-8").read()
    m = re.match(r"\s*<!--\s*(\{.*?\})\s*-->\s*", raw, re.S)
    meta = json.loads(m.group(1))
    body = raw[m.end():]
    body = re.sub(r"\{\{(\w+)\}\}", lambda mm: COMPONENTS[mm.group(1)]() if mm.group(1) in COMPONENTS else
                  (zap() if mm.group(1) == "zapurl" else ICON.get(mm.group(1), mm.group(0))), body)
    title = meta["title"]
    desc = meta["desc"]
    canonical = ESCOLA["url"] + ("" if meta["file"] == "index.html" else meta["file"])
    schema = f'<script type="application/ld+json">{json.dumps(SCHEMA, ensure_ascii=False)}</script>' if meta["file"] == "index.html" else ""
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ESCOLA["url"]}img/fotos/fachada.webp">
<meta name="theme-color" content="#ffc52e">
<link rel="icon" type="image/png" sizes="32x32" href="img/icone-32.png">
<link rel="apple-touch-icon" href="img/icone-180.png">
{FONTS}
<link rel="stylesheet" href="styles.css">
<script>document.documentElement.classList.add('js')</script>
{schema}
</head>
<body>
{header(meta["nav"])}
<main id="conteudo">
{body.strip()}
</main>
{footer()}
<script src="main.js" defer></script>
</body>
</html>
'''
    open(os.path.join(SITE, meta["file"]), "w", encoding="utf-8").write(html)
    print("ok", meta["file"])

if __name__ == "__main__":
    pages = os.path.join(HERE, "pages")
    for f in sorted(os.listdir(pages)):
        if f.endswith(".html"):
            render(os.path.join(pages, f))
