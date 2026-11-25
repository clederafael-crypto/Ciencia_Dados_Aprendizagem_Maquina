# Dicionário de dados

Fonte: Our World in Data, [owid/co2-data](https://github.com/owid/co2-data) (CC BY 4.0). Descrições completas no arquivo `dados/brutos/owid-co2-codebook.csv`. A mesma descrição, com contagens e estatísticas calculadas por fórmula, está na aba **Dicionário** de `dados/planilha_base_de_dados.xlsx`.

## Variáveis originais usadas

| Coluna original | Unidade | Cobertura em 2022 (países) | Uso |
|---|---|---|---|
| `co2_per_capita` | t/pessoa | 97,8% | Alvo (A); atributo e alvo da janela (B); agrupamento |
| `gdp` | US$ internacionais de 2011 | 73,5% | Calculei o PIB per capita (÷ população) |
| `population` | pessoas | 99,1% | Atributo; denominador do PIB |
| `energy_per_capita` | kWh/pessoa | 93,3% | Atributo |
| `methane_per_capita` | t CO₂e/pessoa | 89,2% | Atributo |
| `coal_co2`, `oil_co2`, `gas_co2`, `co2` | milhões de t | 62,3% (carvão); 97,8% (petróleo); 58,3% (gás) | Participação de cada combustível |

O CO₂ per capita inclui combustíveis fósseis e processos industriais, **mas não a mudança no uso da terra**.

## Variáveis construídas

| Variável | Definição |
|---|---|
| `pib_per_capita` | `gdp` ÷ `population` |
| `log_co2`, `log_pib`, `log_pop`, `log_energia` | logaritmo (base 10) das variáveis |
| `part_carvao`, `part_petroleo`, `part_gas` | emissão do combustível ÷ `co2` total |
| `tendencia_5a` | log10 do CO₂ per capita no ano inicial menos o de 5 anos antes |
| `ano_final` | ano inicial + 10 |
| `reduziu` | 1 se o CO₂ per capita do ano final for menor que o do ano inicial; 0 caso contrário |
| `variacao_pct` | (CO₂ pc final ÷ CO₂ pc inicial − 1) × 100 |
| `conjunto` | `treino` ou `teste`, por país (41 países de teste, 123 de treino, semente 42) |

## Tabelas geradas

| Arquivo | Linhas | Conteúdo |
|---|---|---|
| `dados/tratados/painel_pais_ano.csv` | 3.772 | Painel país-ano, 2000–2022 (base da regressão) |
| `dados/tratados/janelas_10_anos.csv` | 2.132 | Janelas de 10 anos com o alvo `reduziu` (base da classificação) |
| `dados/tratados/previsoes_regressao_teste.csv` | 943 | Previsão e resíduo de cada linha de teste |
| `dados/tratados/previsoes_classificacao_teste.csv` | 533 | Previsão e probabilidade de cada janela de teste |
| `dados/tratados/grupos_2022.csv` | 163 | Grupo de cada país no agrupamento (k = 3) |
| `dados/planilha_base_de_dados.xlsx` | 3.772 + 2.132 | Planilha com os dois conjuntos e a descrição |
| `resultados/resultados.json` | — | Todos os números do estudo |

## Cuidados

- **Agregados descartados:** 36 entidades sem código ISO (regiões, "Mundo", União Europeia etc.).
- **Ausências:** imputação pela mediana dentro do `Pipeline`, aprendida só no treino.
- **Anos sem PIB:** a base não tem PIB depois de 2022.
- **Observações repetidas:** o mesmo país aparece em 23 linhas (painel) e 13 janelas; por isso o treino e o teste são separados por país.
- **Emissões territoriais:** o CO₂ é atribuído ao país onde ocorre, e não ao que consome os bens.
