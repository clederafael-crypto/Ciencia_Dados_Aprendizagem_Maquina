# Fase 1: Entendimento do Negócio

## Objetivo central

Traduzir o problema de negócio em metas técnicas viáveis antes de investir recursos computacionais.

## Checklist de execução

- [ ] **Determinar os objetivos de negócio e os critérios de sucesso**
  - [ ] Escrever a pergunta do estudo em uma frase
  - [ ] Definir o critério de sucesso (ex.: diferença máxima aceitável de serviços entre militares da mesma escala)
- [ ] **Avaliar a situação (recursos, riscos, análise de custo-benefício)**
  - [ ] Recursos: banco do sistema, scripts Python existentes, tempo disponível
  - [ ] Riscos: histórico curto, dados pessoais (LGPD), autorização da OM
  - [ ] Custo-benefício: o estudo reaproveita dados que o sistema já grava
- [ ] **Determinar as metas técnicas de mineração de dados**
  - [ ] Medir a dispersão da carga de serviços por escala
  - [ ] Identificar padrões de faltas e substituições
- [ ] **Produzir o Plano de Projeto**
  - [ ] Fases, prazos e entregáveis (use a seção Controle de cada arquivo)
  - [ ] Validar o plano com o sargenteante

## Caso prático: MilitarySchedule

**Cenário:** O rodízio do MilitarySchedule é heurístico: escala, a cada dia, o militar elegível há mais tempo sem servir. Não se sabe quanto a distribuição real se afasta do ideal.

**Meta de negócio:** Garantir uma distribuição equitativa dos serviços e reduzir faltas e substituições.

**Meta técnica:** Métricas de equidade por escala (desvio e índice de Gini da carga) e um modelo simples que identifique os fatores ligados às substituições.

## Entregável

Documento de 1 página com objetivo, critérios de sucesso, avaliação da situação e Plano de Projeto.

## Controle

| Campo | Valor |
|---|---|
| Status | Não iniciado |
| Responsável | |
| Prazo | |
| Observações | |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.

**Próxima fase:** `02-entendimento-dos-dados.md`
