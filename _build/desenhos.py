# Desenhos das aulas extras, no traço do logo (contorno escuro, cores chapadas).
# Rode: python _build/desenhos.py
import math, os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "desenhos")
INK = "#1d2a4d"
def W(w=5):
    return f'stroke="{INK}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'
S = W()

def svg(body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img" aria-label="{label}">{body}</svg>\n'

def pts(cx, cy, r, n, rot=-90):
    return [(cx + r * math.cos(math.radians(rot + i * 360 / n)), cy + r * math.sin(math.radians(rot + i * 360 / n))) for i in range(n)]

def poly(p):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in p)

# bola de futebol
pent = pts(100, 98, 24, 5)
outer = pts(100, 98, 72, 5)
lines = "".join(f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}" {S}/>' for a, b in zip(pent, outer))
edge = "".join(f'<polygon points="{poly(pts(x, y, 14, 5, -90 + i * 72 + 180))}" fill="{INK}"/>' for i, (x, y) in enumerate(outer))
bola = svg(
    f'<ellipse cx="100" cy="182" rx="56" ry="9" fill="{INK}" opacity=".18"/>'
    f'<defs><clipPath id="b"><circle cx="100" cy="98" r="76"/></clipPath></defs>'
    f'<circle cx="100" cy="98" r="76" fill="#fff"/>'
    f'<g clip-path="url(#b)">{lines}{edge}</g>'
    f'<polygon points="{poly(pent)}" fill="{INK}"/>'
    f'<circle cx="100" cy="98" r="76" fill="none" {S}/>'
    f'<path d="M52 62a60 60 0 0 1 30-26" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".9"/>',
    "Bola de futebol")

# notas musicais
musica = svg(
    f'<path d="M70 150V58l84-18v92" fill="none" {W(8)}/>'
    f'<path d="M70 58l84-18v22l-84 18Z" fill="#ff5c8d" {S}/>'
    f'<ellipse cx="52" cy="152" rx="24" ry="18" transform="rotate(-20 52 152)" fill="#8e5be8" {S}/>'
    f'<ellipse cx="136" cy="134" rx="24" ry="18" transform="rotate(-20 136 134)" fill="#45bdf5" {S}/>'
    f'<path d="M30 40v40" fill="none" {W(6)}/><ellipse cx="22" cy="82" rx="12" ry="9" transform="rotate(-20 22 82)" fill="#ffd43b" {S}/>'
    f'<path d="M30 40c8 4 14 10 12 20" fill="none" {S}/>',
    "Notas musicais")

# sapatilhas de ballet
def sapatilha(cx, cy, rot):
    return (f'<g transform="rotate({rot} {cx} {cy})">'
            f'<ellipse cx="{cx}" cy="{cy}" rx="30" ry="62" fill="#ffb3c9" {S}/>'
            f'<ellipse cx="{cx}" cy="{cy-14}" rx="17" ry="34" fill="#ff8fb0" {W(4)}/>'
            f'<path d="M{cx-16} {cy-30}c-26-16-30-40-14-62M{cx+16} {cy-30}c22-18 30-38 16-60" fill="none" stroke="#ff5c8d" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cx="{cx}" cy="{cy-48}" r="7" fill="#ff5c8d" {W(3)}/></g>')
ballet = svg(
    f'<ellipse cx="100" cy="186" rx="64" ry="8" fill="{INK}" opacity=".15"/>'
    + sapatilha(72, 118, -14) + sapatilha(130, 112, 12)
    + f'<path d="M24 34l4 10 10 4-10 4-4 10-4-10-10-4 10-4Z" fill="#ffd43b" {W(3)}/>'
    + f'<path d="M176 30l3 8 8 3-8 3-3 8-3-8-8-3 8-3Z" fill="#ffd43b" {W(3)}/>',
    "Sapatilhas de ballet")

# frutas
seeds = "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.6" ry="4" fill="#ffd43b"/>' for x, y in [(138, 132), (152, 122), (148, 146), (162, 138), (134, 152), (156, 160)])
frutas = svg(
    f'<ellipse cx="100" cy="186" rx="78" ry="8" fill="{INK}" opacity=".15"/>'
    f'<path d="M30 132c-6 34 22 54 64 48 34-5 50-28 44-40-30 16-74 22-108-8Z" fill="#ffd43b" {S}/>'
    f'<path d="M30 132l-6-8M138 140l8-4" fill="none" {S}/>'
    f'<path d="M66 54c-16-10-44-6-48 22-4 26 12 52 30 54 8 1 12-4 18-4s10 5 18 4c18-2 34-28 30-54-4-28-32-32-48-22Z" fill="#f0483e" {S}/>'
    f'<path d="M66 54c0-12 4-22 12-28" fill="none" {S}/><path d="M72 36c10-12 26-12 32-4-10 8-24 10-32 4Z" fill="#5cbf3b" {S}/>'
    f'<path d="M34 70c2-8 8-12 14-12" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".8"/>'
    f'<path d="M148 104c22 0 36 14 30 36-6 22-22 36-34 38-12-2-24-18-26-40-2-20 12-34 30-34Z" fill="#ff5c8d" {S}/>{seeds}'
    f'<path d="M130 108c4-12 14-16 18-8 6-10 16-8 18 4-6 6-26 10-36 4Z" fill="#5cbf3b" {S}/>',
    "Frutas: maçã, banana e morango")

# quimono de judô
judo = svg(
    f'<path d="M78 30h44l42 26 18 60-28 10-12-38v108H58V88l-12 38-28-10 18-60Z" fill="#fff" {S}/>'
    f'<path d="M78 30l22 58 22-58" fill="#e9eef7" {S}/>'
    f'<path d="M100 88l-20 108" fill="none" {W(4)}/>'
    f'<rect x="56" y="128" width="88" height="20" rx="4" fill="#ffd43b" {S}/>'
    f'<path d="M92 146l-12 38 14 2 8-30 8 30 14-2-12-38" fill="#ffb703" {S}/>'
    f'<rect x="88" y="122" width="24" height="32" rx="6" fill="#ff7a1a" {S}/>',
    "Quimono de judô com faixa")

for nome, conteudo in {"bola": bola, "musica": musica, "ballet": ballet, "frutas": frutas, "judo": judo}.items():
    open(os.path.join(OUT, f"{nome}.svg"), "w", encoding="utf-8").write(conteudo)
    print("ok", nome)
