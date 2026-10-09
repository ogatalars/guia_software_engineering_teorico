---
title: "Glossário"
description: "Os termos que atravessam os sete livros, definidos uma vez e do mesmo jeito. Cada entrada tem até três frases e aponta para a página que explica a fundo."
tags: [glossario, referencia]
---

# Glossário

Este é o contrato de vocabulário do guia. Toda página define um termo na primeira vez em que ele aparece e depois linka para cá. Se dois lugares definem o mesmo termo de jeitos diferentes, está errado e precisa ser corrigido. Entradas em ordem alfabética.

## ACID

Sigla para as quatro garantias que um banco de dados relacional promete a uma transação: Atomicidade (tudo ou nada), Consistência (as regras do banco continuam válidas), Isolamento (transações simultâneas não enxergam o meio do caminho umas das outras) e Durabilidade (o que foi confirmado não se perde). Na prática, o "I" é o mais negociado: a maioria dos bancos oferece níveis de isolamento mais fracos por padrão para ganhar velocidade. Aprofunda em DDIA, capítulo 7.

## Acoplamento e coesão

Acoplamento é o quanto uma parte do código depende de outra: mude uma, e quantas outras quebram? Coesão é o quanto as coisas dentro de uma mesma parte pertencem de fato umas às outras. O objetivo clássico é baixo acoplamento entre módulos e alta coesão dentro de cada um. Aprofunda em Clean Architecture (princípios de componentes) e Fundamentals of Software Architecture (modularidade).

## Agregado

No DDD, um grupo de objetos do domínio tratado como uma unidade para fins de mudança e consistência, com um objeto raiz por onde todo acesso passa. A regra prática: uma transação muda um agregado só. Pedido e seus itens são o exemplo clássico; o pedido é a raiz. Aprofunda em DDD, Parte II.

## BASE

Contraponto informal a ACID para sistemas distribuídos: Basicamente disponível, estado Suave (pode estar temporariamente inconsistente) e Eventualmente consistente. Não é um padrão formal, é um modo de dizer "preferimos responder sempre a responder sempre certo". Aprofunda em DDIA, capítulos 5 e 9.

## Backpressure

Mecanismo pelo qual um consumidor lento avisa o produtor para desacelerar, em vez de deixar a fila crescer até estourar a memória. Sem ele, um sistema saudável sob carga normal cai de uma vez quando a carga sobe. Aparece em filas, streams e qualquer pipeline em que uma etapa é mais lenta que a anterior. Aprofunda em DDIA, capítulo 11.

## Batch vs streaming

Processamento em batch trabalha sobre um conjunto fechado de dados de uma vez (o relatório da noite); streaming trabalha sobre eventos conforme chegam, sem fim definido. A diferença não é só velocidade: muda como se lida com dados atrasados, com reprocessamento e com falhas. Aprofunda em DDIA, capítulos 10 e 11, e em Designing ML Systems, capítulo 3.

## Bounded context

No DDD, a fronteira dentro da qual um modelo de domínio tem um significado único e consistente. "Cliente" pode ser uma coisa no contexto de vendas e outra no de suporte, e isso é esperado; o erro é tentar um modelo único para a empresa inteira. É a ideia central do design estratégico. Aprofunda em DDD, Parte IV.

## Cache

Cópia de um dado guardada em um lugar mais rápido de acessar do que a origem, para evitar refazer trabalho. O problema nunca é guardar, é saber quando a cópia ficou velha (invalidação). Aparece em todos os níveis, do processador à CDN. Aprofunda em System Design Interview, capítulo 1, e DDIA, capítulo 3.

## Camada

Agrupamento horizontal de código por responsabilidade técnica: interface, aplicação, domínio, infraestrutura. Em arquiteturas em camadas a regra é que cada camada só conhece a de baixo; na Clean Architecture a regra vira "só conhece a de dentro". Aprofunda em Clean Architecture, Parte V, e DDD, capítulo 4.

## CAP

Teorema que diz que, quando a rede particiona (nós deixam de se falar), um sistema distribuído precisa escolher entre continuar respondendo (disponibilidade) e continuar respondendo certo (consistência). É menos útil do que parece: partições são raras, e as escolhas interessantes acontecem fora delas. Aprofunda em DDIA, capítulo 9.

## Caso de uso

Na Clean Architecture, uma operação do sistema descrita do ponto de vista de quem a usa ("fazer pedido", "cancelar assinatura"), implementada sem depender de interface, banco ou framework. É a camada que orquestra as entidades. Aprofunda em Clean Architecture, Parte V.

## Consistência (forte e eventual)

Consistência forte: depois que uma escrita é confirmada, toda leitura em qualquer lugar vê o novo valor. Consistência eventual: as réplicas vão convergir para o mesmo valor, mas por um tempo leituras diferentes podem ver valores diferentes. A palavra "consistência" em ACID significa outra coisa (regras do banco), o que confunde todo mundo. Aprofunda em DDIA, capítulos 5 e 9.

## Data drift

Mudança na distribuição dos dados que um modelo recebe em produção em relação aos dados com que foi treinado. O modelo não "quebra", só começa a errar mais sem avisar. Detectar e reagir a isso é o trabalho central de monitorar ML. Aprofunda em Designing ML Systems, capítulo 8.

## Dataset e divisão treino / validação / teste

Dataset é o conjunto de exemplos usado para construir um modelo. Divide-se em treino (o modelo aprende aqui), validação (para escolher hiperparâmetros e decidir quando parar) e teste (usado uma vez, no fim, para estimar o desempenho real). Misturar as três é a forma mais comum de acreditar em um modelo que não funciona. Aprofunda em Deep Learning, capítulo 5, e Designing ML Systems, capítulo 4.

## Dependência (direção da)

Quando o módulo A importa, chama ou conhece o módulo B, A depende de B: mudanças em B podem quebrar A. Arquitetura é, em boa parte, decidir para que lado as dependências apontam. A regra da Clean Architecture é que apontem para o centro (regras de negócio), nunca para fora (frameworks, banco, UI). Aprofunda em Clean Architecture, Parte V.

## Disponibilidade

Fração do tempo em que o sistema responde corretamente, em geral expressa em "noves": 99,9% significa cerca de 8h45 fora do ar por ano. Cada nove a mais custa muito mais do que o anterior. Aprofunda em DDIA, capítulo 1, e System Design Interview, capítulo 2.

## Entidade

Objeto do domínio que tem identidade própria ao longo do tempo: dois clientes com o mesmo nome continuam sendo dois clientes. Contrasta com value object. Aprofunda em DDD, capítulo 5, e Clean Architecture, Parte V.

## Feature

Em ML, uma variável de entrada do modelo, derivada dos dados brutos: idade, número de compras nos últimos 30 dias, comprimento do texto. Engenharia de features é transformar dados brutos em entradas que o modelo consegue usar bem. Aprofunda em Designing ML Systems, capítulo 5.

## Fila e mensageria

Componente que recebe mensagens de quem produz e as entrega a quem consome, desacoplando os dois no tempo: o produtor não espera o consumidor. Permite absorver picos e tolerar consumidores fora do ar. Kafka, RabbitMQ e SQS são exemplos com garantias diferentes. Aprofunda em DDIA, capítulo 11, e System Design Interview, capítulo 10.

## Fronteira arquitetural

Linha que separa partes do sistema que mudam por motivos diferentes ou em ritmos diferentes, de modo que uma mudança de um lado não force mudança do outro. Atravessar a fronteira custa (interfaces, conversão de dados), então ela só vale onde a separação paga esse custo. Aprofunda em Clean Architecture, Parte V.

## Gradiente e descida do gradiente

Gradiente é o vetor que aponta na direção em que uma função cresce mais rápido. Descida do gradiente é o algoritmo que ajusta os parâmetros de um modelo um pouquinho na direção contrária, repetidamente, para reduzir o erro. É o motor de quase todo treinamento em deep learning. Aprofunda em Deep Learning, capítulos 4 e 8.

## Idempotência

Propriedade de uma operação que produz o mesmo resultado se executada uma ou várias vezes. "Definir saldo como 100" é idempotente; "somar 10 ao saldo" não é. Importa porque, em sistemas distribuídos, mensagens se repetem, e um consumidor idempotente pode simplesmente processar de novo. Aprofunda em DDIA, capítulos 11 e 12.

## Label

Em ML supervisionado, a resposta certa associada a cada exemplo de treino: a categoria da imagem, o preço real da casa. Obter labels confiáveis costuma ser mais caro e mais difícil do que treinar o modelo. Aprofunda em Designing ML Systems, capítulo 4.

## Latência e throughput

Latência é quanto tempo uma requisição leva do pedido à resposta. Throughput é quantas requisições o sistema processa por unidade de tempo. Melhorar um costuma piorar o outro: processar em lotes grandes aumenta o throughput e a latência ao mesmo tempo. Aprofunda em DDIA, capítulo 1.

## Linguagem ubíqua

No DDD, o vocabulário compartilhado entre desenvolvedores e especialistas do negócio, usado igual na conversa, nos diagramas e no código. Se o negócio diz "apólice" e o código diz "contrato", alguém vai traduzir errado em algum momento. Aprofunda em DDD, capítulo 2.

## Loss (função de perda)

Número que mede quão errado o modelo está em um exemplo ou lote; treinar é minimizar esse número. A escolha da loss define o que o modelo está de fato otimizando, que nem sempre é o que você queria. Aprofunda em Deep Learning, capítulos 5 e 6.

## Modelo de domínio

Representação, em código e em diagramas, dos conceitos e regras do negócio que o sistema trata, independente de como são armazenados ou exibidos. É o centro que a Clean Architecture protege e o que o DDD ensina a construir. Aprofunda em DDD, Parte I.

## Observabilidade

Capacidade de entender o que está acontecendo dentro de um sistema a partir do que ele emite: logs, métricas e traces. Difere de monitoramento, que checa perguntas pré-definidas; observabilidade permite fazer perguntas novas. Aprofunda em Designing ML Systems, capítulo 8, e Fundamentals of Software Architecture (características arquiteturais).

## Overfitting

Quando um modelo aprende os detalhes e o ruído dos dados de treino em vez do padrão geral, e por isso vai bem no treino e mal em dados novos. É o motivo de existir o conjunto de validação e as técnicas de regularização. Aprofunda em Deep Learning, capítulos 5 e 7.

## p50, p99 (percentis de latência)

p99 de 300 ms significa que 99% das requisições respondem em até 300 ms e 1% demora mais. Médias escondem exatamente os usuários que estão sofrendo; percentis altos mostram. Aprofunda em DDIA, capítulo 1.

## Particionamento (sharding)

Dividir um conjunto de dados grande em pedaços menores, cada um em uma máquina diferente, para que nenhuma máquina precise guardar ou servir tudo. O problema difícil é escolher a chave de partição: errar cria "partições quentes" que concentram a carga. Aprofunda em DDIA, capítulo 6, e System Design Interview, capítulo 5.

## Pipeline

Sequência de etapas em que a saída de uma é a entrada da próxima: ingestão, limpeza, transformação, treino, avaliação. Em dados e em ML, quase tudo é pipeline, e a maioria dos problemas em produção está nas emendas entre etapas. Aprofunda em DDIA, capítulo 10, e Designing ML Systems, capítulos 3 e 10.

## Replicação

Manter cópias do mesmo dado em várias máquinas, para tolerar falhas e servir leituras mais perto do usuário. A dificuldade toda é manter as cópias de acordo quando há escritas: líder único, múltiplos líderes ou sem líder são as três famílias de solução. Aprofunda em DDIA, capítulo 5.

## SLO

Service Level Objective: a meta numérica de confiabilidade que um serviço promete, como "99,9% das requisições em menos de 500 ms no mês". Define o que é "bom o suficiente" e, por consequência, quanto risco a equipe pode assumir. Aprofunda em Fundamentals of Software Architecture (características arquiteturais) e Designing ML Systems, capítulo 7.

## Stateless e stateful

Um componente stateless não guarda nada entre requisições; qualquer instância pode atender qualquer pedido, o que facilita escalar e substituir. Um componente stateful guarda estado (sessão, dados), e por isso é mais difícil de replicar e mover. A estratégia comum é empurrar o estado para onde ele é bem cuidado (banco, cache) e deixar o resto stateless. Aprofunda em System Design Interview, capítulo 1.

## Train-serving skew

Diferença entre como as features são calculadas no treino e como são calculadas em produção, fazendo o modelo receber entradas que nunca viu. É uma das causas mais comuns e mais silenciosas de modelo bom offline e ruim online. Aprofunda em Designing ML Systems, capítulos 5 e 8.

## Value object

Objeto do domínio definido só pelos seus atributos, sem identidade: duas quantias de "R$ 10,00" são iguais e intercambiáveis. Deve ser imutável. Modelar como value object o que não precisa de identidade simplifica muito o código. Aprofunda em DDD, capítulo 5.
