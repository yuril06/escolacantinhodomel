# Cantinho do Mel — site

Referência de desenho: escolaviveraprender.com.br, adaptada. O muro pintado da fachada (céu, sol, grama, flores e
abelhas) vira o desenho do site; a abelha da logo é o mascote.

## Páginas
`index.html` (Início) · `a-escola.html` · `cursos.html` · `aulas-extras.html` · `matricula.html` · `contato.html`

As páginas são geradas por `_build/build.py` (cabeçalho, rodapé e ícones comuns). Para mudar textos, edite o
`build.py` e rode `python _build/build.py` dentro da pasta `site/`. Estilos em `styles.css`, interações em `main.js`.

## Cores
Mel `#FFC21A` · laranja `#E8730C` · azul `#1C3F9E` · céu `#CFEAFB` · grama `#67B83F` · rosa `#E5507A` · texto `#1E2340`.
Títulos em Fredoka, texto em Nunito. Botões com "degrau" embaixo; cartões em tons pastel.

## Fotos
Só a fachada, a logo e os logos Positivo/CCAA são imagens reais. Os outros espaços são reservados para fotos
(`<div class="ph ...">`). Para colocar uma foto, troque o bloco por:

    <img class="ph-photo r43" src="img/minha-foto.jpg" alt="Descrição" width="1200" height="900" loading="lazy">

(use `r43`, `r45`, `r169` ou `r11` igual ao espaço que está sendo substituído; no `build.py`, troque a chamada `ph(...)`).

## Interações
"Aberto agora" (horário de Brasília) · períodos com barra do dia · "Um dia no Cantinho" (arrastar a abelha) ·
perguntas em acordeão · "Monte a matrícula" com mensagem pronta para o WhatsApp · menu de celular.
