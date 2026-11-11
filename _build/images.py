# Seleciona, melhora levemente e exporta as fotos do site em WebP.
import os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SITE = os.path.join(ROOT, 'site')
OUT = os.path.join(SITE, 'img')
os.makedirs(os.path.join(OUT, 'fotos'), exist_ok=True)
os.makedirs(os.path.join(OUT, 'marcas'), exist_ok=True)
F = os.path.join(ROOT, 'fotos sem melhora', 'WhatsApp Image 2026-11-10 at {}.jpeg')
O = os.path.join(SITE, '_raw', 'old', '{}')
fotos = {
  'fachada': F.format('17.55.04'),
  'menina-uniforme': F.format('17.27.47 (2)'),
  'mandioca-bebe': F.format('17.27.46'),
  'mandioca-dupla': F.format('17.27.45 (1)'),
  'mandioca-menino': F.format('17.18.48'),
  'mandioca-bebe2': F.format('17.18.47'),
  'morangos': F.format('17.27.46 (1)'),
  'bercario-espelho': F.format('17.27.45'),
  'equipe': F.format('17.27.46 (2)'),
  'argila': F.format('17.27.47 (1)'),
  'refeitorio': F.format('17.27.47'),
  'bandeira': F.format('17.43.16'),
  'cadeiroes': F.format('17.43.15'),
  'frutas-turma': F.format('17.43.16 (1)'),
  'frutas-investigando': F.format('17.43.17'),
  'junina-1': F.format('17.43.17 (1)'),
  'junina-2': F.format('17.43.17 (2)'),
  'junina-3': F.format('17.43.17 (3)'),
  'mostra-1': F.format('17.43.18 (1)'),
  'mostra-2': F.format('17.43.18'),
  'soneca': F.format('17.43.18 (2)'),
  'farinha-1': F.format('17.43.19 (1)'),
  'farinha-2': F.format('17.43.19 (2)'),
  'farinha-mesa': F.format('17.43.19 (3)'),
  'carnaval': F.format('17.43.19'),
  'quebra-cabeca': F.format('18.34.41 (1)'),
  'pintura-chao': F.format('18.34.41 (2)'),
  'piquenique': F.format('18.34.41'),
  'formacao': F.format('18.34.42 (1)'),
  'roda-tapete': F.format('18.34.42'),
  'ballet-roda': O.format('ballet_zoom_2.jpg'),
  'ballet-sorriso': O.format('ballet_zoom_4.jpg'),
  'futebol': O.format('futebol_1.jpg'),
  'musica': O.format('musica_zoom_2.jpg'),
  'movimento': O.format('ed_fisica_zoom_2.jpg'),
}
def enhance(im, old=False):
    im = ImageOps.exif_transpose(im).convert('RGB')
    im = ImageOps.autocontrast(im, cutoff=0.6, preserve_tone=True)
    im = ImageEnhance.Color(im).enhance(1.10 if not old else 1.05)
    im = ImageEnhance.Brightness(im).enhance(1.03)
    return im
for name, path in fotos.items():
    im = enhance(Image.open(path), old='_raw' in path)
    for suffix, side in (('', 1400), ('-p', 720)):
        c = im.copy(); c.thumbnail((side, side), Image.LANCZOS)
        c = c.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=3))
        c.save(os.path.join(OUT, 'fotos', f'{name}{suffix}.webp'), 'WEBP', quality=80, method=6)
    print(name, im.size)
marcas = {
  'logo': '2479c72c-d2c7-4cdc-9064-378acbad3b72.png',
  'logo-redonda': 'logoredondacantinhodomel.png',
  'positivo': '5efbe114-5d5f-433a-8dc8-9a42429e9e60.png',
  'natividade': '6c3b1856-e3b9-4c82-96c8-cedc90ca35a6.png',
  'kidnote': 'ebfc0eb5-c493-45fc-b01a-3e0a065b23b8.png',
  'ccaa': 'f44b48cf-304a-4e06-8984-849a63c53141.png',
}
for name, f in marcas.items():
    im = Image.open(os.path.join(ROOT, f)).convert('RGBA')
    bbox = im.getchannel('A').getbbox()
    if bbox: im = im.crop(bbox)
    im.thumbnail((900, 900), Image.LANCZOS)
    im.save(os.path.join(OUT, 'marcas', f'{name}.webp'), 'WEBP', quality=88, method=6)
    if name == 'logo-redonda':
        for s in (32, 180, 512):
            im.resize((s, s), Image.LANCZOS).save(os.path.join(OUT, f'icone-{s}.png'))
    print(name, im.size)
