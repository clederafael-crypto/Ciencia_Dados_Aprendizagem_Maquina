# Fase 1: Entendimento do Negócio

## Objetivo central

Traduzir o problema em metas técnicas viáveis antes de investir recursos computacionais.

## Checklist de execução

- [x] **Determinar os objetivos de negócio e os critérios de sucesso**
  - [x] Pergunta do estudo em uma frase: *o que o nível de desenvolvimento de um país diz sobre quanto CO₂ ele emite por pessoa, e quais países conseguem reduzir esse valor ao longo de uma década?*
  - [x] Critérios de sucesso: (A) o modelo de regressão tem de errar menos que prever a média; (B) o classificador tem de superar a classe mais frequente; (C) os grupos têm de ser descritíveis, com a silhueta informada (não defini um limite numérico). O teste só é usado uma vez, em países que o modelo não viu.
- [x] **Avaliar a situação (recursos, riscos, análise de custo-benefício)**
  - [x] Recursos: base pública do OWID com 79 colunas e 259 entidades; Python e scikit-learn.
  - [x] Riscos: PIB só até 2022 e ausente em cerca de 26% dos países; o mesmo país aparece em vários anos, o que exige separar treino e teste **por país**; correlação não é causa.
  - [x] Custo-benefício: dados gratuitos e abertos; o estudo cabe em um notebook.
- [x] **Determinar as metas técnicas de mineração de dados**
  - [x] A (regressão): prever o logaritmo do CO₂ per capita de um país em um ano (3.772 linhas).
  - [x] B (classificação): prever se o CO₂ per capita cai nos 10 anos seguintes, usando só dados do ano inicial ou anteriores (2.132 janelas).
  - [x] C (agrupamento): agrupar os países de 2022 pelo perfil de emissão, PIB, energia e metano.
- [x] **Produzir o Plano de Projeto**
  - [x] Fases, entregáveis e regras de decisão (escolha de modelo por validação cruzada no treino, teste usado uma vez) estão nos arquivos `01` a `06`.

## Caso prático: emissões de CO₂ e desenvolvimento

**Cenário:** países de renda mais alta emitem mais CO₂ por pessoa, mas há exceções (países com eletricidade limpa ou muito carvão) e nem todos os países mantêm a trajetória. Não está claro o quanto o perfil econômico explica e quais fatores acompanham uma redução.

**Meta de negócio:** entender o que distingue países que emitem mais ou menos do que o esperado e quais conseguem reduzir o CO₂ per capita.

**Meta técnica:** um modelo de regressão (A), um classificador de redução (B) e um agrupamento (C), todos comparados com uma referência simples.

## Entregável

Este documento: objetivo, critérios de sucesso, avaliação da situação e plano.

## Controle

| Campo | Valor |
|---|---|
| Status | Concluído |
| Responsável | Cléder Rafael Narciso de Araújo |
| Prazo | 25/11/2026 |
| Observações | As comparações com a referência e as regras de escolha de modelo estão no código antes da avaliação no teste. Nenhum limite numérico de desempenho foi definido. |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.


**Próxima fase:** `02-entendimento-dos-dados.md`
