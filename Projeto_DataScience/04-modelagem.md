# Fase 4: Modelagem

## Objetivo central

Escolher e ajustar modelos usando **apenas o treino** (validação cruzada), com uma referência simples para comparar.

## Checklist de execução

- [x] **Selecionar as técnicas de modelagem**
  - [x] A (regressão): regressão linear e floresta aleatória, contra a média (`DummyRegressor`).
  - [x] B (classificação): regressão logística, árvore (profundidade 4) e floresta, contra a classe mais frequente.
  - [x] C (agrupamento): k-means com atributos padronizados.
- [x] **Gerar o desenho dos testes**
  - [x] Validação cruzada **por país** (5 partes × 3 repetições) só no treino; na classificação, estratificada pelo alvo.
  - [x] Regras de escolha fixadas antes de ver o teste: A, menor MAE médio; B, maior AUC médio; C, melhor silhueta entre 3 e 6 grupos.
- [x] **Construir os modelos**
  - [x] Tudo dentro de `Pipeline` (imputação, padronização quando necessária, modelo), semente 42.
- [x] **Avaliar os modelos**
  - [x] Resultados da validação em `resultados/regressao_validacao.csv` e `resultados/classificacao_validacao.csv`.

## Caso prático (números da validação)

**A — regressão (2.829 linhas de treino):** MAE em log10 de 0,2171 (só PIB), 0,2113 (+ população, metano e ano) e **0,1107** (+ energia), contra 0,5724 da referência. A regressão linear ficou à frente da floresta em todos os conjuntos, por margens do tamanho do desvio entre partes. Escolhido: **conjunto 3 + regressão linear**.

**B — classificação (1.599 janelas de treino):** AUC de validação de 0,7873 (logística), 0,7790 (floresta), 0,7306 (árvore) e 0,5 (referência). A diferença entre logística e floresta (0,008) é bem menor que o desvio entre partes (0,03 a 0,06): é um empate prático. Escolhida pela regra: **regressão logística**.

**C — agrupamento (163 países em 2022):** silhueta de 0,507 (k=2), **0,533 (k=3)**, 0,430 (k=4), 0,379 (k=5 e 6) e 0,384 (k=7). Escolhido: k = 3.

## Entregável

Modelos treinados e tabelas de validação, reproduzíveis com `python3 scripts/analise.py`.

## Controle

| Campo | Valor |
|---|---|
| Status | Concluído |
| Responsável | Cléder Rafael Narciso de Araújo |
| Prazo | 25/11/2026 |
| Observações | Nenhum modelo foi trocado depois de olhar o teste. |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.


**Próxima fase:** `05-avaliacao.md`
