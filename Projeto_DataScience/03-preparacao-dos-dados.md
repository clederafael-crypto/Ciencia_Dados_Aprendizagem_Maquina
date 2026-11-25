# Fase 3: Preparação dos Dados

## Objetivo central

Produzir as tabelas finais de modelagem, sem usar informação do teste nas transformações.

## Checklist de execução

- [x] **Selecionar os dados**
  - [x] Descartei os 36 agregados e mantive os 223 países.
  - [x] **Painel (regressão):** país-ano de 2000 a 2022, com CO₂ per capita positivo, PIB e população. **3.772 linhas, 164 países.**
  - [x] **Janelas (classificação):** atributos do ano *t* (2000 a 2012) e alvo no ano *t* + 10. **2.132 linhas**, das quais 898 (42,1%) reduziram o CO₂ per capita.
- [x] **Limpar os dados**
  - [x] Ausências no painel: energia 12, metano 23, participação do carvão 865 e do gás 1.122.
  - [x] Imputação pela **mediana, dentro do `Pipeline`**, aprendida só no treino.
- [x] **Construir novos atributos**
  - [x] PIB per capita = PIB ÷ população.
  - [x] Logaritmo (base 10) de CO₂, PIB, população e energia per capita.
  - [x] Participação de carvão, petróleo e gás no CO₂ total do país.
  - [x] Tendência dos 5 anos anteriores (usa só o passado do ano inicial).
  - [x] Alvo da classificação: `reduziu` = 1 se o CO₂ per capita do ano *t* + 10 for menor que o do ano *t*.
- [x] **Integrar e formatar**
  - [x] Tabelas em `dados/tratados/`: `painel_pais_ano.csv` e `janelas_10_anos.csv`. A planilha `dados/planilha_base_de_dados.xlsx` traz as mesmas linhas.
- [x] **Separar treino e teste antes de qualquer ajuste**
  - [x] **Por país:** sorteio com semente 42 de 41 países de teste (25%) e 123 de treino. Painel: 2.829 e 943 linhas. Janelas: 1.599 e 533 linhas. Nenhum país está nos dois lados (um teste automático confere).

## Caso prático

Nenhum dado foi inventado e nenhum país foi removido por "parecer estranho". Países com valores extremos (como Bahrein e Kuwait) ficam na amostra, porque são reais e o logaritmo reduz o peso deles. A escolha de excluir países sem PIB é uma limitação (ver `07`).

**Por que separar por país:** as 23 linhas de um mesmo país são muito parecidas entre si. Se algumas fossem para o treino e outras para o teste, o modelo "reconheceria" o país e o resultado seria otimista. O Brasil caiu no treino; por isso, na análise do Brasil, uso um modelo ajustado sem ele.

## Entregável

Tabelas tratadas em `dados/tratados/`, a planilha de dados e o código da preparação em `scripts/analise.py` (blocos "Fase 3").

## Controle

| Campo | Valor |
|---|---|
| Status | Concluído |
| Responsável | Cléder Rafael Narciso de Araújo |
| Prazo | 25/11/2026 |
| Observações | As janelas de um mesmo país se sobrepõem; o número efetivo de observações independentes é mais próximo de 164 países do que de 2.132 linhas. |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.


**Próxima fase:** `04-modelagem.md`
