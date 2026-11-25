# Fase 2: Entendimento dos Dados

## Objetivo central

Conhecer a qualidade e a estrutura dos dados antes de tratá-los.

## Checklist de execução

- [x] **Coletar os dados iniciais**
  - [x] `owid-co2-data.csv` (15,2 MB), baixado do repositório do OWID em 25/11/2026. SHA-256 em `dados/brutos/FONTES.json`.
- [x] **Descrever os dados**
  - [x] 56.269 linhas × 79 colunas, de 1750 a 2025, com 259 entidades: **223 países** (com código ISO) e **36 agregados** (regiões, "Mundo", União Europeia etc.).
  - [x] Unidades: CO₂ per capita em t/pessoa; energia em kWh/pessoa; PIB em dólares internacionais de 2011; metano em t de CO₂ equivalente por pessoa. Ver `docs/DICIONARIO_DADOS.md` e a aba **Dicionário** da planilha.
- [x] **Explorar os dados**
  - [x] Em 2022, 218 países têm CO₂ per capita. Só 73,5% (164) têm PIB. Energia: 93,3%. Metano: 89,2%. Carvão: 62,3%. Gás: 58,3%.
  - [x] Para 2000 a 2022, os 164 países com PIB formam um painel balanceado de **3.772 linhas** (23 anos cada).
  - [x] Distribuição do CO₂ per capita muito assimétrica; na escala log, regular (`figuras/01-visao-geral.png`).
  - [x] Correlação entre log do PIB per capita e log do CO₂ per capita, em todas as linhas: 0,925.
- [x] **Verificar a qualidade dos dados**
  - [x] O PIB não existe depois de 2022, então 2022 é o último ano possível.
  - [x] Carvão e gás ausentes (865 e 1.122 linhas do painel) podem significar "zero" ou "não medido" (não dá para separar).
  - [x] Os agregados repetem emissões dos países e precisam sair.

## Caso prático

Entre as 79 colunas, usei as que descrevem o perfil do país **antes** do resultado: população, PIB, energia, metano e participação de cada combustível. As colunas de emissão por combustível por pessoa **não** entram como atributos da regressão, porque somadas formam o próprio CO₂ per capita (vazamento do alvo).

## Entregável

Relatório de qualidade dos dados: seção 2 do notebook, a aba **Dicionário** da planilha e `resultados/resultados.json`.

## Controle

| Campo | Valor |
|---|---|
| Status | Concluído |
| Responsável | Cléder Rafael Narciso de Araújo |
| Prazo | 25/11/2026 |
| Observações | A ausência de PIB reduz a amostra a 164 países, mas o painel multiplica isso por 23 anos. |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.


**Próxima fase:** `03-preparacao-dos-dados.md`
