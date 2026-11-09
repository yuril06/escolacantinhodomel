# Gera as páginas do site a partir de um cabeçalho e rodapé comuns.
# Uso: python _build/build.py   (rodar de dentro da pasta site/)
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA = "https://wa.me/5511948714027"
def wa(msg):
    from urllib.parse import quote
    return WA + "?text=" + quote(msg)
MAPS = "https://www.google.com/maps/search/?api=1&query=Rua+Col%C3%BAmbia%2C+438%2C+Parque+das+Na%C3%A7%C3%B5es%2C+Santo+Andr%C3%A9+-+SP"
IG = "https://www.instagram.com/escola_cantinho_do_mel/"
FB = "https://www.facebook.com/escolacantinhodomel/"

NAV = [("index.html", "Início"), ("a-escola.html", "A escola"), ("cursos.html", "Cursos"),
       ("aulas-extras.html", "Aulas extras"), ("matricula.html", "Matrícula"), ("contato.html", "Contato")]

# ---------- Ícones ----------
SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
<symbol id="i-wa" viewBox="0 0 32 32"><path fill="currentColor" d="M16 3C8.8 3 3 8.7 3 15.8c0 2.3.6 4.5 1.8 6.5L3 29l6.9-1.8c1.9 1 4 1.6 6.1 1.6 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.5c-1.9 0-3.8-.5-5.4-1.5l-.4-.2-4.1 1.1 1.1-4-.3-.4c-1.1-1.7-1.6-3.6-1.6-5.6C5.3 10 10.1 5.3 16 5.3S26.7 10 26.7 15.8 21.9 26.5 16 26.5zm5.9-8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.2 1.4 3.4c.2.2 2.3 3.5 5.6 4.9.8.3 1.4.5 1.9.7.8.2 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21.5s-7.5-6.4-7.5-12a7.5 7.5 0 0115 0c0 5.6-7.5 12-7.5 12z" fill="currentColor"/><circle cx="12" cy="9.5" r="2.8" fill="#fff"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M12 7v5l3.5 2" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></symbol>
<symbol id="i-heart" viewBox="0 0 24 24"><path d="M12 20.5s-8-4.9-8-11A4.5 4.5 0 0112 6.6a4.5 4.5 0 018 2.9c0 6.1-8 11-8 11z" fill="currentColor"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M6.6 3.5l3 .4 1.2 4-2 1.5a12 12 0 005.8 5.8l1.5-2 4 1.2.4 3c0 1.2-1 2.1-2.2 2.1C10.4 19.5 4.5 13.6 4.5 5.7c0-1.2.9-2.2 2.1-2.2z" fill="currentColor"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5.5" width="18" height="13" rx="3" fill="currentColor"/><path d="M4 7l8 6 8-6" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-insta" viewBox="0 0 24 24"><rect x="3.5" y="3.5" width="17" height="17" rx="5" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="17.2" cy="6.8" r="1.3" fill="currentColor"/></symbol>
<symbol id="i-home" viewBox="0 0 24 24"><path d="M3.5 11L12 3.8 20.5 11v8.7a1.3 1.3 0 01-1.3 1.3H15v-6H9v6H4.8a1.3 1.3 0 01-1.3-1.3z" fill="currentColor"/></symbol>
<symbol id="i-blocks" viewBox="0 0 24 24"><rect x="3" y="12" width="8" height="8" rx="2" fill="currentColor"/><rect x="13" y="12" width="8" height="8" rx="2" fill="currentColor"/><rect x="8" y="3.5" width="8" height="8" rx="2" fill="currentColor"/></symbol>
<symbol id="i-family" viewBox="0 0 24 24"><circle cx="8" cy="6.5" r="3" fill="currentColor"/><circle cx="16.5" cy="9" r="2.4" fill="currentColor"/><path d="M2.5 20c0-4 2.5-7 5.5-7s5.5 3 5.5 7zM12.5 20c0-3 1.8-5.5 4-5.5s4 2.5 4 5.5z" fill="currentColor"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 2.8l8 3v6c0 5-3.4 8.6-8 9.9-4.6-1.3-8-4.9-8-9.9v-6z" fill="currentColor"/><path d="M8.3 12l2.6 2.6 4.9-5" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-apple" viewBox="0 0 24 24"><path d="M12 7.5c1.6-1.4 5-1.6 6.6.8 1.8 2.7.3 8-2.4 10.6-1.3 1.3-2.6 1-4.2.4-1.6.6-2.9.9-4.2-.4C5.1 16.3 3.6 11 5.4 8.3 7 5.9 10.4 6.1 12 7.5z" fill="currentColor"/><path d="M12 7.5c0-2 .8-3.6 2.6-4.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></symbol>
<symbol id="i-book" viewBox="0 0 24 24"><path d="M3 5.5c3-1.3 6-1.3 9 .8 3-2.1 6-2.1 9-.8v13.3c-3-1.2-6-1.2-9 .9-3-2.1-6-2.1-9-.9z" fill="currentColor"/><path d="M12 6.3v13.4" stroke="#fff" stroke-width="1.8"/></symbol>
<symbol id="i-star" viewBox="0 0 24 24"><path d="M12 3l2.7 5.6 6.1.8-4.5 4.3 1.1 6.1L12 16.9l-5.4 2.9 1.1-6.1-4.5-4.3 6.1-.8z" fill="currentColor"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12.5l4.2 4.2L19 7" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-cam" viewBox="0 0 48 48"><path d="M8 15h7l3-5h12l3 5h7a3 3 0 013 3v18a3 3 0 01-3 3H8a3 3 0 01-3-3V18a3 3 0 013-3z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="24" cy="26" r="7" fill="none" stroke="currentColor" stroke-width="3"/></symbol>
<symbol id="i-flower" viewBox="0 0 40 40"><g fill="#fff"><circle cx="20" cy="9" r="7"/><circle cx="31" cy="17" r="7"/><circle cx="27" cy="30" r="7"/><circle cx="13" cy="30" r="7"/><circle cx="9" cy="17" r="7"/></g><circle cx="20" cy="20" r="6" fill="#FFC21A"/></symbol>
<symbol id="i-flower-r" viewBox="0 0 40 40"><g fill="#E5507A"><circle cx="20" cy="9" r="7"/><circle cx="31" cy="17" r="7"/><circle cx="27" cy="30" r="7"/><circle cx="13" cy="30" r="7"/><circle cx="9" cy="17" r="7"/></g><circle cx="20" cy="20" r="6" fill="#FFC21A"/></symbol>
<symbol id="i-cloud" viewBox="0 0 200 90"><path d="M40 86a32 32 0 01-4-63.7A40 40 0 01111 14a30 30 0 0145 18 27 27 0 0114 54z"/></symbol>
</svg>"""

# Desenhos das aulas extras (traço escuro, cores chapadas)
INK = "#1E2340"
ART = {
 "ballet": f"""<svg viewBox="0 0 120 120" aria-hidden="true"><g stroke="{INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M46 20c-8 10-10 26-6 40" fill="none"/><path d="M78 20c6 12 6 26 0 40" fill="none"/><path d="M46 20c10-6 22-6 32 0" fill="none"/><ellipse cx="44" cy="76" rx="15" ry="26" transform="rotate(-14 44 76)" fill="#F59DBE"/><ellipse cx="44" cy="70" rx="8" ry="13" transform="rotate(-14 44 70)" fill="#E5507A"/><ellipse cx="78" cy="76" rx="15" ry="26" transform="rotate(14 78 76)" fill="#F59DBE"/><ellipse cx="78" cy="70" rx="8" ry="13" transform="rotate(14 78 70)" fill="#E5507A"/></g></svg>""",
 "edfisica": f"""<svg viewBox="0 0 120 120" aria-hidden="true"><g stroke="{INK}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"><ellipse cx="60" cy="96" rx="38" ry="9" fill="#67B83F"/><path d="M60 18L80 90H40z" fill="#E8730C"/><path d="M50 54h20M45 72h30" stroke="#fff" stroke-width="8"/><path d="M60 18L80 90H40z" fill="none"/><rect x="30" y="88" width="60" height="9" rx="4" fill="#E8730C"/></g></svg>""",
 "taekwondo": f"""<svg viewBox="0 0 120 120" aria-hidden="true"><g stroke="{INK}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"><path d="M40 20l20 10 20-10 24 14-8 18-12-6v52H36V46l-12 6-8-18z" fill="#fff"/><path d="M48 24l12 34 12-34" fill="none"/><path d="M60 58v40" fill="none"/><rect x="34" y="62" width="52" height="10" rx="3" fill="{INK}"/><path d="M54 72l-6 18M66 72l6 18" stroke="{INK}" stroke-width="6"/></g></svg>""",
 "musica": f"""<svg viewBox="0 0 120 120" aria-hidden="true"><g stroke="{INK}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"><path d="M48 82V30l42-10v52" fill="none"/><path d="M48 30l42-10v14l-42 10z" fill="{INK}"/><ellipse cx="38" cy="84" rx="12" ry="9" fill="#E5507A"/><ellipse cx="80" cy="74" rx="12" ry="9" fill="#67B83F"/><path d="M18 50c-6 6-6 16 0 22M102 44c6 6 6 16 0 22" fill="none" stroke="#E8730C"/></g></svg>""",
 "futebol": f"""<svg viewBox="0 0 120 120" aria-hidden="true"><g stroke="{INK}" stroke-width="4" stroke-linejoin="round"><circle cx="60" cy="60" r="40" fill="#fff"/><path d="M60 44l15 11-6 18H51l-6-18z" fill="{INK}"/><path d="M60 44V22M75 55l20-6M69 73l12 17M51 73L39 90M45 55l-20-6" fill="none"/><path d="M42 24l-4 10 8 6 14-6M78 24l4 10-8 6M96 66l-8 2-4 10M24 66l8 2 4 10" fill="none" stroke-linecap="round"/></g></svg>""",
 "ingles": f"""<svg viewBox="0 0 120 120" aria-hidden="true"><g stroke="{INK}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"><path d="M22 26h76a8 8 0 018 8v38a8 8 0 01-8 8H58L40 96V80H22a8 8 0 01-8-8V34a8 8 0 018-8z" fill="#6BB8E6"/></g><text x="60" y="66" text-anchor="middle" font-family="Fredoka, sans-serif" font-weight="700" font-size="30" fill="{INK}">Hi!</text><path d="M100 10l3 7 7 3-7 3-3 7-3-7-7-3 7-3z" fill="#FFC21A" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/></svg>""",
 "artes": f"""<svg viewBox="0 0 120 120" aria-hidden="true"><g stroke="{INK}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"><path d="M60 18c26 0 44 16 44 36 0 14-12 16-22 14-8-2-12 4-8 12 4 10-4 18-16 18-26 0-42-18-42-40s18-40 44-40z" fill="#FFF4D2"/><circle cx="40" cy="46" r="8" fill="#E5507A"/><circle cx="60" cy="36" r="8" fill="#FFC21A"/><circle cx="82" cy="44" r="8" fill="#6BB8E6"/><circle cx="38" cy="72" r="8" fill="#67B83F"/></g></svg>""",
}
ACTS = [
 ("ballet", "Ballet", "berry", "Postura, ritmo e expressão. A dança faz bem ao corpo e às emoções e traz disciplina, criatividade e trabalho em grupo.",
  "Dançar é divertido e muito saudável. O ballet melhora a coordenação motora, desperta a disciplina e o esforço e favorece a criatividade, a musicalidade, o respeito ao próximo e o trabalho em grupo."),
 ("edfisica", "Educação física", "orange", "Correr, pular e equilibrar. O movimento ajuda a criança a expressar emoções e a conhecer o próprio corpo.",
  "O movimento do corpo tem papel essencial no desenvolvimento infantil: expressa emoções, melhora a postura e a linguagem corporal e desenvolve a capacidade afetiva e intelectual da criança."),
 ("taekwondo", "Taekwondo", "sky", "Concentração, disciplina e respeito. Ao dominar o corpo, a criança ganha autoestima e segurança.",
  "Concentração e disciplina. Ao dominar o corpo, a criança ganha autoestima e segurança, aprende honestidade, lealdade, companheirismo, respeito e humildade, e conhece costumes de outra cultura."),
 ("musica", "Musicalização", "honey", "Cantar, bater e ouvir. A música estimula a linguagem, a memória e a atenção.",
  "A iniciação musical estimula áreas do cérebro que ajudam no desenvolvimento de outras linguagens e de muitas habilidades motoras e intelectuais. E é uma forma de a criança expressar o que sente."),
 ("futebol", "Futebol", "grass", "Chutar, correr e jogar junto. Coordenação e espírito de equipe desde cedo.",
  "Desenvolve habilidades como caminhar, saltar e correr, e também arremessar, receber e chutar a bola. Movimento e trabalho em equipe, com papel essencial na educação infantil."),
 ("ingles", "Inglês", "sky", "As primeiras palavras em inglês com músicas e brincadeiras, em parceria com o CCAA.",
  "É na Educação Infantil que a criança mais desenvolve suas potencialidades. Quanto antes começar o contato com o inglês, mais facilidade e naturalidade ela terá. Em parceria com o CCAA."),
 ("artes", "Artes", "orange", "Faz de conta e criatividade: um simples traço vira o telhado de uma casa.",
  "A criança pensa como um artista: entra fácil no faz de conta e usa o dom de fantasiar. Pintura, colagem e modelagem estimulam a coordenação fina, a imaginação e a autoestima."),
]
ART_BG = {"berry": "var(--berry-l)", "orange": "var(--orange-l)", "sky": "var(--sky-l)", "honey": "var(--honey-l)", "grass": "var(--grass-l)"}

def ph(label, cls="", tone=""):
    return f'<div class="ph {tone} {cls}" role="img" aria-label="Espaço para foto: {label}"><span class="ph-in"><svg aria-hidden="true"><use href="#i-cam"/></svg>{label}</span></div>'

def combs():
    return '<span class="combs" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>'

def sec_title(h, p="", left=False, hid=None):
    idattr = f' id="{hid}"' if hid else ""
    return f'<div class="sec-title{" left" if left else ""}">{combs()}<h2{idattr}>{h}</h2>{f"<p>{p}</p>" if p else ""}</div>'

SKY_DECOR = """
  <svg class="cloud c1" aria-hidden="true"><use href="#i-cloud"/></svg>
  <svg class="cloud c2" aria-hidden="true"><use href="#i-cloud"/></svg>
  <svg class="cloud c3" aria-hidden="true"><use href="#i-cloud"/></svg>
  <svg class="sun" viewBox="0 0 120 120" aria-hidden="true"><g class="rays" stroke="#FFC21A" stroke-width="7" stroke-linecap="round"><path d="M60 6v14M60 100v14M6 60h14M100 60h14M22 22l10 10M88 88l10 10M22 98l10-10M88 32l10-10"/></g><circle cx="60" cy="60" r="27" fill="#FFC21A"/><circle cx="51" cy="56" r="3.2" fill="#1E2340"/><circle cx="69" cy="56" r="3.2" fill="#1E2340"/><path d="M50 67c5 6 15 6 20 0" fill="none" stroke="#1E2340" stroke-width="3.5" stroke-linecap="round"/></svg>
  <svg class="hills" viewBox="0 0 1440 130" preserveAspectRatio="none" aria-hidden="true"><path d="M0 70C220 20 420 20 640 60s460 50 800-10V130H0z" fill="#8FD068"/><path d="M0 100c260-40 520-36 760-6s480 20 680-14V130H0z" fill="#67B83F"/></svg>
  <svg class="flower" style="left:6%" aria-hidden="true" viewBox="0 0 40 40"><use href="#i-flower-r"/></svg>
  <svg class="flower" style="left:22%;animation-delay:-1s;width:22px" aria-hidden="true" viewBox="0 0 40 40"><use href="#i-flower"/></svg>
  <svg class="flower" style="left:48%;animation-delay:-2s" aria-hidden="true" viewBox="0 0 40 40"><use href="#i-flower"/></svg>
  <svg class="flower" style="left:71%;animation-delay:-.5s;width:24px" aria-hidden="true" viewBox="0 0 40 40"><use href="#i-flower-r"/></svg>
  <svg class="flower" style="left:90%;animation-delay:-1.6s" aria-hidden="true" viewBox="0 0 40 40"><use href="#i-flower"/></svg>
"""

def head(title, desc, page):
    nav = "\n        ".join(f'<a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#FFC21A">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://escola-cantinho-do-mel.vercel.app/img/fachada.jpg">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="img/icon.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<script>document.documentElement.classList.add('js')</script>
{SPRITE}
<a class="skip" href="#conteudo">Pular para o conteúdo</a>

<header class="top" id="top">
  <div class="container top-in">
    <a class="brand" href="index.html" aria-label="Cantinho do Mel, página inicial"><img src="img/logo.webp" alt="Cantinho do Mel, Educação Infantil e Berçário" width="1200" height="250"></a>
    <nav id="menu" class="menu" aria-label="Principal">
        {nav}
        <a class="btn btn-orange btn-sm" href="{wa('Olá! Gostaria de agendar uma visita ao Cantinho do Mel.')}" target="_blank" rel="noopener"><svg width="18" height="18" aria-hidden="true"><use href="#i-wa"/></svg>Agendar visita</a>
    </nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu"><span class="menu-btn-txt">Menu</span><span class="burger" aria-hidden="true"><i></i><i></i></span></button>
  </div>
  <svg class="drip" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0H1440V14C1418 14 1414 44 1398 44S1380 14 1352 14 1322 22 1306 22 1290 14 1262 14 1238 52 1218 52 1196 14 1168 14 1140 28 1124 28 1106 14 1078 14 1056 40 1040 40 1022 14 994 14 968 24 952 24 936 14 908 14 884 56 862 56 840 14 812 14 790 30 774 30 758 14 730 14 706 46 688 46 670 14 642 14 618 22 602 22 586 14 558 14 532 50 512 50 492 14 464 14 440 32 424 32 408 14 380 14 356 42 338 42 320 14 292 14 268 24 252 24 236 14 208 14 182 54 162 54 142 14 114 14 92 30 76 30 60 14 32 14 16 38 0 38Z"/></svg>
</header>

<main id="conteudo">
"""

def page_hero(crumb, h1, lede):
    return f"""<section class="sky page-hero" aria-labelledby="page-title">
  {SKY_DECOR}
  <img class="flyer" src="img/abelha.webp" alt="" width="355" height="405" style="right:24%;top:30%">
  <div class="container"><div class="page-hero-in">
    <nav class="crumbs" aria-label="Você está em"><a href="index.html">Início</a><span aria-hidden="true">›</span><span>{crumb}</span></nav>
    <h1 id="page-title">{h1}</h1>
    <p class="lede">{lede}</p>
  </div></div>
</section>
"""

def cta(title="Venha conhecer o Cantinho do Mel", text="Agende uma visita, conheça as salas e a equipe e tire todas as suas dúvidas. As matrículas estão abertas."):
    return f"""<section class="section" aria-labelledby="cta-title">
  <div class="container">
    <div class="cta">
      <div class="cta-text">
        <span class="pill"><span class="dot"></span>Matrículas abertas</span>
        <h2 id="cta-title">{title}</h2>
        <p>{text}</p>
        <div class="cta-actions">
          <a class="btn btn-lg" href="{wa('Olá! Gostaria de agendar uma visita ao Cantinho do Mel.')}" target="_blank" rel="noopener"><svg width="20" height="20" aria-hidden="true"><use href="#i-wa"/></svg>Chamar no WhatsApp</a>
          <a class="btn btn-white btn-lg" href="tel:+551126778022"><svg width="18" height="18" aria-hidden="true"><use href="#i-phone"/></svg>(11) 2677-8022</a>
        </div>
      </div>
      <img class="cta-bee" src="img/abelha.webp" alt="Abelhinha, mascote do Cantinho do Mel" width="355" height="405" loading="lazy">
    </div>
  </div>
</section>
"""

def foot():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""</main>

<footer class="footer">
  <svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40C240 0 480 0 720 26s480 40 720 0V60H0z"/></svg>
  <div class="container">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="img/logo.webp" alt="Cantinho do Mel" width="1200" height="250" loading="lazy">
        <p>Escola Cantinho do Mel: educação infantil e berçário no Parque das Nações, Santo André, desde 1992.</p>
        <p class="motto">Conhecimento, afeto e um ambiente aconchegante.</p>
      </div>
      <div><h3>Navegue</h3><ul>{links}</ul></div>
      <div><h3>Fale com a gente</h3><ul>
        <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp (11) 94871-4027</a></li>
        <li><a href="tel:+551126778022">Telefone (11) 2677-8022</a></li>
        <li><a href="tel:+5511969317414">Celular (11) 96931-7414</a></li>
        <li><a href="mailto:contato@escolacantinhodomel.com.br">contato@escolacantinhodomel.com.br</a></li>
      </ul></div>
      <div><h3>Endereço</h3><ul>
        <li>Rua Colúmbia, 438</li><li>Parque das Nações, Santo André, SP</li><li>CEP 09241-000</li><li>Seg. a sex., 6h30 às 19h</li>
        <li><a href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a href="{FB}" target="_blank" rel="noopener">Facebook</a></li>
      </ul></div>
    </div>
    <div class="foot-meta"><p>© Escola Cantinho do Mel · Educação Infantil e Berçário · Santo André, SP</p><a href="#top">Voltar ao topo ↑</a></div>
  </div>
</footer>

<a class="wa-fab" href="{wa('Olá! Vim pelo site do Cantinho do Mel.')}" target="_blank" rel="noopener" aria-label="Fale com a gente no WhatsApp"><svg width="26" height="26" aria-hidden="true"><use href="#i-wa"/></svg><span>Fale com a gente</span></a>

<script src="main.js" defer></script>
</body>
</html>
"""

def acts_grid(link=True):
    items = []
    for key, name, tone, short, _ in ACTS:
        items.append(f'<a class="act" href="aulas-extras.html#{key}"><div class="act-art" style="background:{ART_BG[tone]}">{ART[key]}</div><h3>{name}</h3><p>{short}</p></a>')
    items.append(f'<div class="act act-cta"><h3>Todas dentro da escola</h3><p>Sem precisar levar seu filho para outro lugar. Pergunte quais estão no período escolhido.</p><a class="btn btn-sm" href="aulas-extras.html">Ver aulas extras<svg width="18" height="18" aria-hidden="true"><use href="#i-arrow"/></svg></a></div>')
    return '<div class="acts">' + "".join(items) + "</div>"

PARTNERS = f"""<div class="partners">
      <article class="partner">
        <div class="partner-logo"><img src="img/positivo.webp" alt="Sistema de Ensino Positivo, escola conveniada" width="800" height="365"></div>
        <div><h3>Sistema de Ensino Positivo</h3><p>Somos escola conveniada. A Educação Infantil usa o material didático do Sistema Positivo de Ensino, com atividades práticas para cada idade.</p></div>
      </article>
      <article class="partner">
        <div class="partner-logo"><img src="img/ccaa.webp" alt="CCAA" width="700" height="508"></div>
        <div><h3>Inglês com o CCAA</h3><p>As aulas de inglês são em parceria com o CCAA, para a criança ter contato com a língua desde cedo, de um jeito leve e natural.</p></div>
      </article>
    </div>
    <ul class="more-partners">
      <li><strong>Kid Note</strong> · agenda digital</li>
      <li><strong>Aline Fregozzi</strong> · nutricionista</li>
      <li><strong>N'Atividade</strong> · esporte e nutrição</li>
    </ul>"""

PERIODS = f"""<div class="periods" id="periodos-box">
      <div class="ptabs" role="tablist" aria-label="Períodos">
        <button type="button" role="tab" aria-selected="false" data-from="390" data-to="720" data-title="Meio período da manhã" data-tag="Manhã" data-text="A criança chega pela manhã, participa das atividades, lancha e almoça antes da saída." data-btn="Quero o meio período">Meio período<small>manhã</small></button>
        <button type="button" role="tab" aria-selected="false" data-from="720" data-to="1140" data-title="Meio período da tarde" data-tag="Tarde" data-text="A criança chega depois do almoço, faz as atividades da tarde, lancha e vai para casa." data-btn="Quero o meio período">Meio período<small>tarde</small></button>
        <button type="button" role="tab" aria-selected="false" data-from="390" data-to="900" data-title="Semi-integral" data-tag="Mais tempo" data-text="Mais horas na escola, com refeições e atividades da manhã e de parte da tarde." data-btn="Quero o semi-integral">Semi-integral<small>meio dia e meio</small></button>
        <button type="button" role="tab" aria-selected="true" data-from="390" data-to="1140" data-title="6h30 às 19h" data-tag="12h30 na escola" data-text="O dia todo na escola, com café, almoço, lanches e jantar feitos na nossa cozinha, descanso, atividades e aulas extras." data-btn="Quero o integral">Integral<small>o dia todo</small></button>
      </div>
      <div class="pcard" aria-live="polite">
        <div class="pcard-head"><h3 id="p-title">6h30 às 19h</h3><span class="tag" id="p-tag">12h30 na escola</span></div>
        <div class="bar"><div class="bar-fill" id="p-fill" style="left:0;right:0"></div></div>
        <div class="bar-marks" aria-hidden="true"><span style="left:0">6h30</span><span style="left:20%">9h</span><span style="left:40%">11h30</span><span style="left:60%">14h</span><span style="left:80%">16h30</span><span style="left:100%">19h</span></div>
        <p class="pcard-text" id="p-text">O dia todo na escola, com café, almoço, lanches e jantar feitos na nossa cozinha, descanso, atividades e aulas extras.</p>
        <div class="pcard-foot"><a class="btn btn-orange" id="p-btn" href="matricula.html">Quero o integral</a><small>Os horários de entrada e saída de cada período são combinados na matrícula.</small></div>
      </div>
    </div>"""

FAQ = [
 ("Com que idade meu filho pode começar?", "No berçário recebemos bebês a partir de 4 meses. Depois, a criança segue pelos níveis da Educação Infantil (Nível I a Nível IV), sempre com planejamento próprio para cada faixa etária."),
 ("Qual é o horário e quais são os períodos?", "A escola funciona de segunda a sexta, das 6h30 às 19h. Você escolhe entre meio período (manhã ou tarde), semi-integral ou integral. Os horários de entrada e saída são combinados na matrícula."),
 ("Qual material didático vocês usam?", "A Educação Infantil usa o Sistema de Ensino Positivo, da Editora Positivo. Somos escola conveniada. O berçário tem planejamentos próprios para cada idade."),
 ("Como funciona a alimentação?", "As refeições são feitas em cozinha própria, com alimentos frescos. O cardápio é da nutricionista Aline Fregozzi e respeita a orientação do pediatra de cada criança. Restrições e alergias são combinadas com a família."),
 ("Quais aulas extras a escola oferece?", "Ballet, educação física, taekwondo, musicalização, futebol, inglês (em parceria com o CCAA) e artes, todas dentro da escola. Pergunte quais estão incluídas no período escolhido."),
 ("Como acompanho o dia do meu filho?", "Pela agenda digital Kid Note, no celular: recados, rotina e comunicados da escola chegam direto para a família."),
 ("A escola é segura?", "Sim. A escola tem câmeras, alarme e uma vaga exclusiva de embarque e desembarque escolar na porta. Os bebês são supervisionados de perto pela coordenação."),
 ("Posso conhecer a escola antes de matricular?", "Claro. Agende uma visita pelo WhatsApp (11) 94871-4027 ou pelo telefone (11) 2677-8022 e venha conhecer as salas e a equipe."),
 ("Qual é o valor da mensalidade?", "Os valores dependem da turma e do período. Monte a matrícula nesta página e a gente responde no WhatsApp com todos os detalhes."),
]
def faq_html(items):
    out = []
    for i, (q, a) in enumerate(items):
        out.append(f'<details{" open" if i == 0 else ""}><summary>{q}<i aria-hidden="true"></i></summary><div class="acc-body"><p>{a}</p></div></details>')
    return '<div class="acc">' + "".join(out) + "</div>"

ENROLL = f"""<form class="enroll" id="enroll" action="{WA}" method="get" target="_blank">
      <div class="enroll-picks">
        <fieldset class="pick"><legend>Idade da criança</legend><div class="pick-row">
          <label><input type="radio" name="idade" value="Berçário I|4 a 11 meses"><span>4 a 11 meses</span></label>
          <label><input type="radio" name="idade" value="Berçário II|1 ano" checked><span>1 ano</span></label>
          <label><input type="radio" name="idade" value="Nível I|2 anos"><span>2 anos</span></label>
          <label><input type="radio" name="idade" value="Nível II|3 anos"><span>3 anos</span></label>
          <label><input type="radio" name="idade" value="Nível III|4 anos"><span>4 anos</span></label>
          <label><input type="radio" name="idade" value="Nível IV|5 anos"><span>5 anos</span></label>
        </div></fieldset>
        <fieldset class="pick"><legend>Período</legend><div class="pick-row">
          <label><input type="radio" name="periodo" value="Meio período (manhã)"><span>Meio período manhã</span></label>
          <label><input type="radio" name="periodo" value="Meio período (tarde)"><span>Meio período tarde</span></label>
          <label><input type="radio" name="periodo" value="Semi-integral"><span>Semi-integral</span></label>
          <label><input type="radio" name="periodo" value="Integral" checked><span>Integral</span></label>
        </div></fieldset>
        <label class="name-field"><span>Nome da criança <em>(opcional)</em></span><input type="text" id="kid" name="crianca" autocomplete="off" maxlength="40" placeholder="Ex.: Helena"></label>
      </div>
      <div class="ticket" aria-live="polite">
        <p class="ticket-small">Turma indicada</p>
        <p class="ticket-class" id="ticket-class">Berçário II</p>
        <p class="ticket-meta" id="ticket-meta">1 ano · integral</p>
        <p class="ticket-msg" id="ticket-msg">Olá! Vim pelo site do Cantinho do Mel. Tenho uma criança de 1 ano (turma Berçário II), período integral. Pode me passar os valores e um horário para visita?</p>
        <button class="btn btn-wa btn-lg" type="submit"><svg width="20" height="20" aria-hidden="true"><use href="#i-wa"/></svg>Enviar no WhatsApp</button>
        <input type="hidden" name="text" id="enroll-text" value="Olá! Gostaria de informações sobre matrícula no Cantinho do Mel.">
      </div>
    </form>"""

def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", name)

# =================== INÍCIO ===================
home = head("Escola Cantinho do Mel · Berçário e Educação Infantil em Santo André",
            "Berçário e educação infantil no Parque das Nações, Santo André, desde 1992. Bebês a partir de 4 meses, de segunda a sexta, das 6h30 às 19h. Matrículas abertas.", "index.html")
home += f"""
<section class="sky hero" aria-labelledby="hero-title">
  {SKY_DECOR}
  <img class="flyer" src="img/abelha.webp" alt="" width="355" height="405" style="left:41%;bottom:15%">
  <div class="container hero-grid">
    <div class="hero-text">
      <span class="pill"><span class="dot"></span>Matrículas abertas</span>
      <p class="hero-kicker">Escola Cantinho do Mel: berçário e educação infantil no Parque das Nações, em Santo André</p>
      <h1 id="hero-title">Um cantinho doce <span class="hl">para crescer<svg viewBox="0 0 200 16" preserveAspectRatio="none" aria-hidden="true"><path d="M3 11C50 3 150 3 197 9" fill="none" stroke="#FFC21A" stroke-width="7" stroke-linecap="round"/></svg></span></h1>
      <p class="lede">Bebês a partir de 4 meses, cozinha própria, Sistema de Ensino Positivo e sete aulas extras dentro da escola. Tudo com muito carinho, desde 1992.</p>
      <div class="hero-actions">
        <a class="btn btn-orange btn-lg" href="{wa('Olá! Quero saber sobre matrículas no Cantinho do Mel.')}" target="_blank" rel="noopener"><svg width="20" height="20" aria-hidden="true"><use href="#i-wa"/></svg>Garantir a vaga</a>
        <a class="btn btn-white btn-lg" href="{MAPS}" target="_blank" rel="noopener"><svg width="18" height="18" aria-hidden="true"><use href="#i-pin"/></svg>Como chegar</a>
      </div>
      <div class="hero-meta">
        <span><i><svg width="16" height="16" aria-hidden="true"><use href="#i-heart"/></svg></i>Desde 1992</span>
        <span><i><svg width="16" height="16" aria-hidden="true"><use href="#i-clock"/></svg></i>Seg. a sex., 6h30 às 19h</span>
        <span class="pill status" id="status" aria-live="polite"><span class="dot"></span><span class="status-txt">Horário de Brasília</span></span>
      </div>
    </div>
    <figure class="hero-card">
      <div class="frame"><img src="img/fachada.jpg" srcset="img/fachada-900.jpg 900w, img/fachada.jpg 1846w" sizes="(max-width: 900px) 92vw, 560px" alt="Fachada do Cantinho do Mel na Rua Colúmbia, 438: faixa de mel escorrendo, letras azuis, muro pintado com sol e abelhas e a abelha gigante no telhado" width="1846" height="852" fetchpriority="high"></div>
      <figcaption class="sticker">Integral · semi-integral<br>meio período</figcaption>
      <span class="sticker sticker-2" aria-hidden="true">Rua Colúmbia, 438</span>
    </figure>
  </div>
</section>

<div class="ribbon" aria-hidden="true"><div class="ribbon-track">
  <span>Berçário</span><span>Educação Infantil</span><span>Ballet</span><span>Taekwondo</span><span>Musicalização</span><span>Inglês CCAA</span><span>Futebol</span><span>Artes</span><span>Educação física</span><span>Cozinha própria</span><span>Sistema Positivo</span><span>Agenda Kid Note</span>
</div></div>

<section class="section" aria-labelledby="why-title">
  <div class="container">
    {sec_title("Por que escolher o Cantinho do Mel", "O que o seu filho encontra aqui, todos os dias.", hid="why-title")}
    <div class="cards cards-4">
      <article class="card"><span class="ico"><svg aria-hidden="true"><use href="#i-home"/></svg></span><h3>Desde 1992 no bairro</h3><p>Mais de três décadas cuidando das crianças do Parque das Nações, num espaço pensado só para a educação infantil.</p></article>
      <article class="card berry"><span class="ico berry"><svg aria-hidden="true"><use href="#i-heart"/></svg></span><h3>Equipe com afeto</h3><p>Profissionais qualificados que acompanham cada criança de perto, com carinho e supervisão da coordenação.</p></article>
      <article class="card orange"><span class="ico orange"><svg aria-hidden="true"><use href="#i-blocks"/></svg></span><h3>Aprender brincando</h3><p>Material do Sistema Positivo de Ensino, histórias, música, arte e movimento para cada idade.</p></article>
      <article class="card sky"><span class="ico sky"><svg aria-hidden="true"><use href="#i-family"/></svg></span><h3>Família por perto</h3><p>Recados, rotina e comunicados no celular pela agenda digital Kid Note, além de datas especiais na escola.</p></article>
    </div>
  </div>
</section>

<section class="section bg-cream" aria-labelledby="courses-title">
  <div class="container">
    {sec_title("Nossos cursos", "Do primeiro colo ao último ano antes do ensino fundamental.", hid="courses-title")}
    <div class="cards cards-2">
      <article class="course">{ph("Berçário", "r169", "honey")}<div class="course-body"><h3>Berçário</h3><p class="muted">Cuidado e educação num ambiente tranquilo, com cada bebê acompanhado individualmente.</p><ul class="chips"><li>Berçário I · 4 a 11 meses</li><li>Berçário II · 1 ano</li></ul><a class="link" href="cursos.html#bercario">Conhecer o berçário<svg width="18" height="18" aria-hidden="true"><use href="#i-arrow"/></svg></a></div></article>
      <article class="course">{ph("Educação Infantil", "r169", "")}<div class="course-body"><h3>Educação Infantil</h3><p class="muted">Desenvolvimento físico, social e emocional, com o Sistema de Ensino Positivo.</p><ul class="chips sky"><li>Nível I · 2 anos</li><li>Nível II · 3 anos</li><li>Nível III · 4 anos</li><li>Nível IV · 5 anos</li></ul><a class="link" href="cursos.html#infantil">Conhecer a Educação Infantil<svg width="18" height="18" aria-hidden="true"><use href="#i-arrow"/></svg></a></div></article>
    </div>
  </div>
</section>

<section class="section bg-honey-l" aria-labelledby="periods-title">
  <div class="container">
    {sec_title("Um período para cada rotina", "Meio período, semi-integral ou integral: escolha e veja quanto do dia o seu filho passa com a gente.", hid="periods-title")}
    {PERIODS}
  </div>
</section>

<section class="section" aria-labelledby="acts-title">
  <div class="container">
    {sec_title("Aulas extras", "Mais movimento, mais música, um novo idioma e muita criatividade, sem sair da escola.", hid="acts-title")}
    {acts_grid()}
  </div>
</section>

<section class="section bg-sky-l" aria-labelledby="partners-title">
  <div class="container">
    {sec_title("Quem caminha com a gente", "Parceiros que ajudam a fazer o dia a dia do Cantinho.", hid="partners-title")}
    {PARTNERS}
  </div>
</section>

<section class="section" aria-labelledby="faq-title">
  <div class="container faq-grid">
    <div class="faq-side">{combs()}<h2 id="faq-title">Perguntas frequentes</h2><p>Ficou alguma dúvida? Chame no WhatsApp que a gente responde rapidinho.</p><a class="btn btn-wa" href="{wa('Olá! Tenho uma dúvida sobre o Cantinho do Mel.')}" target="_blank" rel="noopener"><svg width="18" height="18" aria-hidden="true"><use href="#i-wa"/></svg>Tirar uma dúvida</a></div>
    {faq_html(FAQ[:6])}
  </div>
</section>
{cta()}
"""
home += foot()
write("index.html", home)

# =================== A ESCOLA ===================
p = head("A escola · Escola Cantinho do Mel", "Conheça a história, a proposta pedagógica, a missão e a estrutura da Escola Cantinho do Mel, em Santo André.", "a-escola.html")
p += page_hero("A escola", "Pequena no tamanho, gigante no carinho", "Desde 1992 no Parque das Nações, em Santo André, cuidando e educando crianças a partir de 4 meses.")
p += f"""
<section class="section" aria-labelledby="hist-title">
  <div class="container split">
    <div class="split-text">
      {combs()}
      <h2 id="hist-title">Nossa história</h2>
      <p>A Escola Cantinho do Mel nasceu em 1992 com um propósito simples: ser um lugar aconchegante, seguro e estimulador para os primeiros anos de vida. Pense bem onde seu filho vai passar grande parte da infância: é aqui que ele aprende valores e vive experiências essenciais.</p>
      <p>Temos um amplo espaço e instalações próprias, uma equipe qualificada que trabalha com profissionalismo e carinho e horários flexíveis para atender à rotina de cada família.</p>
      <p class="strong">Desde 1992, brincando, cuidando e ensinando com amor.</p>
      <ul class="checks">
        <li><svg aria-hidden="true"><use href="#i-check"/></svg>Especialistas em berçário e educação infantil</li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg>Material didático do Sistema Positivo de Ensino</li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg>Cozinha própria com cardápio de nutricionista</li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg>Visita sem compromisso para conhecer a escola</li>
      </ul>
    </div>
    <div class="split-media">{ph("Equipe ou turma na escola", "r45", "honey")}<span class="badge"><strong>1992</strong>o ano em que abrimos</span></div>
  </div>
</section>

<section class="section bg-cream" aria-labelledby="prop-title">
  <div class="container">
    {sec_title("Proposta pedagógica", "Formação integral: capacidades motoras, afetivas, sociais e cognitivas.", hid="prop-title")}
    <div class="cards cards-3">
      <article class="card"><span class="ico"><svg aria-hidden="true"><use href="#i-blocks"/></svg></span><h3>Aprendizagem dinâmica</h3><p>Partimos da realidade de cada aluno. Com estímulos e desafios, ele age sobre o mundo e entende o que fez.</p></article>
      <article class="card grass"><span class="ico grass"><svg aria-hidden="true"><use href="#i-star"/></svg></span><h3>Global</h3><p>Corpo, emoções, linguagem e convivência caminham juntos, com atividades que desenvolvem a criança por inteiro.</p></article>
      <article class="card sky"><span class="ico sky"><svg aria-hidden="true"><use href="#i-book"/></svg></span><h3>Significativa</h3><p>O conhecimento é construído pela própria criança, com histórias, dramatização, brincadeiras e o Sistema Positivo.</p></article>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="mvv-title">
  <div class="container">
    {sec_title("Missão, visão e valores", hid="mvv-title")}
    <div class="cards cards-3">
      <article class="card white"><span class="ico orange"><svg aria-hidden="true"><use href="#i-heart"/></svg></span><h3>Missão</h3><p>Oferecer conhecimento, afeto e um ambiente aconchegante para formar cidadãos conscientes.</p></article>
      <article class="card white"><span class="ico navy"><svg aria-hidden="true"><use href="#i-star"/></svg></span><h3>Visão</h3><p>Ser referência em berçário e educação infantil.</p></article>
      <article class="card white"><span class="ico grass"><svg aria-hidden="true"><use href="#i-shield"/></svg></span><h3>Valores</h3><p>Cooperação, transparência, respeito, comprometimento, inovação e formação dos alunos.</p></article>
    </div>
  </div>
</section>

<section class="section bg-sky-l" aria-labelledby="est-title">
  <div class="container">
    {sec_title("Nossa estrutura", "Cada canto foi pensado para a criança se mexer, explorar e imaginar.", hid="est-title")}
    <div class="spaces">
      {ph("Berçário I", "big", "honey")}
      {ph("Berçário II", "", "")}
      {ph("Sala do Nível I", "tall", "grass")}
      {ph("Sala do Nível IV", "", "orange")}
      {ph("Biblioteca", "", "berry")}
      {ph("Brinquedoteca", "", "")}
      {ph("Parquinho", "", "grass")}
      {ph("Quadra coberta", "", "honey")}
    </div>
    <div class="here"><h3>Aqui tem</h3><ul><li>Salas para cada turma</li><li>Biblioteca</li><li>Brinquedoteca</li><li>Parquinho</li><li>Quadra coberta</li><li>Cozinha própria</li></ul></div>
  </div>
</section>

<section class="section" aria-labelledby="seg-title">
  <div class="container split rev">
    <div class="split-text">
      {combs()}
      <h2 id="seg-title">Segurança em primeiro lugar</h2>
      <p>Um ambiente seguro e bem assessorado, para a família ficar tranquila durante o dia.</p>
      <ul class="checks">
        <li><svg aria-hidden="true"><use href="#i-check"/></svg>Sistema de câmeras e alarme</li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg>Vaga exclusiva de embarque e desembarque escolar</li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg>Bebês supervisionados de perto pela coordenação</li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg>Rotina, recados e comunicados pela agenda Kid Note</li>
      </ul>
    </div>
    <div class="split-media">{ph("Entrada da escola", "r43", "grass")}</div>
  </div>
</section>

<section class="section bg-cream" aria-labelledby="partners-title">
  <div class="container">
    {sec_title("Quem caminha com a gente", hid="partners-title")}
    {PARTNERS}
  </div>
</section>
{cta()}
"""
p += foot()
write("a-escola.html", p)

# =================== CURSOS ===================
p = head("Cursos · Berçário e Educação Infantil · Cantinho do Mel", "Berçário a partir de 4 meses e Educação Infantil do Nível I ao Nível IV com o Sistema de Ensino Positivo. Alimentação em cozinha própria.", "cursos.html")
p += page_hero("Cursos", "Berçário e Educação Infantil", "Cada turma com sala, rotina e planejamento próprios, dos 4 meses aos 5 anos.")
p += f"""
<section class="section" id="bercario" aria-labelledby="ber-title">
  <div class="container split">
    <div class="split-text">
      {combs()}
      <h2 id="ber-title">Berçário</h2>
      <p>Cuidado e educação num ambiente tranquilo, que transmite confiança, afeto e aprendizagens que fazem sentido para os bebês.</p>
      <p>Cada bebê é acompanhado individualmente por profissionais qualificados, com supervisão direta da coordenação. A rotina respeita o tempo de cada um: colo, sono, alimentação, brincadeiras e muitos estímulos.</p>
      <div class="groups" style="width:100%">
        <div class="group"><strong>Berçário I</strong><span>4 a 11 meses</span></div>
        <div class="group"><strong>Berçário II</strong><span>1 ano</span></div>
      </div>
    </div>
    <div class="split-media">{ph("Berçário", "r45", "honey")}</div>
  </div>
</section>

<section class="section bg-cream" id="infantil" aria-labelledby="inf-title">
  <div class="container split rev">
    <div class="split-text">
      {combs()}
      <h2 id="inf-title">Educação Infantil</h2>
      <p>Uma base sólida para o crescimento saudável. Exploramos atividades que desenvolvem a criança física, social e emocionalmente, e estimulamos a linguagem com histórias, dramatização e brincadeiras, respeitando o jeito de cada um.</p>
      <p>Usamos o material didático do <strong>Sistema de Ensino Positivo</strong>, com atividades práticas programadas à medida que os conteúdos avançam.</p>
      <div class="groups" style="width:100%">
        <div class="group"><strong>Nível I</strong><span>2 anos</span></div>
        <div class="group"><strong>Nível II</strong><span>3 anos</span></div>
        <div class="group"><strong>Nível III</strong><span>4 anos</span></div>
        <div class="group"><strong>Nível IV</strong><span>5 anos</span></div>
      </div>
    </div>
    <div class="split-media">{ph("Educação Infantil", "r45", "")}</div>
  </div>
</section>

<section class="section" id="alimentacao" aria-labelledby="ali-title">
  <div class="container">
    {sec_title("Alimentação", "Tudo preparado na nossa cozinha, com alimentos fresquinhos e refeições equilibradas.", hid="ali-title")}
    <div class="cards cards-3">
      <article class="card grass"><span class="ico grass"><svg aria-hidden="true"><use href="#i-apple"/></svg></span><h3>Cozinha própria</h3><p>Refeições feitas na escola todos os dias. A equipe recebe treinamento periódico de higiene, conservação e manipulação dos alimentos.</p></article>
      <article class="card"><span class="ico"><svg aria-hidden="true"><use href="#i-book"/></svg></span><h3>Cardápio de nutricionista</h3><p>Elaborado pela nutricionista Aline Fregozzi, seguindo a orientação do pediatra de cada criança.</p></article>
      <article class="card berry"><span class="ico berry"><svg aria-hidden="true"><use href="#i-heart"/></svg></span><h3>Aula de nutrição</h3><p>Os pequenos aprendem, brincando, de onde vêm os alimentos e por que comer bem faz bem.</p></article>
    </div>
  </div>
</section>

<section class="section bg-honey-l" id="rotina" aria-labelledby="day-title">
  <div class="container">
    {sec_title("Um dia no Cantinho", "Arraste a abelhinha e veja o que acontece em cada hora do dia.", hid="day-title")}
    <div class="clock" id="clock">
      <div class="clock-read">
        <p class="clock-time" id="clock-time" aria-hidden="true">8h00</p>
        <div class="clock-now" aria-live="polite"><h3 id="clock-title">Roda de conversa</h3><p id="clock-text">A turma se encontra, canta, conta as novidades e combina o dia.</p></div>
      </div>
      <label class="clock-label" for="clock-range">Arraste para mudar a hora</label>
      <div class="clock-track"><div class="clock-fill"></div>
        <input type="range" id="clock-range" min="390" max="1140" step="15" value="480" aria-describedby="clock-title" aria-valuetext="8h00, roda de conversa">
        <ol class="clock-marks" aria-hidden="true"><li style="--p:0">6h30</li><li style="--p:.2">9h</li><li style="--p:.4">11h30</li><li style="--p:.6">14h</li><li style="--p:.8">16h30</li><li style="--p:1">19h</li></ol>
      </div>
      <p class="clock-note">Rotina de referência da Educação Infantil; cada turma tem a sua.</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="periods-title">
  <div class="container">
    {sec_title("Escolha o período", hid="periods-title")}
    {PERIODS}
  </div>
</section>
{cta("Qual turma é a do seu filho?", "Monte a matrícula em segundos: escolha a idade e o período e mande a mensagem pronta no WhatsApp.")}
"""
p += foot()
write("cursos.html", p)

# =================== AULAS EXTRAS ===================
p = head("Aulas extras · Escola Cantinho do Mel", "Ballet, educação física, taekwondo, musicalização, futebol, inglês com o CCAA e artes, todas dentro da Escola Cantinho do Mel.", "aulas-extras.html")
p += page_hero("Aulas extras", "Sete aulas extras, dentro da escola", "Valorizar a criatividade e oferecer estímulos diferentes ajuda a criança a desenvolver várias habilidades.")
rows = []
for i, (key, name, tone, short, long) in enumerate(ACTS):
    rows.append(f'<article class="extra" id="{key}"><div class="act-art" style="background:{ART_BG[tone]}">{ART[key]}</div><div class="extra-text"><h2 style="font-size:clamp(26px,2.6vw,34px)">{name}</h2><p>{long}</p></div>{ph(name, "r43", tone if tone != "sky" else "")}</article>')
p += f"""
<section class="section" aria-label="Lista de aulas extras">
  <div class="container">
    {"".join(rows)}
  </div>
</section>
<section class="section bg-sky-l" aria-labelledby="partners-title">
  <div class="container">
    {sec_title("Parcerias que fazem a diferença", hid="partners-title")}
    {PARTNERS}
  </div>
</section>
{cta("Quais aulas estão no seu período?", "Depende da turma e do período escolhido. Chame no WhatsApp e a gente te conta tudo.")}
"""
p += foot()
write("aulas-extras.html", p)

# =================== MATRÍCULA ===================
p = head("Matrícula · Escola Cantinho do Mel", "Monte a matrícula no Cantinho do Mel: escolha a idade e o período e envie a mensagem pronta no WhatsApp. Matrículas abertas.", "matricula.html")
p += page_hero("Matrícula", "Monte a matrícula do seu filho", "Escolha a idade e o período. A gente mostra a turma indicada e abre o WhatsApp com a mensagem pronta, é só enviar.")
p += f"""
<section class="section" aria-label="Monte a matrícula">
  <div class="container">
    {ENROLL}
  </div>
</section>
<section class="section bg-honey-l" aria-labelledby="periods-title">
  <div class="container">
    {sec_title("Um período para cada rotina", hid="periods-title")}
    {PERIODS}
  </div>
</section>
<section class="section" aria-labelledby="faq-title">
  <div class="container faq-grid">
    <div class="faq-side">{combs()}<h2 id="faq-title">Perguntas frequentes</h2><p>Ficou alguma dúvida? Chame no WhatsApp que a gente responde rapidinho.</p><a class="btn btn-wa" href="{wa('Olá! Tenho uma dúvida sobre a matrícula no Cantinho do Mel.')}" target="_blank" rel="noopener"><svg width="18" height="18" aria-hidden="true"><use href="#i-wa"/></svg>Tirar uma dúvida</a></div>
    {faq_html(FAQ)}
  </div>
</section>
"""
p += foot()
write("matricula.html", p)

# =================== CONTATO ===================
p = head("Contato · Escola Cantinho do Mel", "Endereço, telefone, WhatsApp, e-mail e mapa da Escola Cantinho do Mel, Rua Colúmbia, 438, Parque das Nações, Santo André.", "contato.html")
p += page_hero("Contato", "Venha nos visitar", "Estamos no Parque das Nações, em Santo André. Será um prazer mostrar cada cantinho da escola.")
p += f"""
<section class="section" aria-label="Formas de contato">
  <div class="container contact-grid">
    <div class="ccards">
      <div class="ccard"><span class="ico orange"><svg aria-hidden="true"><use href="#i-pin"/></svg></span><div><h3>Endereço</h3><p>Rua Colúmbia, 438 · Parque das Nações<br>Santo André, SP · CEP 09241-000</p><a class="link" href="{MAPS}" target="_blank" rel="noopener">Abrir no Google Maps<svg width="16" height="16" aria-hidden="true"><use href="#i-arrow"/></svg></a></div></div>
      <div class="ccard"><span class="ico grass"><svg aria-hidden="true"><use href="#i-wa"/></svg></span><div><h3>WhatsApp</h3><p>(11) 94871-4027</p><a class="link" href="{wa('Olá! Vim pelo site do Cantinho do Mel.')}" target="_blank" rel="noopener">Chamar no WhatsApp<svg width="16" height="16" aria-hidden="true"><use href="#i-arrow"/></svg></a></div></div>
      <div class="ccard"><span class="ico sky"><svg aria-hidden="true"><use href="#i-phone"/></svg></span><div><h3>Telefones</h3><p>(11) 2677-8022 · (11) 96931-7414</p><a class="link" href="tel:+551126778022">Ligar agora<svg width="16" height="16" aria-hidden="true"><use href="#i-arrow"/></svg></a></div></div>
      <div class="ccard"><span class="ico berry"><svg aria-hidden="true"><use href="#i-mail"/></svg></span><div><h3>E-mail</h3><p>contato@escolacantinhodomel.com.br</p><a class="link" href="mailto:contato@escolacantinhodomel.com.br">Enviar e-mail<svg width="16" height="16" aria-hidden="true"><use href="#i-arrow"/></svg></a></div></div>
      <div class="ccard"><span class="ico"><svg aria-hidden="true"><use href="#i-clock"/></svg></span><div><h3>Horário</h3><p>Segunda a sexta, das 6h30 às 19h</p><p class="pill status" id="status" style="margin-top:8px"><span class="dot"></span><span class="status-txt">Horário de Brasília</span></p></div></div>
      <div class="ccard"><span class="ico navy"><svg aria-hidden="true"><use href="#i-insta"/></svg></span><div><h3>Redes sociais</h3><p><a class="link" href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a class="link" href="{FB}" target="_blank" rel="noopener">Facebook</a></p></div></div>
    </div>
    <div class="map">
      <iframe title="Mapa: Escola Cantinho do Mel, Rua Colúmbia, 438, Santo André" src="https://www.google.com/maps?q=Escola+Cantinho+do+Mel,+Rua+Col%C3%BAmbia,+438,+Parque+das+Na%C3%A7%C3%B5es,+Santo+Andr%C3%A9+-+SP&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      <a class="btn btn-orange btn-sm" href="{MAPS}" target="_blank" rel="noopener"><svg width="16" height="16" aria-hidden="true"><use href="#i-pin"/></svg>Traçar rota até a escola</a>
    </div>
  </div>
</section>
{cta()}
"""
p += foot()
write("contato.html", p)
