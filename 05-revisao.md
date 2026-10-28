<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Questões de revisão — Registro individual

## Identificação

- Estudante ou equipe: **Cléder Rafael Narciso de Araújo**
- Turma: **Ciência de Dados e Aprendizagem de Máquina — quarta-feira, noturno**
- Data de realização: **28/10/2026**
- Integrantes e contribuições (se em equipe): **Não se aplica: registro individual.**

Responda com suas palavras e apresente os cálculos quando solicitados. Os números dos exercícios manuais não são os resultados do laboratório.

## 1. Explique a diferença entre regra programada para bloquear uma palavra e modelo de spam treinado com exemplos.

**Resposta:** Na regra programada, uma pessoa define explicitamente a condição ("se contém a palavra X, bloqueie"). Ela é previsível e fácil de explicar, mas só cobre o que foi previsto e falha diante de variações. No modelo de spam, não se escreve a regra: o algoritmo aprende, com mensagens já classificadas como spam ou legítimas, quais combinações de sinais indicam spam e produz uma previsão para mensagens novas. Ele se adapta melhor, mas depende da qualidade dos exemplos, pode errar nos dois sentidos e é mais difícil de explicar.

## 2. Por que codificar evadiu/permaneceu como 1/0 não transforma classificação em regressão?

**Resposta:** O tipo de tarefa depende do significado do alvo, não de como ele é escrito. Evadiu e permaneceu são categorias; 1 e 0 são só rótulos, sem noção de quantidade (1 não é "o dobro" de 0). Em regressão o alvo é uma quantidade, como o total de vendas em reais. Aqui a pergunta é "em qual classe o estudante está", então é classificação, avaliada com acurácia e matriz de confusão, e não com MAE ou R².

## 3. Uma biblioteca quer estimar empréstimos e descobrir perfis. Que tarefas correspondem a cada pergunta?

**Resposta:** Estimar empréstimos (um número, como empréstimos por semana) é regressão, uma tarefa supervisionada, pois há histórico com o valor observado. Descobrir perfis, sem categorias prévias, é agrupamento (clustering), uma tarefa não supervisionada, pois não há alvo.

## 4. O que são atributo, alvo e unidade de análise no laboratório educacional?

**Resposta:** Atributos são as informações usadas para prever: `frequencia_sem4`, `nota_sem4` e `entregas_sem4`, conhecidas até a semana 4. O alvo é o que se quer prever: `evasao_fim_semestre` (0 permaneceu, 1 evadiu). A unidade de análise é o que cada linha da tabela representa: um estudante fictício em um semestre.

## 5. Por que calcular a mediana antes de dividir os dados pode invalidar a avaliação?

**Resposta:** Porque a mediana calculada com todos os dados já usa informação do conjunto de teste. O teste deixa de ser "dados nunca vistos" e o desempenho medido pode ficar otimista (vazamento de dados). O correto é dividir primeiro, calcular a mediana apenas no treino e aplicar esse mesmo valor no teste, o que o `Pipeline` faz automaticamente (e também a cada rodada da validação cruzada).

## 6. Em uma matriz didática com TN=80, FP=5, FN=10, TP=5, calcule acurácia e sensibilidade. O resultado é suficiente para aprovar o modelo?

**Resposta:** Total = 80 + 5 + 10 + 5 = 100. Acurácia = (TN + TP) / total = (80 + 5) / 100 = 0,85 (85%). Sensibilidade = TP / (TP + FN) = 5 / (5 + 10) = 5/15 ≈ 0,333 (33,3%). Não é suficiente. Há 15 casos positivos e o modelo identifica só 5, deixando passar dois terços. E um modelo que sempre previsse a classe negativa teria a mesma acurácia (85 em 100) com sensibilidade zero, então a acurácia de 85% não mostra que ele é melhor que a referência. É preciso considerar os custos dos erros, a sensibilidade e outras métricas.

## 7. Valores reais 100, 120, 140 e previsões 110, 115, 130. Calcule MAE e informe a unidade se o alvo for vendas em reais.

**Resposta:** Erros absolutos: |100 − 110| = 10, |120 − 115| = 5, |140 − 130| = 10. MAE = (10 + 5 + 10) / 3 = 25 / 3 ≈ 8,33. Na unidade do alvo, o MAE é de aproximadamente R$ 8,33: em média, a previsão erra cerca de 8,33 reais.

## 8. Um R² de -0,2 significa “20% de acertos negativos”? Explique.

**Resposta:** Não. R² não é porcentagem de acertos. Ele compara o erro quadrático do modelo com o de uma referência que prevê sempre a média dos valores do conjunto avaliado. R² = 1 é ajuste perfeito, 0 equivale à referência e valores negativos indicam um modelo pior que simplesmente prever a média. Então −0,2 significa que o modelo foi pior que a média, não que há "20% de acertos negativos".

## 9. Uma árvore tem acurácia 1,00 no treino e 0,65 na validação. Que hipótese investigar e como?

**Resposta:** A hipótese é sobreajuste: a árvore decorou o treino, incluindo ruído, e não generaliza. Para investigar: comparar treino e validação por validação cruzada em várias configurações; limitar `max_depth` e aumentar `min_samples_leaf` e ver se a distância diminui; verificar se há dados em quantidade suficiente e se não há vazamento; comparar com uma referência simples. Se a validação melhorar com um modelo mais simples, a hipótese é reforçada.

## 10. Por que escolher a profundidade pelo teste prejudica a estimativa final?

**Resposta:** Porque, ao escolher a configuração que vai melhor no teste, o teste passa a participar do ajuste. O melhor resultado nele é em parte sorte (ou adaptação ao teste) e a estimativa fica otimista. A escolha deve ser feita no treino (validação cruzada), reservando o teste para uma avaliação final única. Se for preciso escolher de novo depois de ver o teste, é necessário um novo teste independente.

## 11. Baixa frequência associada à evasão demonstra causa? Proponha explicação alternativa.

**Resposta:** Não. Mostra associação, não que a baixa frequência cause a evasão. Explicação alternativa: um terceiro fator, como o estudante começar a trabalhar, problemas de saúde, falta de transporte ou dificuldades financeiras, pode reduzir a frequência e também levar à saída. Também pode haver causalidade inversa: quem já decidiu sair deixa de frequentar. Só um desenho de estudo adequado, e não este modelo, permitiria discutir causa.

## 12. Um modelo sinaliza um estudante como possível evasão. Que ação responsável pode ser adotada?

**Resposta:** Tratar a sinalização como um aviso, não como um fato. Uma pessoa da equipe de apoio revisa o caso e faz um convite voluntário e acolhedor para conversar e oferecer opções (monitoria, orientação de estudos, apoio social), sem punição, sem rótulo e sem decisão automática. O estudante pode recusar e contestar, os dados são usados com o mínimo necessário e com acesso restrito, e quem não foi sinalizado também pode pedir ajuda.

## Fontes adicionais consultadas

**Não consultei fontes além do material do módulo (notebook e referências nele listadas). Os cálculos das questões 6 e 7 foram conferidos por código no notebook (seção 6). Uso de IA declarado em [06-autoavaliacao.md](06-autoavaliacao.md).**

[Voltar ao início](README.md).
