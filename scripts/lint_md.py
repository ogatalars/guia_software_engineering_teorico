#!/usr/bin/env python3
"""Falha se o conteúdo usar sintaxe que o GitHub não renderiza (ver STYLE.md §2)."""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "content"
CALLOUTS = {"NOTE", "TIP", "IMPORTANT", "WARNING", "CAUTION"}
errors = []

for f in sorted(ROOT.rglob("*.md")):
    text = f.read_text(encoding="utf-8")
    rel = f.relative_to(ROOT.parent)
    for n, line in enumerate(text.splitlines(), 1):
        if "[[" in line:
            errors.append(f"{rel}:{n}: wikilink/embed. Use [texto](caminho.md).")
        m = re.match(r"^\s*>\s*\[!(\w+)\]", line)
        if m and m.group(1) not in CALLOUTS:
            errors.append(f"{rel}:{n}: callout [!{m.group(1)}] fora de {sorted(CALLOUTS)} (maiúsculas).")
    for link in re.findall(r"\]\(([^)#:\s]+\.md)(?:#[^)]*)?\)", text):
        if not (f.parent / link).exists():
            errors.append(f"{rel}: link quebrado -> {link}")

print("\n".join(errors) if errors else "lint-md: ok")
sys.exit(1 if errors else 0)
