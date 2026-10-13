---
title: "Arquitetura de Software"
description: "Como organizar código e decisões para que o sistema continue mudável por anos. Três livros complementares."
tags: [arquitetura]
---

# Arquitetura de Software

Arquitetura é o conjunto de decisões que são caras de mudar depois: onde ficam as fronteiras, de que lado cada dependência aponta, qual estilo estrutural o sistema segue.

## Livros

- **[Clean Architecture](clean-architecture/index.md)** (Robert C. Martin) — o princípio: dependências apontam para dentro, para as regras de negócio, nunca para frameworks e bancos.
- **[Domain-Driven Design](ddd/index.md)** (Eric Evans) — o conteúdo do centro: como modelar o domínio do negócio em código e como dividir um sistema grande em contextos.
- **[Fundamentals of Software Architecture](fundamentals-software-architecture/index.md)** (Mark Richards & Neal Ford) — o mapa: características arquiteturais, estilos (monolito, microsserviços, event-driven) e como registrar decisões.

Ordem sugerida: Clean Architecture → DDD → Fundamentals. No guia principal, esta área corresponde aos módulos 1 a 4 de [Fundamentos de Software Engineering](../fundamentos/index.md).
