# Pré-requisitos

Confirmados antes de começar. Todos foram atendidos.

- [x] **Pergunta e dados:** a pergunta do estudo pode ser respondida com dados públicos e reais (nada foi simulado).
- [x] **Volume de dados:** a base de modelagem tem **3.772 linhas** (painel país-ano) e **2.132 linhas** (janelas de 10 anos), acima do mínimo de 1.000 registros. A planilha `dados/planilha_base_de_dados.xlsx` traz todas elas e descreve cada coluna.
- [x] **Fonte e licença:** Our World in Data, repositório [owid/co2-data](https://github.com/owid/co2-data), licença **CC BY 4.0** (uso permitido com citação da fonte).
- [x] **Sem dados pessoais:** a unidade é o país. Não há pessoas, empresas nem endereços, então a LGPD não se aplica.
- [x] **Procedência registrada:** `dados/brutos/FONTES.json` guarda a URL, a data de acesso (25/11/2026) e o hash SHA-256 de cada arquivo.
- [x] **Ambiente:** Python 3.13.18, NumPy 2.5.3, pandas 3.0.5, scikit-learn 1.9.1, matplotlib 3.11.2, semente 42 (`requirements.txt`).
- [x] **Reprodutibilidade:** `python3 scripts/analise.py` gera todas as tabelas, figuras e `resultados/resultados.json`. O notebook `notebooks/crisp-dm-co2.ipynb` faz o mesmo passo a passo.
- [x] **Rede:** só é preciso internet para baixar o arquivo bruto uma vez (`python3 scripts/obter_dados.py`). O arquivo já está em `dados/brutos/`.

**Próxima fase:** `01-entendimento-do-negocio.md`
