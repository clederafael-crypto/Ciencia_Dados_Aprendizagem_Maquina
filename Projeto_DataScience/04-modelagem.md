# Fase 4: Modelagem

## Objetivo central

Aplicar técnicas matemáticas, gerar designs de teste e iterar parâmetros para descobrir padrões de alto valor.

## Checklist de execução

- [ ] **Selecionar as técnicas (clusterização, predição)**
  - [ ] Estatística descritiva para equidade: desvio e índice de Gini por escala
  - [ ] Predição de substituições com um modelo simples (ex.: regressão logística ou árvore de decisão)
- [ ] **Gerar o design de teste (partição em treino/teste)**
  - [ ] Partição por tempo: meses mais antigos para treino e mais recentes para teste, nunca divisão aleatória
- [ ] **Construir e iterar**
  - [ ] Começar pelo modelo mais simples
  - [ ] Ajustar parâmetros e variáveis a cada rodada
- [ ] **Fazer a avaliação técnica estatística**
  - [ ] Métricas do modelo (ex.: precisão, recall, F1)
  - [ ] Comparar com um baseline simples (ex.: "sempre prevê sem substituição")

## Caso prático: MilitarySchedule

**Equidade:** Índice de Gini da carga de serviços em cada uma das 5 escalas, separando dias úteis e vermelhos.

**Substituições:** Árvore de decisão mostrando quais fatores (escala, tipo de dia, mês, folga anterior) mais se associam a substituições.

## Entregável

Métricas de equidade por escala e modelo baseline com avaliação técnica.

## Controle

| Campo | Valor |
|---|---|
| Status | Não iniciado |
| Responsável | |
| Prazo | |
| Observações | |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.

**Próxima fase:** `05-avaliacao.md`
