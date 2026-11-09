# Cantinho do Mel — design system

Direção: **Loud and flat** (tasteskill v2, seed 1743897944). Pôster de rua, campos de cor chapados, tipo pesado.

**Ideia:** o mel que escorre da faixa amarela da fachada da Rua Colúmbia, 438 vira os campos de cor do site;
as letras azuis gigantes da fachada viram o nome que atravessa a primeira tela.

**Parte viva:** "Monte a matrícula": a família escolhe a idade da criança e o período; o site mostra a turma
e abre o WhatsApp com a mensagem pronta.

## Cores (tokens)

| Token | Valor | Uso |
| --- | --- | --- |
| `--bg` | `#FFFFFF` | fundo |
| `--ink` | `#16181D` | texto |
| `--honey` | `#FFC21A` | campo principal (faixa da fachada) |
| `--orange` | `#E8730C` | campo secundário (logo) |
| `--navy` | `#1C3F9E` | ação principal, letras da fachada |
| `--sky` | `#DCEBFA` | campo claro (céu do muro pintado) |
| `--grass` | `#4FA33A` | só no rodapé do muro / detalhe |
| `--wa` | `#25D366` | só o botão flutuante do WhatsApp |

Cada painel tem uma cor e uma tinta. Sem gradiente, sem sombra em repouso, sem linhas finas.

## Tipo

- Display: **Fredoka** 600/700 (arredondada como a logo e a fachada), tracking -0.02em, entrelinha 0.9.
- Texto: **Nunito Sans** 400/700, 18px, entrelinha 1.55.
- Cinco tamanhos: `--t-mega` (nome), `--t-xl` (títulos), `--t-l` (frases), `--t-m` (18px), `--t-s` (15px).

## Forma

- Raio único: 28px nos painéis grandes, botões totalmente redondos.
- Margens externas: 20px celular, 32px desktop.
- Seções separadas por troca de campo de cor, 120–200px de respiro.
- A borda de mel escorrendo (SVG) aparece só na transição da primeira tela e no rodapé.

## Revisão de 09/11/2026 (segunda versão, a que está no ar)

A direção "Loud and flat" foi suavizada a pedido do cliente: escala de texto contida (h1 até 72px, h2 até 46px),
grade com largura máxima de 1240px, imagens retas com proporções fixas (4:3, 4:5, 1:1, 16:9) e cantos de 24px.

**Fotos.** A fachada, a logo e os logos Positivo/CCAA são da escola. As fotos de atividades e ambientes em
`img/fotos/` são **ilustrativas, geradas por IA no estilo banco de imagens** (Higgsfield, GPT Image), sem logo
nem fachada de outras escolas. O rodapé avisa "Fotos de atividades ilustrativas". Para trocar por foto real, substitua o
arquivo em `img/fotos/` mantendo o mesmo nome (WebP, por volta de 1200px de largura) e as proporções:
quadrados na galeria, 4:3 nos cursos e aulas extras, 4:5 nos espaços.

As fotos antigas (baixa resolução) estão em `../fotos-antigas-baixa-qualidade/`.

**Partes interativas:** "Aberto agora" (horário de Brasília), abas dos cursos, "Um dia no Cantinho" (arrastar a abelha),
galeria que amplia a foto, carrossel dos espaços com setas, dúvidas em acordeão e "Monte a matrícula" com mensagem pronta
para o WhatsApp.
