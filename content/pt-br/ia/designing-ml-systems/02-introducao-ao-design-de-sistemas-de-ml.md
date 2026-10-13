---
title: "2. Introdução ao design de sistemas de ML"
description: "Como transformar um objetivo de negócio em um problema de ML, quais requisitos um sistema precisa cumprir e por que o desenvolvimento é um ciclo, não uma linha reta."
tags: [designing-ml-systems, ia, objetivos-de-negocio, framing, requisitos]
---

# 2. Introdução ao design de sistemas de ML

> [!NOTE] Em uma frase
> Todo sistema de ML começa por um objetivo de negócio, que precisa ser traduzido em um problema de ML bem formulado, com requisitos claros, e construído em ciclos que nunca terminam de verdade.

## Por que isso importa

Uma equipe passa três meses melhorando a acurácia de um modelo que prevê se um cliente vai clicar em um anúncio, de 92% para 94%. Na reunião de resultados, a diretora pergunta: "e quanto isso aumentou a receita?". Ninguém sabe. Talvez nada, talvez até tenha diminuído, porque o modelo passou a favorecer anúncios baratos em que as pessoas clicam muito.

Essa cena é comum e é o assunto do capítulo. Empresas não se importam com métricas de ML; importam-se com receita, custo, retenção, satisfação. Uma métrica de ML só vale algo se mover uma métrica de negócio. E, mesmo com o objetivo certo, a forma de formular o problema (o que o modelo recebe, o que devolve, o que otimiza) decide se ele vai ser fácil ou impossível de resolver.

## O que você precisa saber antes

- [Capítulo 1](01-visao-geral-de-sistemas-de-ml.md): quando usar ML e por que o modelo é só uma peça do sistema.
- [Loss (função de perda)](../../glossario.md#loss-função-de-perda): o número que o treino tenta minimizar.
- [Label](../../glossario.md#label): a resposta certa de cada exemplo.

## As ideias centrais

### Do objetivo de negócio ao objetivo de ML

O primeiro passo é escrever, em termos de negócio, o que o projeto deve mudar: "reduzir fraudes em 20%", "aumentar o tempo assistido". Depois, traduzir isso em algo que um modelo consegue otimizar: "classificar transações como fraude ou não", "prever a probabilidade de o usuário assistir a um título".

A tradução nunca é perfeita, e é aí que nascem os problemas. A probabilidade de clique é fácil de medir, mas o negócio talvez queira compras, não cliques. Por isso a autora insiste em mapear a relação entre as duas métricas, idealmente com experimentos que mostram que melhorar a métrica de ML melhora a de negócio. A Netflix, por exemplo, publicou uma estimativa de que seu sistema de recomendação economiza cerca de um bilhão de dólares por ano ao reduzir cancelamentos; é esse tipo de ligação que justifica o investimento.

Um aviso honesto do livro: o retorno de ML depende da maturidade da empresa. Quem já tem dados organizados, infraestrutura e outros modelos em produção colhe resultados muito mais rápido do que quem está começando do zero.

### Os quatro requisitos

Antes de construir, defina o que é "bom". O livro foca em quatro requisitos gerais:

- **Confiabilidade**: o sistema continua funcionando corretamente diante de problemas. Em ML há uma armadilha: o sistema pode falhar **em silêncio**. Um serviço web quebrado devolve erro 500; um modelo quebrado continua devolvendo previsões, só que erradas, e ninguém percebe.
- **Escalabilidade**: aguentar crescimento em três dimensões: complexidade do modelo, volume de requisições e número de modelos. Uma empresa começa com um modelo e, dois anos depois, tem centenas. Escalar inclui subir e descer recursos automaticamente (autoscaling) e gerenciar muitos modelos.
- **Manutenibilidade**: várias pessoas com formações diferentes (engenheiros de ML, de dados, de software, especialistas do domínio) trabalham no mesmo sistema. Código versionado, documentado e reprodutível permite que alguém que não escreveu o sistema o conserte.
- **Adaptabilidade**: os dados e o negócio mudam. O sistema precisa conseguir descobrir oportunidades de melhoria e ser atualizado sem parar tudo.

### Um processo iterativo

Desenvolver um sistema de ML não é uma sequência "coleta, treino, deploy, fim". É um ciclo com seis etapas que se realimentam:

```mermaid
flowchart LR
    A["1 · Escopo do projeto"] --> B["2 · Engenharia de dados"]
    B --> C["3 · Desenvolvimento do modelo"]
    C --> D["4 · Deploy"]
    D --> E["5 · Monitoramento e aprendizado contínuo"]
    E --> F["6 · Análise de negócio"]
    F --> A
    C -. "precisa de mais dados" .-> B
    E -. "modelo degradou" .-> C
    D -. "latência ruim" .-> C
```

Um exemplo concreto de como o ciclo gira: você treina um classificador de spam (etapa 3), percebe que faltam exemplos de um tipo novo de golpe e volta à coleta (etapa 2). Depois do deploy (etapa 4), o monitoramento (etapa 5) mostra que a taxa de spam não detectado subiu em uma semana; você retreina. A análise de negócio (etapa 6) mostra que usuários reclamam mais de e-mails legítimos indo para spam do que de spam chegando, e isso muda o próprio objetivo (etapa 1).

### Formular o problema (framing)

Formular é decidir a entrada, a saída e a função objetivo do modelo. O mesmo problema de negócio aceita formulações muito diferentes.

**Tipos de tarefa.** As duas grandes famílias são **classificação** (escolher uma categoria: spam ou não) e **regressão** (prever um número: preço de uma casa). Dentro da classificação:

- **Binária**: duas classes (fraude ou não).
- **Multiclasse**: várias classes, cada exemplo em exatamente uma (qual dígito está na imagem).
- **Multilabel**: cada exemplo pode ter várias classes ao mesmo tempo (um artigo que é sobre tecnologia e sobre economia). É a mais difícil, inclusive para rotular, porque anotadores discordam sobre quantas classes marcar.

Quando o número de classes é muito alto (alta cardinalidade, como milhares de categorias de produto), uma técnica comum é a classificação hierárquica: primeiro decide-se a categoria grande (eletrônicos), depois a pequena (fones de ouvido).

Classificação e regressão também se convertem uma na outra. Prever o preço de uma casa é regressão, mas pode virar classificação se você dividir os preços em faixas. Detectar spam é classificação, mas pode virar regressão se o modelo devolver uma probabilidade de 0 a 1 e você escolher um limiar.

**O exemplo do próximo app.** Suponha que você quer prever qual aplicativo o usuário vai abrir em seguida, entre 100 instalados. Formulado como classificação multiclasse, o modelo recebe as features do usuário e devolve 100 probabilidades. Se o usuário instalar um app novo, a saída muda de tamanho e o modelo precisa ser retreinado. Formulado como regressão, o modelo recebe features do usuário **e do app** e devolve um número entre 0 e 1: a chance de abrir aquele app. Você roda o modelo uma vez por app e escolhe o maior. Um app novo é só mais uma entrada; nada precisa ser retreinado. A segunda formulação é mais trabalhosa de servir, mas muito mais fácil de manter.

**Funções objetivo e o desacoplamento.** A função objetivo (em geral uma [loss](../../glossario.md#loss-função-de-perda)) é o que o modelo de fato otimiza. Quando há mais de um objetivo, a escolha fica delicada. Pense em um feed de notícias que quer **engajamento** (cliques) mas também **qualidade** (nada de spam ou desinformação). Uma opção é treinar um único modelo com uma loss que soma as duas, com pesos. O problema: cada vez que a empresa quiser mudar o equilíbrio entre qualidade e engajamento, precisa retreinar. A alternativa sugerida no livro é **desacoplar**: um modelo prevê qualidade, outro prevê engajamento, e uma regra simples combina as duas notas com pesos ajustáveis. Mudar o peso vira mudança de configuração, não de modelo. Além disso, cada modelo pode ser atualizado no seu ritmo.

### Mente versus dados

O capítulo termina com um debate: o progresso de ML vem de algoritmos mais inteligentes ou de mais dados? Há quem defenda que estrutura e raciocínio embutidos no modelo vão vencer, e há quem aponte que os grandes saltos da última década (AlexNet em visão, BERT e GPT em linguagem) vieram em boa parte de mais dados e mais computação. A autora não fecha a questão, mas registra que ninguém nega a importância dos dados, e por isso boa parte do livro é sobre eles.

## Onde isso aparece no mundo real

- **Recomendação de vídeos**: plataformas que otimizaram só cliques aprenderam a favorecer títulos sensacionalistas. Várias passaram a combinar sinais como tempo assistido e pesquisas de satisfação, um exemplo prático de múltiplos objetivos.
- **Desacoplamento em ranking**: sistemas grandes de busca e anúncios costumam ter modelos separados (relevância, probabilidade de clique, risco de política) e uma camada de combinação ajustável, justamente para mudar prioridades sem retreinar.
- **Classificação hierárquica** é comum em e-commerce para categorizar milhões de produtos novos que chegam de vendedores.

## Erros comuns de quem está aprendendo

- **Começar pelo modelo, não pelo objetivo.** Sem uma métrica de negócio definida, não há como saber se o projeto deu certo.
- **Assumir que mais acurácia sempre ajuda.** A partir de certo ponto, o ganho no negócio é zero, e o custo de manter um modelo mais complexo continua.
- **Tratar o deploy como fim do projeto.** O ciclo continua com monitoramento e retreino. Os capítulos 8 e 9 mostram por quê.
- **Escolher a formulação mais natural sem pensar em manutenção.** No exemplo do próximo app, a formulação "natural" exigia retreinar a cada app novo.

## Verifique se entendeu

1. Por que uma melhora na acurácia pode não significar nada para o negócio? (Do objetivo de negócio ao objetivo de ML)
2. O que torna as falhas de ML "silenciosas", e qual requisito isso ameaça? (Os quatro requisitos)
3. Reformule "prever o preço de uma casa" como classificação. O que se ganha e o que se perde? (Formular o problema)
4. Por que desacoplar qualidade e engajamento em dois modelos facilita a vida da equipe? (Funções objetivo e o desacoplamento)
5. Descreva um caminho no ciclo de desenvolvimento em que o monitoramento faz a equipe voltar ao escopo. (Um processo iterativo)

## Para ir além

- [summary.md oficial](https://github.com/chiphuyen/dmls-book/blob/main/summary.md): resumo da autora, útil para confirmar os quatro requisitos e o debate mente versus dados.
- [Booklet Machine Learning Systems Design](https://huyenchip.com/machine-learning-systems-design/design-a-machine-learning-system.html): a etapa de "project setup" do booklet gratuito é a versão inicial da discussão de escopo deste capítulo.
- [Resumo de Andrew Clark](https://andrewclark.co.uk/product-book-summaries/designing-machine-learning-systems): traz o capítulo de design resumido com tabelas comparativas.

---
Anterior: [1. Visão geral de sistemas de ML](01-visao-geral-de-sistemas-de-ml.md) · Próximo: [3. Fundamentos de engenharia de dados](03-fundamentos-de-engenharia-de-dados.md) · Voltar ao livro: [Guia de leitura](index.md)
