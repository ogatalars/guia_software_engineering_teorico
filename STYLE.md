# Guia de estilo e templates

Este arquivo é o contrato de quem escreve conteúdo. Toda página em `content/` segue o que está aqui. O lint (`scripts/lint_md.py`) checa a parte mecânica; a parte pedagógica é checada em revisão.

## 1. Princípios de escrita

1. **Jargão definido na primeira vez**, em uma frase, no mesmo parágrafo. Depois, link para o [glossário](content/pt-br/glossario.md).
2. **Não assumir conhecimento prévio.** Se a página depende de um conceito, ou explica antes, ou linka a página que explica dizendo em uma frase o que ela dá.
3. **O porquê antes do quê.** Toda técnica aparece como resposta a um problema concreto.
4. **Caminho inteiro.** Não pular o passo "óbvio".
5. **Concreto antes de abstrato.** Exemplo real (sistema conhecido, incidente público, situação do dia a dia de um dev) antes da definição geral.
6. **Dizer quando há controvérsia ou quando o livro envelheceu.**
7. **Explicação original.** Nunca reproduzir texto, figuras ou exercícios do livro. Máximo 2 frases literais por página, com atribuição. Resumos de terceiros são fonte de consulta, não de cópia.

## 2. Compatibilidade GitHub × Quartz

O conteúdo precisa renderizar igual no site e navegando o repositório no GitHub.

| Recurso | Regra |
|---|---|
| Links internos | Sempre `[texto](caminho/relativo.md)`. Caminho relativo ao arquivo atual. |
| Wikilinks `[[nota]]`, embeds `![[nota]]` | **Proibidos.** GitHub mostra texto cru. |
| Diagramas | Bloco ```` ```mermaid ````. Só `flowchart`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`. |
| Callouts | Só `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`, em maiúsculas. |
| Frontmatter | `title`, `description`, `tags`. Curto. `description` sempre entre aspas duplas (dois-pontos no texto quebram o YAML). GitHub mostra como tabela, aceitável. |
| Imagens | Permitidas em `assets/` ao lado do `.md`, só próprias ou com licença aberta e crédito. Nunca figura de livro. |
| LaTeX `$...$` | Só na área de IA. |
| Dataview, Bases, Canvas | **Proibidos.** |

## 3. Template de página de capítulo/parte

Todas as seções, nesta ordem. Seção vazia não é permitida; se não há o que dizer, a página não deveria existir. Alvo: 1.200–2.000 palavras. O leitor pode nunca abrir o livro: "As ideias centrais" precisa entregar o conteúdo, não só apontar para ele.

```markdown
---
title: "<número>. <nome do capítulo em português>"
description: <uma frase: o que a pessoa vai entender ao terminar>
tags: [<livro>, <área>, <2–3 conceitos>]
---

# <número>. <nome>

> [!NOTE] Em uma frase
> <a ideia central do capítulo, sem jargão>

## Por que isso importa
<o problema real que motiva o capítulo; 1–2 parágrafos; um exemplo concreto>

## O que você precisa saber antes
<links para páginas anteriores ou glossário, uma frase cada; ou "Nada além do capítulo anterior">

## As ideias centrais
<2–5 subseções ###, uma por conceito: definição em uma frase, analogia ou exemplo, onde aparece na prática. Pelo menos 1 diagrama Mermaid.>

## Onde isso aparece no mundo real
<1–3 exemplos: sistemas conhecidos, incidentes públicos, decisões comuns de projeto>

## Erros comuns de quem está aprendendo
<2–4 mal-entendidos frequentes e a correção de cada um>

## Verifique se entendeu
<3–5 perguntas abertas, cada uma apontando a seção que responde>

## Para ir além
<links do fontes.md do livro relevantes a ESTE capítulo, uma frase dizendo o que tem lá>

---
Anterior: [..](..) · Próximo: [..](..) · Voltar ao livro: [..](index.md)
```

## 4. Template de `index.md` de livro

```markdown
---
title: "<Título do livro> — guia de leitura"
description: <uma frase>
tags: [<livro>, <área>, guia-de-leitura]
---

# <Título do livro> — guia de leitura

> [!NOTE] Em uma frase
> <o que o livro ensina>

## Para quem é e quando ler
## O que o livro NÃO é
## Como o livro está organizado
<Mermaid: mapa das partes/capítulos e dependências>
## Como ler
<ordem sugerida, o que pular na 1ª leitura, ritmo>
## O que você leva ao terminar
## Capítulos
<lista linkada, uma frase por capítulo>
## Fontes públicas para acompanhar
<link para fontes.md>
```

## 5. Glossário

Um termo = uma entrada `## termo` com definição em até 3 frases + link para a página que explica a fundo. Páginas linkam `glossario.md#termo` na primeira menção após a definição inline. Termo definido em dois lugares de formas diferentes é conflito a resolver.

## 6. Checklist de aceite por página

- [ ] Segue o template §3 com todas as seções preenchidas.
- [ ] `python3 scripts/lint_md.py` passa.
- [ ] Todo jargão novo definido inline na primeira vez e linkado ao glossário.
- [ ] Pelo menos 1 Mermaid que renderiza no preview do GitHub.
- [ ] Nenhum trecho com mais de 2 frases literais de livro; nenhuma figura de livro.
- [ ] "Para ir além" usa só links do `fontes.md` do livro ou fontes oficiais.
- [ ] 1.200–2.000 palavras.
- [ ] Links anterior/próximo/index funcionam.
