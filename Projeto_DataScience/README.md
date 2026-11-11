# CRISP-DM aplicado ao MilitarySchedule

Roteiro no formato do *Guia Definitivo: O Modelo CRISP-DM* (Ciência de Dados e Aprendizagem de Máquina, Profa. Kadidja Valéria), usando o MilitarySchedule como caso prático no lugar do varejo eletrônico.

**Pergunta do estudo:** a distribuição dos serviços está de fato equitativa? Quais escalas têm mais faltas e substituições, e por quê?

## Partes

| Arquivo | Conteúdo |
|---|---|
| `00-pre-requisitos.md` | O que confirmar antes de começar |
| `01-entendimento-do-negocio.md` | Fase 1 |
| `02-entendimento-dos-dados.md` | Fase 2 |
| `03-preparacao-dos-dados.md` | Fase 3 |
| `04-modelagem.md` | Fase 4 |
| `05-avaliacao.md` | Fase 5 |
| `06-implantacao.md` | Fase 6 |
| `07-uso-no-tcc.md` | Quando e como usar o CRISP-DM no TCC |

## Síntese prática: o fluxo do MilitarySchedule

1. **Negócio:** queremos escalas equitativas e menos substituições.
2. **Dados:** coletamos o histórico das 5 escalas, férias e feriados.
3. **Preparação:** anonimizamos, limpamos o status e mesclamos as tabelas.
4. **Modelagem:** medimos a equidade (Gini) e modelamos as substituições.
5. **Avaliação:** validamos com o sargenteante se os achados fazem sentido.
6. **Implantação:** criamos um painel de equidade no sistema.

## Por que o ciclo retorna

| Volta | Quando acontece no MilitarySchedule |
|---|---|
| Dados → Negócio | O histórico é curto demais para a pergunta original. O escopo precisa encolher (ex.: estudar só uma escala). |
| Modelagem → Preparação | O algoritmo exige dados sem nulos ou normalizados, forçando um novo tratamento. |
| Avaliação → Negócio | O modelo é preciso, mas não ajuda a montar escalas mais justas. A premissa precisa ser reconstruída. |

> No CRISP-DM, recuar não é falhar. Cada volta no ciclo aumenta a precisão do projeto.

## Resumo executivo: checklist para o sucesso

- [ ] **Comece pelo negócio:** um algoritmo perfeito não salva uma premissa falha.
- [ ] **Respeite o atrito:** a preparação de dados consumirá mais da metade do projeto.
- [ ] **Abrace a iteração:** rode modelos básicos cedo, avalie e volte com frequência.
- [ ] **Mensure o impacto:** avalie pelos critérios da Fase 1, nunca só por métricas estatísticas.
- [ ] **Documente a jornada:** as regras precisam ser traduzidas com clareza para quem mantém o sistema.

## Progresso

| Fase | Status |
|---|---|
| 1. Entendimento do Negócio | Não iniciado |
| 2. Entendimento dos Dados | Não iniciado |
| 3. Preparação dos Dados | Não iniciado |
| 4. Modelagem | Não iniciado |
| 5. Avaliação | Não iniciado |
| 6. Implantação | Não iniciado |
