<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Aula 2 — Registro do laboratório supervisionado

## Identificação

- Estudante ou equipe: **Cléder Rafael Narciso de Araújo (atividade individual)**
- Turma: **Ciência de Dados e Aprendizagem de Máquina — quarta-feira, noturno**
- Data de realização: **28/10/2026**
- Integrantes e contribuições (se em equipe): **Não se aplica: atividade individual.**

## Percurso escolhido

- [x] Python/Colab ou Jupyter.
- [ ] Orange Data Mining.

Use o [notebook de apoio](notebooks/laboratorio.ipynb) ou o [CSV sintético](dados/educacionais-sinteticos.csv). O CSV contém 600 registros fictícios. Atributos: `frequencia_sem4`, `nota_sem4`, `entregas_sem4`. Alvo: `evasao_fim_semestre` (0 permaneceu, 1 evadiu). As associações foram definidas pela simulação, sem validade empírica sobre estudantes reais.

## 1. Ambiente e reprodução

| Item | Registro |
| --- | --- |
| Ambiente e data | Python 3 executado em ambiente de nuvem (não no Colab), em 28/10/2026, com as células do notebook de apoio na ordem. |
| Versões das ferramentas/bibliotecas | Python 3.13.18, NumPy 2.5.3, pandas 3.0.5, matplotlib 3.11.2, scikit-learn 1.9.1. (O notebook de apoio mostra versões diferentes, de outra execução; os resultados numéricos coincidiram.) |
| Semente aleatória | 42 (`SEMENTE = 42`), usada na simulação, na divisão, na validação cruzada e na árvore. |
| Caminho do notebook executado ou fluxo Orange | [notebooks/laboratorio-equipe.ipynb](notebooks/laboratorio-equipe.ipynb) |
| Origem dos dados e condição sintética | Gerados por simulação no próprio notebook (idêntica ao arquivo [dados/educacionais-sinteticos.csv](dados/educacionais-sinteticos.csv), conferida). Todos os registros são sintéticos e não representam estudantes reais. |

## 2. Problema e preparação

- Pergunta de negócio: **Quem poderia receber um convite voluntário de apoio antes do fim do semestre?**
- Unidade de análise e horizonte: **Um estudante fictício; previsão feita ao fim da semana 4, para o desfecho do fim do semestre.**
- Atributos disponíveis no instante da previsão: **`frequencia_sem4` (%), `nota_sem4` (0 a 10) e `entregas_sem4` (0 a 8), todos observados até a semana 4.**
- Variável-alvo e sua natureza: **`evasao_fim_semestre`, categórica binária (0 permaneceu, 1 evadiu); 59,0% de classe 0 e 41,0% de classe 1. Conhecida só no fim do semestre.**
- Ausências e outros problemas encontrados: **30 valores ausentes, todos em `nota_sem4` (5% das linhas). Frequência e entregas estão completas. Não há identificadores.**
- Tratamentos e conjunto usado para aprendê-los: **Imputação pela mediana de cada coluna, aprendida apenas no conjunto de treino, dentro de um `Pipeline`. Não houve padronização, pois a árvore não precisa dela.**

## 3. Desenvolvimento e teste

- Método de divisão e justificativa: **`train_test_split` aleatório e estratificado pelo alvo (25% para teste, semente 42). A divisão aleatória é adequada porque as observações simuladas são independentes; com turmas reais seria melhor separar por período e por estudante.**
- Quantidades de treino e teste: **450 e 150 registros.**
- Procedimento de validação no treino: **Validação cruzada estratificada em 5 partes (`StratifiedKFold`, embaralhada, semente 42), usando só o treino.**
- Parâmetros da árvore e como foram escolhidos: **`max_depth` comparado em 2, 3, 5 e sem limite (validação média 0,6844; 0,7022; 0,7222; 0,7111), escolhendo 5; `min_samples_leaf` fixado em 10. Em um segundo experimento comparei folhas de 5, 10, 20 e 40 (seção 5).**
- Como o teste ficou fora da seleção: **A escolha usou apenas a validação cruzada do treino. O teste foi usado uma única vez para a avaliação final. Os experimentos extras foram feitos depois, apenas no treino, e não alteraram o modelo final.**

### Alternativa Orange

Confira o alvo como categórico. Registre as conexões: File/Select Columns → Test & Score (Data), Tree → Test & Score (Learner), Test & Score → Confusion Matrix (Evaluation Results). Data Table permite inspeção. Se usar Preprocess, conecte o preprocessor ao learner para ajustar transformações dentro do treino. Não use apenas `Test on train data` como avaliação final.

**Fluxo e método de avaliação realmente utilizados:** **Não se aplica: usei Python (notebook), não o Orange.**

Se comparar configurações, use validação no treino e reserve teste independente. Documente em Test & Score as entradas Data e Test Data, quando utilizadas.

## 4. Resultados calculados de classificação

| Modelo | Configuração | Acurácia de treino | Acurácia de validação e dispersão | Acurácia de teste |
| --- | --- | --- | --- | --- |
| Referência | `DummyClassifier`, classe mais frequente (permaneceu) | Não calculada (não foi necessária para a comparação) | Não calculada | 0,5933 |
| Árvore final | Imputação pela mediana + árvore, `max_depth=5`, `min_samples_leaf=10`, semente 42 | 0,8133 (no treino inteiro; 0,8111 na média da validação cruzada) | 0,7222 ± 0,0391 (média ± desvio entre as 5 partes) | 0,7800 |

Não invente valores. Se sua ferramenta não produziu uma medida, registre “não calculada” e explique.

**Matriz: linhas reais e colunas previstas; classe positiva = 1.**

| Real / previsto | Permaneceu (0) | Evadiu (1) |
| --- | --- | --- |
| Permaneceu (0) | 75 (TN) | 14 (FP) |
| Evadiu (1) | 19 (FN) | 42 (TP) |

- Acurácia calculada manualmente pela matriz: **(75 + 42) / 150 = 0,78.**
- Sensibilidade da classe 1: **42 / (42 + 19) = 0,6885 (cerca de 68,9%).** Precisão da classe 1: 42/56 = 0,75.
- Comparação com referência: **0,78 contra 0,5933, uma melhora de cerca de 18,7 pontos percentuais. A referência tem sensibilidade zero para a classe 1 (nunca sinaliza ninguém), então o modelo é útil para o propósito de identificar quem pode precisar de apoio.**
- Consequências dos falsos positivos: **14 estudantes que não evadiriam seriam convidados para apoio sem necessidade: custo de tempo da equipe e possível incômodo, mas o convite é voluntário e o dano é baixo.**
- Consequências dos falsos negativos: **19 estudantes que evadiriam não seriam sinalizados e perderiam a oportunidade de apoio. É o erro mais grave aqui, e a sensibilidade de 68,9% mostra que cerca de 31% dos casos de evasão passariam despercebidos. Por isso nenhum estudante deve ser desassistido só porque o modelo não o sinalizou.**
- Interpretação do gráfico e da árvore: **![Matriz de confusão](assets/matriz-confusao.png) A diagonal principal (75 e 42) concentra a maioria dos casos. ![Árvore](assets/arvore.png) A primeira pergunta da árvore é `nota_sem4 <= 6,207`, seguida de `frequencia_sem4` (cerca de 64 a 65%) e `entregas_sem4`. No ramo de nota baixa e frequência baixa, a maioria dos registros de treino é de evasão (no nó seguinte, com entregas até 3, 95 dos 128 registros de treino evadiram); no ramo de nota alta e frequência acima de cerca de 65%, quase todos permanecem (89 de 90 antes de novas divisões). Isso descreve associações do conjunto simulado, não causas. Só os primeiros níveis estão visíveis; há ramos mais profundos ocultos.**

## 5. Experimentos no treino

Compare parâmetros usando apenas treino/validação. Após conhecer o teste, uma nova seleção exige novo teste independente para avaliação final.

| Experimento | Alteração | Resultado de validação | Interpretação |
| --- | --- | --- | --- |
| 1 | `min_samples_leaf` em 5, 10, 20 e 40 (cada um com profundidade 3, 5 e sem limite) | De 0,7000 a 0,7289. Melhor: folha 40 (0,7289 ± 0,0303). Escolhido originalmente (profundidade 5, folha 10): 0,7222 ± 0,0391. | A diferença (0,0067) é muito menor que o desvio, então não há evidência de melhora real. Folhas maiores reduziram a acurácia de treino (de 0,8678 para 0,7756) e a distância entre treino e validação. Mantive o modelo final; trocar de configuração agora exigiria um novo teste independente. |
| 2 | Retirar um atributo por vez (profundidade 5, folha 10) | Com os três atributos: 0,7222. Sem frequência: 0,7156. Sem entregas: 0,7022. Sem nota: 0,6289. | A queda maior ocorre sem a nota, então o modelo depende mais dela neste conjunto. Isso mostra associação na simulação, não causa. |

Responda:

1. Como a profundidade e o tamanho das folhas podem afetar o sobreajuste? **Árvores mais profundas e com folhas muito pequenas conseguem separar quase todos os exemplos de treino, incluindo o ruído, e o desempenho em dados novos deixa de acompanhar o do treino. Nos experimentos, folha 5 sem limite de profundidade chegou a 0,8678 no treino e 0,7133 na validação, e folha 40 ficou em 0,7756 e 0,7289. Limitar profundidade e exigir mais exemplos por folha simplifica o modelo e reduz esse risco.**
2. Retirar um atributo e observar mudança no desempenho prova causalidade? **Não. Mostra apenas que o modelo usa a informação daquele atributo para prever; ela pode estar correlacionada com outros atributos ou com causas que não foram medidas, e a mudança também depende do modelo e da divisão dos dados. Neste conjunto, as associações foram definidas pela simulação.**
3. Se 95% permanecem, o que acontece com um modelo que sempre prevê permanência? **Teria 95% de acurácia, aparentemente ótima, mas sensibilidade zero: nenhum estudante que evadiria seria identificado (todos seriam falsos negativos). Por isso é preciso olhar a matriz de confusão e a sensibilidade, não só a acurácia.**

## 6. Regressão — seção independente

Execute a seção da biblioteca no notebook ou registre o procedimento equivalente em Orange. Dados também sintéticos. Alvo numérico: empréstimos por semana.

| Item | Registro |
| --- | --- |
| Atributos e alvo | Atributos: `usuarios_ativos` (100 a 1000) e `horas_abertura` (20 a 60 por semana). Alvo: `emprestimos_semana` (numérico, 300 registros sintéticos). |
| Divisão e preparação | Divisão aleatória, 25% para teste (225 treino e 75 teste), semente 42, sem estratificação. Imputação pela mediana dentro do `Pipeline` (não havia ausências). Regressão linear. |
| MAE do modelo e unidade | 28,59 empréstimos por semana (teste). |
| MAE da referência | 84,73 empréstimos por semana (`DummyRegressor`, média do treino). |
| R² do teste | 0,8774 |
| Interpretação do gráfico observado/previsto | ![Observado × previsto](assets/regressao-obs-prev.png) Os pontos ficam em torno da linha tracejada (previsão igual ao observado), sem desvio sistemático evidente; a dispersão em torno da linha corresponde ao erro de cerca de 28 empréstimos. |
| Interpretação dos resíduos | ![Resíduos](assets/regressao-residuos.png) Os resíduos (observado − previsto) oscilam em torno de zero (média −1,28, desvio 35,47; de cerca de −87 a +65), sem padrão curvo evidente na inspeção visual. Isso é leitura visual, não teste estatístico. |
| Limitação de extrapolação | Os dados de treino cobrem cerca de 107 a 993 usuários ativos e 20 a 60 horas. Uma previsão para 10.000 usuários estaria fora desse domínio e não seria confiável. Os coeficientes (≈ 0,35 por usuário e ≈ 2,30 por hora) não são efeitos causais. |

Explique por que R² não é porcentagem de acertos: **Em regressão o valor previsto quase nunca é exatamente igual ao observado, então não faz sentido contar acertos. O R² compara o erro quadrático do modelo com o de uma referência que prevê sempre a média: 1 é ajuste perfeito, 0 equivale à referência e pode ser negativo (pior que a referência). R² = 0,8774 quer dizer que o erro quadrático é cerca de 12% do da referência, não que 87,7% das previsões estão certas.**

## 7. Evidências e conclusão

- Link relativo do notebook/fluxo: **[notebooks/laboratorio-equipe.ipynb](notebooks/laboratorio-equipe.ipynb)**
- Links das imagens, se houver: **[matriz](assets/matriz-confusao.png), [árvore](assets/arvore.png), [observado × previsto](assets/regressao-obs-prev.png), [resíduos](assets/regressao-residuos.png), [histogramas](assets/hist-atributos.png)**
- Principal aprendizado: **Um modelo só tem valor quando comparado com uma referência simples e avaliado em dados que ele não viu; e a acurácia sozinha não basta, pois os dois tipos de erro têm custos diferentes. Escolher parâmetros só com o treino mantém o teste honesto.**
- Limitações de generalização e vieses possíveis: **Os dados são simulados, com associações escolhidas por quem fez a simulação; houve uma única divisão final (75 e 42 acertos em 150 casos) e o teste é pequeno, então a acurácia de 0,78 tem incerteza. Não há grupos reais no conjunto, portanto não se pode afirmar equidade. Em dados reais, um modelo poderia errar mais com grupos pouco representados.**
- Cuidados com privacidade e uso responsável: **Usar apenas dados sintéticos; em uma aplicação real, coletar o mínimo, restringir acesso, definir retenção, não usar a previsão para punir e garantir revisão humana e direito de contestação.**

Para inserir uma imagem salva, use `![Matriz de confusão](assets/minha-matriz.png)` e confira se o arquivo existe. Mostre apenas dados sintéticos.

[Voltar ao início](README.md).
