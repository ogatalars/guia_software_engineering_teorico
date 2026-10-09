---
title: "Guia Teórico de Software Engineering"
description: "O que é este guia, para quem é, as três áreas, as trilhas de estudo e como usar o site ou o repositório."
tags: [inicio]
---

# Guia Teórico de Software Engineering

> [!NOTE] Em uma frase
> Um mapa de leitura comentado dos livros que formam a base de um software engineer hoje, escrito para quem estuda sozinho e não quer pular etapas.

## Para quem é

Para quem já programa, mesmo que pouco, e sente que falta a teoria por trás: por que sistemas caem quando crescem, por que código vira bagunça, o que de fato acontece quando se "treina um modelo". Não assumimos que você leu nenhum dos livros. Cada termo técnico é definido na primeira vez em que aparece e reunido no [glossário](glossario.md).

## O que este guia faz e o que não faz

Este guia **explica e orienta**. Para cada livro ele diz o que o livro ensina, por que isso importa, como ler, o que levar de cada capítulo e onde errar é comum. Ele **não substitui o livro**: não reproduz texto, figuras nem exercícios. Para cada livro há uma página de [fontes públicas](referencias/fontes-completas.md), verificadas uma a uma, com resumos de terceiros, material oficial gratuito e artigos que aprofundam.

## Como estudar

Comece por [Como estudar](como-estudar.md): o método para ler livro técnico sem travar, quanto tempo reservar e como usar as perguntas de verificação. Depois escolha uma [trilha](trilhas/index.md).

## As três áreas

```mermaid
flowchart LR
  A[Arquitetura de Software] --> SD[System Design]
  SD --> IA[IA em produção]
  A -.-> IA
```

### [System Design](system-design/index.md)
Como construir sistemas que aguentam escala, falhas e mudança. Dois livros: *Designing Data-Intensive Applications* (o fundamento) e *System Design Interview* (a prática de projetar).

### [Arquitetura de Software](arquitetura/index.md)
Como organizar código e decisões para que o sistema continue mudável por anos. Três livros: *Clean Architecture*, *Domain-Driven Design* e *Fundamentals of Software Architecture*.

### [Inteligência Artificial](ia/index.md)
O que há por baixo de um modelo e o que é preciso para colocá-lo em produção. Dois livros: *Deep Learning* e *Designing Machine Learning Systems*.

## Trilhas

As [trilhas](trilhas/index.md) cruzam os livros em ordens pensadas para um objetivo: fundamentos de backend, sistemas distribuídos, ML em produção.

## Dois jeitos de ler

No **site**, você tem busca, grafo de notas e modo escuro. No **GitHub**, cada página é um arquivo markdown que renderiza no próprio repositório, inclusive os diagramas. O conteúdo é o mesmo.

## Licença

Conteúdo sob CC BY-SA 4.0. Pode copiar e adaptar, citando a origem e mantendo a licença.
