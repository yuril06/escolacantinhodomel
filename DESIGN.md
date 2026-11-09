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

## Revisão de 09/11/2026: espaços para fotos

As fotos antigas (baixa resolução) saíram do site e estão em `../fotos-antigas-baixa-qualidade/`.
No lugar de cada uma há um espaço reservado branco (`.ph`), com o nome da foto que deve entrar ali.

Para colocar uma foto nova, troque o bloco inteiro:

```html
<div class="ph ph-45" role="img" aria-label="..."> ... </div>
```

por uma imagem com as **mesmas classes** mais `ph-photo` (`ph-45` = 4:5, `ph-32` = 3:2, `ph-fill` = preenche o espaço):

```html
<img class="ph ph-45 ph-photo" src="img/nova-foto.jpg" alt="Descrição da foto" width="1200" height="1500" loading="lazy">
```

Use fotos com no mínimo 1200px no lado maior.

**Parte viva, agora são três:** "Aberto agora" no topo (horário de Brasília), "Um dia no Cantinho" (arrastar a abelha
de 6h30 a 19h) e "Monte a matrícula" (chips de idade e período, nome opcional, mensagem pronta para o WhatsApp).
