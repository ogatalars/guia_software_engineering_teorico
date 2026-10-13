---
title: "2. Modularidade"
description: "Como medir se um código está bem dividido em módulos: coesão, acoplamento aferente e eferente, abstração, instabilidade, distância da sequência principal e conascência."
tags: [fundamentals-software-architecture, arquitetura, coesão, acoplamento, conascência]
---

# 2. Modularidade

> [!NOTE] Em uma frase
> Dividir o código em módulos só ajuda se cada módulo junta coisas que mudam juntas e depende pouco dos outros, e isso dá para medir em vez de discutir no gosto.

## Por que isso importa

Pense em um sistema de e-commerce com uma classe `PedidoUtils` de 3 mil linhas. Ela calcula frete, formata nota fiscal, valida CPF e manda e-mail de confirmação. Toda alteração de frete faz o time de notas fiscais rodar a bateria de testes inteira, e duas pessoas mexendo em assuntos diferentes vivem em conflito de merge. Ninguém discorda que "está ruim", mas na hora de priorizar a refatoração a conversa vira opinião contra opinião.

O capítulo 3 do livro dá vocabulário e números para essa conversa. Modularidade, aqui, é a organização lógica do código em grupos relacionados (pacotes, namespaces, bibliotecas). Ela é a base de tudo que vem depois: estilos de arquitetura são, no fundo, jeitos diferentes de decidir onde ficam as fronteiras entre módulos.

## O que você precisa saber antes

- [Página 1](01-pensamento-arquitetural.md): a ideia de que toda escolha é trade-off.
- [Acoplamento e coesão](../../glossario.md#acoplamento-e-coesão): a definição curta está no glossário; aqui ela ganha medidas.
- [Dependência (direção da)](../../glossario.md#dependência-direção-da): quando A importa B, A depende de B.

## As ideias centrais

### Coesão: o quanto as partes de um módulo pertencem juntas

Coesão é o grau em que os elementos de um módulo deveriam estar ali. O livro apresenta uma escala de tipos, do melhor para o pior:

- **Funcional**: tudo no módulo serve a uma única função bem definida (um módulo que só calcula frete).
- **Sequencial**: a saída de uma parte é a entrada da próxima.
- **Comunicacional**: as partes trabalham sobre os mesmos dados (ler e atualizar o cadastro do cliente).
- **Procedural**: as partes precisam rodar em uma certa ordem.
- **Temporal**: as partes estão juntas porque rodam no mesmo momento (tudo que acontece na inicialização).
- **Lógica**: as partes fazem coisas "parecidas", mas sem relação real. `StringUtils` é o exemplo típico.
- **Coincidental**: as partes estão juntas por acaso. É a nossa `PedidoUtils`.

Para medir, o livro cita a métrica **LCOM** (*Lack of Cohesion in Methods*, falta de coesão nos métodos). A intuição: se os métodos de uma classe usam conjuntos de campos que não se cruzam, a classe é na verdade duas ou três classes coladas. Um valor alto indica baixa coesão. O livro avisa que a métrica só enxerga a estrutura, não o significado: ela não sabe se faz sentido de negócio juntar duas coisas.

### Acoplamento: aferente, eferente e as métricas derivadas

O livro usa duas contagens propostas por Edward Yourdon e Larry Constantine:

- **Acoplamento aferente (Ca)**: quantos módulos de fora dependem deste. É o "quantos me usam".
- **Acoplamento eferente (Ce)**: de quantos módulos de fora este depende. É o "quantos eu uso".

A partir delas, Robert C. Martin definiu métricas que o livro adota:

- **Abstração (A)**: proporção de elementos abstratos (interfaces, classes abstratas) sobre o total do módulo. Vai de 0 (tudo concreto) a 1 (tudo abstrato).
- **Instabilidade (I) = Ce / (Ce + Ca)**. Vai de 0 a 1. Um módulo com I perto de 1 depende de muita coisa e quase ninguém depende dele, então tende a quebrar quando algo muda em volta. Com I perto de 0, muita gente depende dele, então mudar é caro.
- **Distância da sequência principal (D) = |A + I − 1|**. A "sequência principal" é a linha ideal em que abstração e instabilidade se equilibram.

```mermaid
flowchart LR
    Z1["Zona de dor: concreto e muito usado (A baixo, I baixo)"] --- SP["Sequência principal: A + I = 1"]
    SP --- Z2["Zona de inutilidade: abstrato e pouco usado (A alto, I alto)"]
```

Longe da linha há duas zonas ruins. Na **zona de dor**, o módulo é concreto e todo mundo depende dele: qualquer mudança espalha quebras (pense em uma classe de utilidades usada em 200 lugares). Na **zona de inutilidade**, o módulo é tão abstrato que quase ninguém o usa: interfaces criadas "para o futuro" que nunca ganharam uma segunda implementação.

Exemplo numérico: um módulo `pagamentos` com 2 dependências de saída (Ce = 2), 8 módulos dependendo dele (Ca = 8) e nenhuma interface (A = 0) tem I = 2/10 = 0,2 e D = |0 + 0,2 − 1| = 0,8. Está perto da zona de dor. A correção típica é extrair interfaces para que os 8 consumidores dependam de um contrato estável, e não da implementação.

### Conascência: um vocabulário mais fino para acoplamento

Dizer "esses dois módulos estão acoplados" é vago. Meilir Page-Jones propôs em 1996 o conceito de **conascência**: dois componentes são conascentes se uma mudança em um exige mudança no outro para o sistema continuar correto. O ganho é poder dizer **que tipo** de acoplamento existe.

**Conascência estática** (visível lendo o código), da mais fraca para a mais forte:

- **De nome**: os dois concordam com o nome de algo (chamar `calcularFrete()`). É a mais fraca e inevitável; IDEs renomeiam isso automaticamente.
- **De tipo**: concordam com o tipo de uma variável ou parâmetro.
- **De significado (ou convenção)**: concordam com o que um valor quer dizer. Exemplo: em vários lugares, `status == 3` significa "cancelado". Trocar por uma constante nomeada a transforma em conascência de nome, mais fraca.
- **De posição**: concordam com a ordem de valores. `criarUsuario("Ana", "Silva", "ana@x.com")`: inverter nome e e-mail compila e quebra em produção.
- **De algoritmo**: concordam com um algoritmo. O cliente e o servidor precisam calcular o mesmo hash para validar uma assinatura.

**Conascência dinâmica** (só aparece em execução), também da mais fraca para a mais forte:

- **De execução**: a ordem das chamadas importa (configurar o e-mail antes de enviar).
- **De tempo (*timing*)**: o momento importa; a origem clássica de condições de corrida.
- **De valores**: vários valores precisam mudar juntos (os cantos de um retângulo, ou réplicas que precisam concordar).
- **De identidade**: dois componentes precisam referenciar a mesma instância.

Além do tipo, a conascência tem três propriedades: **força** (quão difícil é refatorar aquele tipo), **localidade** (quão próximos os componentes estão; acoplamento forte dentro de uma mesma classe é tolerável, entre serviços não é) e **grau** (quantos componentes são afetados).

As regras práticas, de Page-Jones e de Jim Weirich, se resumem a: quebre o sistema em partes encapsuladas, minimize a conascência que atravessa as fronteiras, deixe a conascência forte só dentro de uma mesma parte, e converta formas fortes em formas fracas sempre que puder.

### De volta à arquitetura

Estas métricas nasceram para código orientado a objetos, mas o livro as usa como ponte. Em uma arquitetura distribuída, conascência de algoritmo entre dois serviços (os dois precisam validar CPF exatamente igual) é muito mais cara do que dentro de um processo, porque mudar exige implantar os dois juntos. É esse raciocínio que gera, na [página 3](03-caracteristicas-arquiteturais.md), o conceito de quantum arquitetural.

## Onde isso aparece no mundo real

- **Ferramentas de análise estática**: SonarQube, JDepend (Java) e similares calculam acoplamento, instabilidade e ciclos de dependência. Muitos times as rodam no CI (integração contínua, o processo que roda testes a cada mudança) e falham o build se uma métrica passa de um limite.
- **Contratos de API com parâmetros posicionais**: o caso de `criarUsuario(nome, sobrenome, email)` é tão comum que linguagens adotaram parâmetros nomeados (Python, Kotlin) justamente para trocar conascência de posição por conascência de nome.
- **Bibliotecas compartilhadas entre microsserviços**: uma biblioteca `common` usada por 30 serviços é um módulo na zona de dor em escala de empresa. Mudar uma linha nela força 30 deploys.

## Erros comuns de quem está aprendendo

- **Achar que acoplamento zero é a meta.** Sistema sem acoplamento não faz nada. A meta é acoplamento fraco entre partes e forte dentro de cada parte.
- **Usar métricas como alvo.** Uma métrica de coesão boa não garante um design que faz sentido para o negócio. O livro trata as métricas como sinal para investigar, não como nota.
- **Criar abstração para fugir da zona de dor sem necessidade.** Uma interface com uma única implementação e um só consumidor joga o módulo na zona de inutilidade. Abstraia onde muitos dependem e a implementação pode mudar.
- **Confundir coesão lógica com coesão funcional.** `Utils` agrupa coisas "parecidas", não coisas que mudam juntas.

## Verifique se entendeu

1. Por que uma classe `StringUtils` tem coesão lógica e não funcional? (Veja "Coesão".)
2. Calcule a instabilidade de um módulo com Ce = 6 e Ca = 2. Ele é fácil ou difícil de mudar sem quebrar os outros? (Veja "Acoplamento".)
3. Como transformar conascência de significado em conascência de nome? Dê um exemplo. (Veja "Conascência".)
4. Por que conascência forte entre dois serviços é pior do que dentro de uma mesma classe? (Veja a propriedade localidade e "De volta à arquitetura".)

## Para ir além

- [Resumo de Dan Lebrero](https://danlebrero.com/2021/11/17/fundamentals-of-software-architecture-summary/): as notas do capítulo 3 listam as métricas de modularidade e os tipos de conascência de forma compacta.
- [Q&A de Edwin Torres, Parte 1](https://dev.to/codesandtags/fundamentals-of-software-architecture-book-part-1-ela): traz as respostas sobre conascência e sobre as métricas de acoplamento do capítulo 3.
- [Clube de leitura no GitHub](https://github.com/melaniebrgr/bookclub-fundamentals-software-architecture): a pasta `summaries/` tem o resumo do capítulo 3 feito pelo grupo.

---
Anterior: [1. Pensamento arquitetural](01-pensamento-arquitetural.md) · Próximo: [3. Características arquiteturais](03-caracteristicas-arquiteturais.md) · Voltar ao livro: [Guia de leitura](index.md)
