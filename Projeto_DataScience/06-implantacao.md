# Fase 6: Implantação

## Objetivo central

Entregar o resultado de forma que outra pessoa possa ler, reproduzir e atualizar.

## Checklist de execução

- [x] **Planejar a implantação**
  - [x] Este é um estudo acadêmico, não um sistema em produção. A "implantação" é a publicação reprodutível no GitHub.
- [x] **Planejar monitoramento e manutenção**
  - [x] O OWID atualiza a base a cada ano. Para atualizar: rodar `python3 scripts/obter_dados.py` e depois `python3 scripts/analise.py`. Se um ano novo tiver PIB, trocar `ANO` no início do script.
  - [x] Os testes (`python3 -m pytest tests -q`) conferem se os dados e os resultados continuam coerentes.
- [x] **Produzir o relatório final**
  - [x] `README.md` (resumo), notebook executado, figuras e a planilha de dados.
- [x] **Revisar o projeto**
  - [x] Ver as lições em `07-conclusoes-e-limitacoes.md`.

## Caso prático

| O que entregar | Onde |
|---|---|
| Código reprodutível | `scripts/obter_dados.py`, `scripts/analise.py` |
| Notebook com interpretações | `notebooks/crisp-dm-co2.ipynb` (abre no Colab pelo botão do README) |
| Dados e procedência | `dados/brutos/`, `dados/tratados/`, `dados/brutos/FONTES.json` |
| Planilha descrevendo os dados | `dados/planilha_base_de_dados.xlsx` |
| Resultados | `resultados/`, `figuras/` |
| Verificação | `tests/test_resultados.py` (8 testes) |

## Entregável

Repositório com README, as seis fases documentadas, o código, os resultados e a planilha.

## Controle

| Campo | Valor |
|---|---|
| Status | Concluído |
| Responsável | Cléder Rafael Narciso de Araújo |
| Prazo | 25/11/2026 |
| Observações | Não há sistema em produção: o foco é reprodutibilidade. |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.


**Próxima fase:** `07-conclusoes-e-limitacoes.md`
