# Contribuindo

## Rodar localmente

```bash
npm ci
npx quartz build --serve   # http://localhost:8080
python3 scripts/lint_md.py
```

## Onde fica cada coisa

- `content/pt-br/` é a fonte da verdade. `content/en/` é tradução.
- Um livro = uma pasta com `index.md` (guia de leitura), um `.md` por capítulo/parte e `fontes.md`.
- `STYLE.md` tem os templates e o checklist. Leia antes de escrever.
- Não edite `quartz/`. Configuração do site fica em `quartz.config.yaml`.

## Pull requests

Um PR por livro ou por página. O CI roda o lint e o build; o preview do markdown no próprio GitHub serve para conferir Mermaid e callouts. Antes de pedir revisão, passe pelo checklist do `STYLE.md` §6.
