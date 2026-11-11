# Fase 3: Preparação dos Dados

## Objetivo central

Transformar, limpar e empacotar os dados brutos em um formato digerível pelos algoritmos. É a base do sucesso.

## Checklist de execução

- [ ] **Selecionar (filtrar)**
  - [ ] Manter só os registros do período analisado
  - [ ] Descartar colunas que não serão usadas
- [ ] **Limpar (tratar)**
  - [ ] Corrigir ou excluir registros com status inconsistente
  - [ ] Tratar nulos
- [ ] **Construir (derivar)**
  - [ ] Uma linha por militar por mês
  - [ ] Serviços em dias úteis e em dias vermelhos
  - [ ] Folga média e nº de faltas e substituições
- [ ] **Integrar (mesclar)**
  - [ ] Juntar as 5 tabelas de escala pelo identificador do militar
  - [ ] Cruzar com `FERIAS` e `FERIADO`

## Caso prático: MilitarySchedule

**Mesclar:** As 5 tabelas `ESCALA_*` com `FERIAS` e `FERIADO`, via identificador do militar.

**Filtrar atributos confidenciais:** Trocar nome, CPF e dados de dependentes por um identificador anônimo (LGPD).

**Criar atributos:** Dias de folga entre serviços e proporção de serviços em dias vermelhos.

> **Atenção:** de 50% a 70% do tempo e do esforço do projeto costumam ir para esta fase. Planeje-se para isso.

## Entregável

Base analítica anonimizada e script Python versionado.

## Controle

| Campo | Valor |
|---|---|
| Status | Não iniciado |
| Responsável | |
| Prazo | |
| Observações | |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.

**Próxima fase:** `04-modelagem.md`
