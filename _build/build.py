# Monta as páginas do site: cada arquivo em _build/pages/ recebe o mesmo
# <head>, cabeçalho, rodapé, desenhos e componentes. Rode: python _build/build.py
import json, math, os, re, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)

ESCOLA = {
    "nome": "Escola Cantinho do Mel",
    "fone": "(11) 2677-8022",
    "fone_link": "tel:+551126778022",
    "zap": "(11) 94871-4027",
    "zap_num": "5511948714027",
    "email": "contato@escolacantinhodomel.com.br",
    "rua": "Rua Colúmbia, 458",
    "bairro": "Parque das Nações",
    "cidade": "Santo André, SP",
    "cep": "09241-000",
    "maps": "https://www.google.com/maps?ll=-23.632686,-46.525478&z=18&t=m&hl=pt-BR&gl=BR&mapclient=embed&cid=11133067005482875823",
    "instagram": "https://www.instagram.com/cantinhodomel/",
    "facebook": "https://www.facebook.com/escolacantinhodomel/",
    "youtube": "https://www.youtube.com/channel/UCcw24CynVY4-346pbGE55BQ",
    "url": "https://escolacantinhodomel.com.br/",
}

def zap(msg="Olá! Gostaria de agendar uma visita à Escola Cantinho do Mel."):
    return f"https://wa.me/{ESCOLA['zap_num']}?text=" + urllib.parse.quote(msg)

INK = "#1d2a4d"
COLORS = {"sun": "#ffd43b", "sky": "#e3f5ff", "skyfull": "#45bdf5", "grass": "#ebf8e3", "green": "#5cbf3b",
          "pink": "#ffe6ee", "white": "#ffffff", "ink": INK}

# ---------- ícones (traço) ----------
def _i(body, fill=False):
    if fill:
        return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{body}</svg>'
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'

ICON = {
    "zap": _i('<path d="M12.04 2a9.9 9.9 0 0 0-8.5 15l-1.4 5.1 5.24-1.37A9.9 9.9 0 1 0 12.04 2Zm0 18.1a8.2 8.2 0 0 1-4.18-1.15l-.3-.18-3.1.82.83-3.03-.2-.31a8.2 8.2 0 1 1 6.95 3.850Zm4.5-6.14c-.25-.12-1.46-.72-1.69-.8-.23-.08-.39-.12-.55.12-.16.25-.63.8-.78.97-.14.16-.29.18-.53.06-.25-.12-1.040-.38-1.980-1.22-.73-.65-1.23-1.46-1.37-1.7-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.15.16-.25.25-.41.08-.17.04-.31-.02-.43-.06-.13-.55-1.33-.76-1.82-.2-.48-.4-.41-.55-.42h-.47a.9.9 0 0 0-.65.31c-.23.25-.86.84-.86 2.04 0 1.2.88 2.37 1 2.53.12.17 1.73 2.64 4.2 3.7.58.26 1.04.41 1.4.52.59.19 1.12.16 1.54.1.47-.07 1.46-.6 1.66-1.17.2-.58.2-1.07.15-1.17-.06-.1-.22-.17-.47-.29Z"/>', True),
    "tel": _i('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>'),
    "mail": _i('<rect x="2" y="4" width="20" height="16" rx="3"/><path d="m22 7-10 6L2 7"/>'),
    "pin": _i('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>'),
    "clock": _i('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
    "ig": _i('<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>'),
    "fb": _i('<path d="M14 8.5V6.8c0-.8.5-1 1-1h2.5V2H14c-3.4 0-4.2 2.5-4.2 4.2v2.3H7.5V12h2.3v10H14V12h3l.4-3.5H14Z"/>', True),
    "yt": _i('<path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8ZM9.8 15V9l5.8 3-5.8 3Z"/>', True),
    "arrow": _i('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    "up": _i('<path d="M12 19V5M6 11l6-6 6 6"/>'),
    "close": _i('<path d="M6 6l12 12M18 6 6 18"/>'),
    "left": _i('<path d="m15 18-6-6 6-6"/>'),
    "right": _i('<path d="m9 18 6-6-6-6"/>'),
    "heart": _i('<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/>'),
    "shield": _i('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>'),
    "star": _i('<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1Z"/>'),
    "book": _i('<path d="M2 4h6a4 4 0 0 1 4 4v13a3 3 0 0 0-3-3H2Z"/><path d="M22 4h-6a4 4 0 0 0-4 4v13a3 3 0 0 1 3-3h7Z"/>'),
    "users": _i('<circle cx="9" cy="7" r="4"/><path d="M2 21v-2a4 4 0 0 1 4-4h6a4 4 0 0 1 4 4v2"/><path d="M16 3.1a4 4 0 0 1 0 7.8M22 21v-2a4 4 0 0 0-3-3.9"/>'),
    "baby": _i('<circle cx="12" cy="12" r="10"/><path d="M9 10h.01M15 10h.01M9.5 15a3.5 3.5 0 0 0 5 0"/><path d="M12 2c-1.5 1.5-1.5 3 0 4"/>'),
    "sun": _i('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'),
    "cal": _i('<rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4M8 2v4M3 10h18"/>'),
    "ball": _i('<circle cx="12" cy="12" r="10"/><path d="m12 7 4 3-1.5 5h-5L8 10Z"/><path d="M12 2v5M16 10l5-1M14.5 15l3 4.5M9.5 15l-3 4.5M8 10 3 9"/>'),
    "music": _i('<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>'),
    "chat": _i('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2Z"/><path d="M8 9h8M8 13h5"/>'),
    "belt": _i('<path d="M2 9h20v4H2Z"/><path d="m10 13-3 8M14 13l3 8"/><rect x="9.5" y="7.5" width="5" height="7" rx="1"/>'),
    "sparkle": _i('<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9Z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8Z"/>'),
    "apple": _i('<path d="M12 7c-1.5-1-3-1.4-4.5-1C4.6 6.7 3 9.4 3 12.6 3 17 6 22 9 22c1 0 1.8-.6 3-.6s2 .6 3 .6c3 0 6-5 6-9.4 0-3.2-1.6-5.9-4.5-6.6-1.5-.4-3 0-4.5 1Z"/><path d="M12 7c0-2 1-4 3-5"/>'),
    "home": _i('<path d="M3 10.5 12 3l9 7.5V21H3Z"/><path d="M9 21v-7h6v7"/>'),
    "pot": _i('<path d="M4 10h16v5a6 6 0 0 1-6 6h-4a6 6 0 0 1-6-6Z"/><path d="M2 10h20M8 6c0-1 1-2 1-3M12 6c0-1 1-2 1-3M16 6c0-1 1-2 1-3"/>'),
    "first": _i('<rect x="3" y="7" width="18" height="14" rx="3"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M12 11v6M9 14h6"/>'),
    "puzzle": _i('<path d="M19.4 15a1 1 0 0 0 .6-.9V10a1 1 0 0 0-1-1h-3.1a2 2 0 1 0-3.8 0H9a1 1 0 0 0-1 1v3.1a2 2 0 1 0 0 3.8V20a1 1 0 0 0 1 1h4.1a2 2 0 1 1 3.8 0H19a1 1 0 0 0 1-1v-4.1a2 2 0 0 1-.6-.9Z"/>'),
    "camera": _i('<path d="M3 8a2 2 0 0 1 2-2h2l2-3h6l2 3h2a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><circle cx="12" cy="13" r="4"/>'),
}

# ---------- desenhos ----------
CLOUD = '<svg viewBox="0 0 200 110" fill="currentColor" aria-hidden="true"><circle cx="62" cy="66" r="34"/><circle cx="104" cy="48" r="42"/><circle cx="148" cy="68" r="30"/><rect x="30" y="66" width="150" height="38" rx="19"/></svg>'

def _sun():
    rays = "".join(f'<rect x="92" y="2" width="16" height="34" rx="8" transform="rotate({i*30} 100 100)"/>' for i in range(12))
    return ('<svg class="sun" viewBox="0 0 200 200" aria-hidden="true">'
            f'<g class="sun__rays" fill="#ffb703" stroke="{INK}" stroke-width="4">{rays}</g>'
            f'<circle cx="100" cy="100" r="58" fill="#ffd43b" stroke="{INK}" stroke-width="5"/>'
            f'<ellipse cx="80" cy="92" rx="6" ry="9" fill="{INK}"/><ellipse cx="120" cy="92" rx="6" ry="9" fill="{INK}"/>'
            '<circle cx="68" cy="112" r="9" fill="#ff8fb0"/><circle cx="132" cy="112" r="9" fill="#ff8fb0"/>'
            f'<path d="M78 116c10 14 34 14 44 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></svg>')
SUN = _sun()

BEE = (f'<svg viewBox="0 0 66 54" aria-hidden="true"><g stroke="{INK}" stroke-width="3" stroke-linejoin="round">'
       '<ellipse cx="26" cy="14" rx="10" ry="13" fill="#e8f7ff" transform="rotate(-20 26 14)"/>'
       '<ellipse cx="40" cy="13" rx="9" ry="12" fill="#e8f7ff" transform="rotate(18 40 13)"/>'
       '<path d="M10 33 2 35l8 4" fill="#ffd43b"/>'
       '<ellipse cx="33" cy="34" rx="22" ry="16" fill="#ffd43b"/></g>'
       f'<path d="M27 19v30M38 19v30" stroke="{INK}" stroke-width="5"/>'
       f'<ellipse cx="33" cy="34" rx="22" ry="16" fill="none" stroke="{INK}" stroke-width="3"/>'
       f'<circle cx="47" cy="30" r="3" fill="{INK}"/><path d="M45 38c2 2 5 2 7 0" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>'
       '<circle cx="51" cy="36" r="2.5" fill="#ff8fb0"/></svg>')

def flower(color, d):
    petals = "".join(f'<circle cx="{20+9*math.cos(math.radians(a)):.1f}" cy="{20+9*math.sin(math.radians(a)):.1f}" r="7.5"/>' for a in range(-90, 270, 72))
    return (f'<svg class="flower" style="--d:{d}s" viewBox="0 0 40 64" aria-hidden="true">'
            f'<path d="M20 64V28" stroke="#3f9d27" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M20 48c-8-1-12-6-12-10 6 0 11 3 12 10Z" fill="#8fd96a" stroke="{INK}" stroke-width="2"/>'
            f'<g fill="{color}" stroke="{INK}" stroke-width="2.5">{petals}</g>'
            f'<circle cx="20" cy="20" r="6.5" fill="#ffd43b" stroke="{INK}" stroke-width="2.5"/></svg>')

def hills(next_color="white"):
    cols = ["#ff5c8d", "#ffffff", "#8e5be8", "#ff7a1a", "#f0483e", "#ffd43b", "#45bdf5", "#ff5c8d", "#ffffff", "#ff7a1a", "#8e5be8", "#f0483e"]
    fl = "".join(flower(c, round(i * 0.37 % 2, 2)) for i, c in enumerate(cols))
    nc = COLORS[next_color]
    return (f'<div class="hills" aria-hidden="true">'
            f'<svg class="hills__shape" viewBox="0 0 1440 160" preserveAspectRatio="none">'
            f'<path d="M0 64C220 8 430 6 700 56S1180 118 1440 34V160H0Z" fill="#8fd96a" stroke="{INK}" stroke-width="3" vector-effect="non-scaling-stroke"/>'
            f'<path d="M0 104C300 44 610 140 920 88S1290 58 1440 96V160H0Z" fill="#5cbf3b" stroke="{INK}" stroke-width="3" vector-effect="non-scaling-stroke"/>'
            f'<path d="M0 146C380 118 1060 172 1440 134V160H0Z" fill="{nc}"/></svg>'
            f'<div class="flowers">{fl}</div></div>')

def clouds():
    spec = [("150px", "8%", "62s", "-10s"), ("220px", "30%", "84s", "-50s"), ("120px", "56%", "58s", "-30s"), ("180px", "16%", "96s", "-72s"), ("100px", "70%", "70s", "-5s")]
    return '<div class="sky__clouds" aria-hidden="true">' + "".join(
        f'<div class="cloud" style="--w:{w};top:{t};--t:{dur};--d:{d}">{CLOUD}</div>' for w, t, dur, d in spec) + "</div>"

def flybees():
    return (f'<div class="flybee" style="left:44%;top:7%;--t:17s">{BEE}</div>'
            f'<div class="flybee" style="left:6%;top:auto;bottom:16%;--t:21s;--d:-6s;width:42px">{BEE}</div>')

def _drip_path():
    # gotas de mel de larguras e comprimentos variados, como no toldo da fachada
    pts = [(1400, 70, 30), (1290, 56, 58), (1180, 76, 22), (1060, 60, 70), (950, 80, 34), (830, 58, 50), (715, 74, 26), (600, 62, 64), (480, 84, 30), (360, 58, 54), (245, 76, 24), (130, 62, 62), (30, 70, 28)]
    base = 30
    d = f"M-20 -20H1460V{base}"
    for c, w, L in pts:
        h = w / 2
        d += f"H{c+h}C{c+h*0.6} {base+4} {c+h*0.55} {base+L} {c+h*0.5} {base+L+h*0.4}A{h*0.5} {h*0.5} 0 0 1 {c-h*0.5} {base+L+h*0.4}C{c-h*0.55} {base+L} {c-h*0.6} {base+4} {c-h} {base}"
    d += "H-20Z"
    return d
DRIP_D = _drip_path()

def drip(above="sun", below="white"):
    return (f'<div style="background:{COLORS[below]}" aria-hidden="true"><svg class="drip" viewBox="0 0 1440 120" preserveAspectRatio="none" style="color:{COLORS[above]}">'
            f'<path d="{DRIP_D}" fill="currentColor" stroke="{INK}" stroke-width="3" vector-effect="non-scaling-stroke"/></svg></div>')

def wave(above="white", below="sky"):
    return (f'<div style="background:{COLORS[above]}" aria-hidden="true"><svg class="wave" viewBox="0 0 1440 70" preserveAspectRatio="none">'
            f'<path d="M0 36C240 0 480 70 720 36S1200 2 1440 36V70H0Z" fill="{COLORS[below]}"/></svg></div>')

SQUIGGLE = '<svg class="squiggle" viewBox="0 0 130 16" aria-hidden="true"><path d="M3 9c10-8 20 8 31 0s20-8 31 0 20 8 31 0 20-8 31 0" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/></svg>'

NAV = [
    ("inicio", "index.html", "Início"),
    ("escola", "a-escola.html", "A escola"),
    ("turmas", "turmas.html", "Turmas"),
    ("extras", "aulas-extras.html", "Aulas extras"),
    ("alimentacao", "alimentacao.html", "Alimentação"),
    ("contato", "contato.html", "Contato"),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">')

SCHEMA = {
    "@context": "https://schema.org", "@type": ["Preschool", "ChildCare"], "name": ESCOLA["nome"],
    "description": "Berçário e educação infantil para crianças de 4 meses a 6 anos em Santo André, desde 1992.",
    "url": ESCOLA["url"], "telephone": "+55-11-2677-8022", "email": ESCOLA["email"], "foundingDate": "1992",
    "image": ESCOLA["url"] + "img/fotos/fachada.webp", "logo": ESCOLA["url"] + "img/marcas/logo-redonda.webp",
    "address": {"@type": "PostalAddress", "streetAddress": ESCOLA["rua"], "addressLocality": "Santo André",
                "addressRegion": "SP", "postalCode": ESCOLA["cep"], "addressCountry": "BR"},
    "geo": {"@type": "GeoCoordinates", "latitude": -23.632686, "longitude": -46.525478},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "06:30", "closes": "18:45"}],
    "sameAs": [ESCOLA["instagram"], ESCOLA["facebook"], ESCOLA["youtube"]],
}

SOCIAL = (("instagram", "Instagram", "ig"), ("facebook", "Facebook", "fb"), ("youtube", "YouTube", "yt"))

def header(active):
    links = "\n".join(f'<li><a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{l}</a></li>' for k, h, l in NAV)
    soc = "".join(f'<a href="{ESCOLA[k]}" target="_blank" rel="noopener" aria-label="{n}">{ICON[i]}</a>' for k, n, i in SOCIAL)
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<div class="topbar"><div class="wrap">
  <div class="topbar__l"><a href="{ESCOLA["fone_link"]}">{ICON["tel"]} {ESCOLA["fone"]}</a><a class="topbar__mail" href="mailto:{ESCOLA["email"]}">{ICON["mail"]} {ESCOLA["email"]}</a></div>
  <div class="topbar__r"><span class="topbar__hours">Seg a sex, 6:30 às 18:45</span><div class="topbar__soc">{soc}</div></div>
</div></div>
<header class="header" id="topo"><div class="wrap">
  <a class="logo" href="index.html" aria-label="Escola Cantinho do Mel, página inicial"><img src="img/marcas/logo.webp" alt="Cantinho do Mel, Educação Infantil e Berçário" width="900" height="300"></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu"><span class="bars"><i></i><i></i><i></i></span>Menu</button>
  <nav class="nav" id="menu" aria-label="Principal">
    <ul class="nav__links">
{links}
    </ul>
    <a class="btn btn--zap btn--sm" href="{zap()}" target="_blank" rel="noopener">{ICON["zap"]} Agendar visita</a>
  </nav>
</div></header>'''

def footer():
    nav = "".join(f'<li><a href="{h}">{l}</a></li>' for _, h, l in NAV)
    soc = "".join(f'<a href="{ESCOLA[k]}" target="_blank" rel="noopener" aria-label="{n}">{ICON[i]}</a>' for k, n, i in SOCIAL)
    return f'''<footer class="footer">
  <svg class="footer__wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40C200 6 420 6 640 34S1100 70 1440 22V70H0Z" fill="currentColor"/></svg>
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <img class="footer__logo" src="img/marcas/logo-redonda.webp" alt="Escola Cantinho do Mel" width="900" height="900" loading="lazy">
        <p>Berçário e educação infantil para crianças de 4 meses a 6 anos. Desde 1992 no Parque das Nações, em Santo André.</p>
        <div class="footer__soc">{soc}</div>
      </div>
      <div><h2>Páginas</h2><ul>{nav}</ul></div>
      <div><h2>Turmas</h2><ul>
        <li><a href="turmas.html#bercario">Berçário</a></li><li><a href="turmas.html#infantil">Nível 1 ao 4</a></li>
        <li><a href="turmas.html#periodos">Períodos</a></li><li><a href="turmas.html#monte-o-dia">Monte o dia</a></li></ul></div>
      <div><h2>Visite a gente</h2>
        <p><a href="{ESCOLA["maps"]}" target="_blank" rel="noopener">{ESCOLA["rua"]}<br>{ESCOLA["bairro"]}, {ESCOLA["cidade"]}<br>CEP {ESCOLA["cep"]}</a></p>
        <p>Segunda a sexta, das 6:30 às 18:45</p>
        <p><a href="{ESCOLA["fone_link"]}">{ESCOLA["fone"]}</a> · <a href="{zap()}" target="_blank" rel="noopener">WhatsApp {ESCOLA["zap"]}</a></p>
        <p><a href="mailto:{ESCOLA["email"]}">{ESCOLA["email"]}</a></p></div>
    </div>
    <div class="footer__end"><span>© <span data-year>2026</span> Escola Cantinho do Mel. Todos os direitos reservados.</span><a class="btn btn--sun btn--sm" href="#topo">{ICON["up"]} Voltar ao topo</a></div>
  </div>
</footer>
<a class="zap-float" href="{zap()}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{ICON["zap"]}</a>'''

# ---------- componentes ----------
TURMAS = [("Berçário", "4 meses a 2 anos"), ("Nível 1", "2 a 3 anos"), ("Nível 2", "3 a 4 anos"), ("Nível 3", "4 a 5 anos"), ("Nível 4", "5 a 6 anos")]

def planner():
    curto = ["4m a 2 anos", "2 a 3 anos", "3 a 4 anos", "4 a 5 anos", "5 a 6 anos"]
    meses = [12, 30, 42, 54, 66]
    bubbles = "".join(f'<button type="button" class="bubble" data-turma="{i}" data-months="{meses[i]}" aria-pressed="false" aria-label="{n}, {a}"><b>{n}</b><span>{curto[i]}</span></button>' for i, (n, a) in enumerate(TURMAS))
    return f'''{wave("white", "sky")}
<section class="section bg-sky" id="monte-o-dia" aria-labelledby="planner-title">
  <div class="wrap">
    <div class="head" data-reveal><span class="tag tag--white">{ICON["puzzle"]} Experimente</span><h2 id="planner-title">Monte o dia do seu filho</h2>{SQUIGGLE}<p>Arraste até a idade, escolha o período e veja a turma e o horário do seu filho.</p></div>
    <div class="planner" data-planner data-reveal>
      <div class="planner__grid">
        <div>
          <label class="planner__q" for="age" style="margin-top:0">Quantos anos tem seu filho?</label>
          <div class="planner__age"><output for="age" data-age-out>1 ano e 2 meses</output></div>
          <input class="range" type="range" id="age" min="4" max="72" step="1" value="14" data-age>
          <div class="range__ends"><span>4 meses</span><span>6 anos</span></div>
          <fieldset><legend class="planner__q">Qual período?</legend>
            <div class="opts">
              <label class="opt"><input type="radio" name="periodo" value="manha" data-label="meio período da manhã" data-from="420" data-to="720" checked><span>Meio período manhã<small>7:00 às 12:00</small></span></label>
              <label class="opt"><input type="radio" name="periodo" value="tarde" data-label="meio período da tarde" data-from="780" data-to="1080"><span>Meio período tarde<small>13:00 às 18:00</small></span></label>
              <label class="opt"><input type="radio" name="periodo" value="semi" data-label="semi integral"><span>Semi integral<small>8 horas · horário flexível</small></span></label>
              <label class="opt"><input type="radio" name="periodo" value="integral" data-label="integral" data-from="390" data-to="1125"><span>Integral<small>6:30 às 18:45</small></span></label>
            </div>
          </fieldset>
          <div class="semi-pick" data-semi hidden>
            <label class="planner__q" for="entry">Que horas ele chega?</label>
            <input class="range" type="range" id="entry" min="390" max="645" step="15" value="420" data-entry>
            <div class="range__ends"><span>6:30</span><span>10:45</span></div>
          </div>
        </div>
        <div>
          <p class="bubbles__label">Ou toque na turma:</p>
          <div class="bubbles" role="group" aria-label="Escolher turma">{bubbles}</div>
          <div class="planner__out">
            <p class="say" aria-live="polite" data-say>Turma <b>Berçário</b>, no meio período da manhã.</p>
            <div class="day__bar" style="margin-top:16px"><div class="day__fill" data-fill></div></div>
            <div class="day__ticks"><span>6:30</span><span>9:00</span><span>12:00</span><span>15:00</span><span>18:45</span></div>
            <p class="say" style="margin-top:12px;font-size:1.15rem" data-times>Das <b>7:00</b> às <b>12:00</b>.</p>
            <p class="day__note" data-note>Horário fixo, igual para todas as crianças do período.</p>
          </div>
          <div class="planner__cta">
            <a class="btn btn--zap" href="contato.html#agendar" data-planner-go>{ICON["cal"]} Agendar visita com essas escolhas</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
{wave("sky", "white")}'''

def visit(above="white"):
    opts_t = '<option value="">Escolha a turma</option>' + "".join(f'<option>{n} ({a})</option>' for n, a in TURMAS)
    opts_p = '<option value="">Escolha o período</option><option>Meio período manhã (7:00 às 12:00)</option><option>Meio período tarde (13:00 às 18:00)</option><option>Semi integral (8 horas)</option><option>Integral (6:30 às 18:45)</option><option>Ainda não sei</option>'
    return f'''{wave(above, "green")}
<section class="section visit" id="agendar" aria-labelledby="visit-title">
  <div class="wrap visit__grid">
    <div class="visit__text" data-reveal>
      <span class="tag">{ICON["cal"]} Matrículas abertas</span>
      <h2 id="visit-title">Venha conhecer o Cantinho!</h2>
      <p class="lead">Preencha rapidinho e a mensagem chega pronta no WhatsApp da escola. É só apertar enviar.</p>
      <ol class="visit__steps"><li>Conte quem é você e a criança</li><li>Escolha a turma e o período</li><li>Combine o dia da visita</li></ol>
    </div>
    <form class="form" data-zap-form novalidate data-reveal>
      <div class="row2">
        <div class="field"><label for="c-resp">Seu nome</label><input id="c-resp" name="responsavel" autocomplete="name" required placeholder="Como podemos te chamar?"></div>
        <div class="field"><label for="c-tel">Seu telefone</label><input id="c-tel" name="telefone" type="tel" autocomplete="tel" inputmode="tel" placeholder="(11) 90000-0000"></div>
      </div>
      <div class="row2">
        <div class="field"><label for="c-crianca">Nome da criança</label><input id="c-crianca" name="crianca" required placeholder="Nome do pequeno"></div>
        <div class="field"><label for="c-nasc">Data de nascimento</label><input id="c-nasc" name="nascimento" type="date"></div>
      </div>
      <p class="hint" data-age-hint aria-live="polite">Pela data de nascimento, a gente sugere a turma.</p>
      <div class="row2">
        <div class="field"><label for="c-turma">Turma de interesse</label><select id="c-turma" name="turma" required>{opts_t}</select></div>
        <div class="field"><label for="c-periodo">Período</label><select id="c-periodo" name="periodo">{opts_p}</select></div>
      </div>
      <details class="more" data-more>
        <summary>Adicionar mais detalhes <small>(opcional)</small></summary>
        <div class="more__body">
          <div class="row2">
            <div class="field"><label for="c-dia">Melhor horário da visita</label><select id="c-dia" name="dia"><option value="">Tanto faz</option><option>De manhã</option><option>À tarde</option></select></div>
          </div>
          <div class="field"><label for="c-msg">Quer contar mais alguma coisa?</label><textarea id="c-msg" name="mensagem" placeholder="Dúvidas, cuidados especiais, quando pretende começar..."></textarea></div>
        </div>
      </details>
      <p class="form-error" role="alert" data-error></p>
      <button class="btn btn--zap btn--full" type="submit">{ICON["zap"]} Enviar pelo WhatsApp</button>
    </form>
  </div>
</section>
{wave("green", "white")}'''

def where():
    q = urllib.parse.quote("Escola Cantinho do Mel, Rua Colúmbia, Parque das Nações, Santo André - SP")
    return f'''<section class="section" id="como-chegar" aria-labelledby="where-title">
  <div class="wrap">
    <div class="head" data-reveal><span class="tag tag--sky">{ICON["pin"]} Parque das Nações</span><h2 id="where-title">Como chegar</h2>{SQUIGGLE}<p>Procure o muro pintado com sol, grama, flores e a abelha gigante no telhado.</p></div>
    <div class="where">
      <div class="infos" data-stagger>
        <a class="info" href="{ESCOLA["maps"]}" target="_blank" rel="noopener"><span class="info__i">{ICON["pin"]}</span><span><b>{ESCOLA["rua"]}</b><span>{ESCOLA["bairro"]}, {ESCOLA["cidade"]}, CEP {ESCOLA["cep"]}</span></span></a>
        <div class="info"><span class="info__i">{ICON["clock"]}</span><span><b>6:30 às 18:45</b><span>Segunda a sexta-feira</span></span></div>
        <a class="info" href="{ESCOLA["fone_link"]}"><span class="info__i">{ICON["tel"]}</span><span><b>{ESCOLA["fone"]}</b><span>Telefone fixo</span></span></a>
        <a class="info" href="{zap()}" target="_blank" rel="noopener"><span class="info__i">{ICON["zap"]}</span><span><b>{ESCOLA["zap"]}</b><span>WhatsApp</span></span></a>
      </div>
      <div class="map" data-reveal>
        <iframe title="Mapa da Escola Cantinho do Mel" src="https://maps.google.com/maps?q={q}&z=17&hl=pt-BR&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        <a class="btn btn--white btn--sm" href="{ESCOLA["maps"]}" target="_blank" rel="noopener">{ICON["pin"]} Abrir no Google Maps</a>
      </div>
    </div>
  </div>
</section>'''

def partners():
    items = [("positivo", "Positivo", "Sistema de ensino", 440), ("ccaa", "CCAA", "Inglês", 664), ("kidnote", "Kid Note", "Agenda digital escolar", 763), ("natividade", "N'Atividade", "Esporte e nutrição", 692)]
    lis = "".join(f'<li class="partner"><img src="img/marcas/{f}.webp" alt="{n}" width="900" height="{h}" loading="lazy"><b>{n}</b><span>{d}</span></li>' for f, n, d, h in items)
    return f'''<section class="section" id="parceiros" aria-labelledby="par-title">
  <div class="wrap">
    <div class="head" data-reveal><span class="tag tag--grass">{ICON["heart"]} Juntos com a gente</span><h2 id="par-title">Nossos parceiros</h2>{SQUIGGLE}<p>No ensino, no inglês, na comunicação com as famílias e na nutrição.</p></div>
    <ul class="partners" data-stagger>{lis}</ul>
  </div>
</section>'''

def ctaband():
    return f'''<section class="section" aria-label="Agendar visita"><div class="wrap">
  <div class="cta-band cta-band--plain" data-reveal>
    <div><h2 style="font-size:clamp(1.7rem,1.2rem + 1.6vw,2.6rem)">Que tal conhecer a escola pessoalmente?</h2><p>Agende uma visita para ver as salas, o berçário e conhecer a equipe. Respondemos pelo WhatsApp de segunda a sexta.</p></div>
    <div class="cta-band__btns"><a class="btn btn--zap" href="{zap()}" target="_blank" rel="noopener">{ICON["zap"]} Agendar pelo WhatsApp</a><a class="btn btn--white" href="contato.html#agendar">Preencher formulário {ICON["arrow"]}</a></div></div>
</div></section>'''

COMPONENTS = {"planner": planner, "visit": visit, "where": where, "partners": partners, "ctaband": ctaband,
              "clouds": clouds, "flybees": flybees, "squiggle": lambda: SQUIGGLE, "sun": lambda: SUN,
              "zapurl": zap}

def token(m):
    name = m.group(1)
    args = m.group(2).split(":")[1:] if m.group(2) else []
    if name == "hills": return hills(*args)
    if name == "drip": return drip(*args)
    if name == "wave": return wave(*args)
    if name in COMPONENTS: return COMPONENTS[name](*args)
    if name in ICON: return ICON[name]
    raise KeyError(name)

def render(page_path):
    raw = open(page_path, encoding="utf-8").read()
    m = re.match(r"\s*<!--\s*(\{.*?\})\s*-->\s*", raw, re.S)
    meta = json.loads(m.group(1))
    body = re.sub(r"\{\{(\w+)((?::\w+)*)\}\}", token, raw[m.end():])
    title, desc = meta["title"], meta["desc"]
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
<meta name="theme-color" content="#45bdf5">
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
<div class="lightbox" data-lightbox role="dialog" aria-modal="true" aria-label="Foto ampliada">
  <button class="lb-close" type="button" aria-label="Fechar">{ICON["close"]}</button>
  <button class="lb-prev" type="button" aria-label="Foto anterior">{ICON["left"]}</button>
  <button class="lb-next" type="button" aria-label="Próxima foto">{ICON["right"]}</button>
  <figure><img alt=""><figcaption></figcaption></figure>
</div>
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
