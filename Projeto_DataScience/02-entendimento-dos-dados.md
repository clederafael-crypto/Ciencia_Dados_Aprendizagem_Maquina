# Fase 2: Entendimento dos Dados

## Objetivo central

Acessar, quantificar e qualificar a matéria-prima disponível para evitar falhas imprevistas na modelagem.

## Checklist de execução

- [ ] **Coletar os dados iniciais (existentes, comprados ou adicionais)**
  - [ ] Conferir antes os pré-requisitos (`00-pre-requisitos.md`)
  - [ ] Extrair do banco as tabelas listadas no caso prático
  - [ ] Avaliar se faltam dados adicionais (ex.: motivo das substituições)
- [ ] **Descrever quantidade e qualidade (volume, tipos de valores, códigos)**
  - [ ] Período coberto por cada tabela
  - [ ] Nº de registros por escala e por mês
  - [ ] Códigos usados no campo status
- [ ] **Explorar os dados (gráficos, hipóteses iniciais)**
  - [ ] Gráfico de serviços por militar em cada escala
  - [ ] Hipóteses iniciais (ex.: dias vermelhos concentram mais substituições)
- [ ] **Verificar a qualidade (erros, dados omissos, inconsistências de medição)**
  - [ ] Nulos e inconsistências no campo status
  - [ ] Escalas lançadas para militares de férias
  - [ ] Datas fora do período esperado

## Caso prático: MilitarySchedule

**Fontes:** As 5 tabelas `ESCALA_*`, `ESCALA_FILA`, `FERIAS`, `FERIADO` e `LOG_AUDITORIA`.

**Descobertas possíveis:** Registros antigos com status sempre em "Escalado" (nunca atualizado para Cumprido) e substituições sem motivo registrado.

## Entregável

Relatório de coleta, descrição, exploração e qualidade dos dados.

## Controle

| Campo | Valor |
|---|---|
| Status | Não iniciado |
| Responsável | |
| Prazo | |
| Observações | |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.

**Próxima fase:** `03-preparacao-dos-dados.md`
