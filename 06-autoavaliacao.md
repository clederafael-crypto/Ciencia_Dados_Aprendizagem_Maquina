<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Autoavaliação e conferência da entrega

## Identificação

- Estudante ou equipe: **Cléder Rafael Narciso de Araújo (atividade individual)**
- Turma: **Ciência de Dados e Aprendizagem de Máquina — quarta-feira, noturno**
- Data de realização: **28/10/2026**
- Integrantes e contribuições (se em equipe): **Não se aplica: atividade individual.**

## Checklist

- [x] Diferenciei IA, Ciência de Dados e ML com um exemplo.
- [x] Completei o quadro supervisionado/não supervisionado.
- [x] Justifiquei pelo menos cinco situações-problema.
- [x] Registrei a investigação da biblioteca.
- [x] Identifiquei atributos, alvo, unidade e momento da previsão.
- [x] Executei e documentei a prática em Python ou Orange.
- [x] Escolhi configurações usando treino/validação.
- [x] Mantive o teste fora do ajuste e da seleção.
- [x] Interpretei acurácia, matriz, MAE e R².
- [x] Comparei com uma referência e discuti erros.
- [x] Registrei limitações, dados sintéticos, privacidade e vieses.
- [x] Formulei recomendações de apoio com revisão humana.
- [x] Respondi às questões individuais.
- [x] Conferi os links e os arquivos de evidências.
- [x] Substituí os campos PREENCHER ou justifiquei os não aplicáveis.

## Reflexão individual

- O que aprendi e consigo explicar: **A diferença entre classificação, regressão e agrupamento pelo significado do alvo; por que separar treino e teste e fazer a imputação só com o treino; como ler a matriz de confusão (acurácia, sensibilidade, falsos positivos e negativos); por que comparar com uma referência; e por que R² não é porcentagem de acertos.**
- Qual foi minha principal dificuldade: **[Escreva a sua, com sinceridade. Sugestão baseada no conteúdo: distinguir quando uma acurácia alta é enganosa (classes desbalanceadas) e entender por que a escolha de parâmetros não pode usar o teste.]**
- Qual evidência mostra meu avanço: **O notebook [laboratorio-equipe.ipynb](notebooks/laboratorio-equipe.ipynb), com resultados calculados (acurácia de teste 0,78 contra 0,5933 da referência; MAE 28,59 contra 84,73), os experimentos no treino e a matriz conferida manualmente.**
- Como contribuí com a equipe: **Não se aplica: trabalho individual.**
- O que preciso revisar: **Validação temporal em dados reais, avaliação por grupos (equidade) e outras métricas para classes desbalanceadas (precisão, recall, curva ROC).**
- Ferramentas de apoio utilizadas, incluindo IA quando houver, e como verifiquei as respostas: **Usei o Claude (Anthropic) como assistente de IA para executar o laboratório e redigir as respostas nos arquivos. Os números foram calculados por código (Python 3.13.18, scikit-learn 1.9.1, semente 42) e coincidiram com os do notebook de apoio; os cálculos manuais foram conferidos por código e a coerência entre arquivos e imagens foi revisada. Assumo a responsabilidade pelo conteúdo entregue e devo revisá-lo e ajustá-lo com minhas palavras antes de enviar.**

## Critérios de avaliação

Escala sugerida do material: nível 3 consistente, 2 adequado com lacunas, 1 parcial, 0 ausente/incoerente. Nota do critério = peso × nível/3. A professora pode ajustar a aplicação.

| Critério | Peso aula 1 | Peso aula 2/PBL |
| --- | --- | --- |
| Problema e conceitos | 3,0 | 2,0 |
| Dados e justificativa | 2,0 | 2,0 |
| Método e avaliação | 1,0 | 3,0 |
| Interpretação e responsabilidade | 2,0 | 2,0 |
| Clareza e colaboração | 2,0 | 1,0 |
| Total | 10,0 | 10,0 |

Na aula 1, método corresponde à avaliação proposta. Na aula 2, inclui execução e interpretação. A maior acurácia isolada não assegura a melhor avaliação da atividade.

## Fontes de apoio

- SCIKIT-LEARN. *User Guide*. https://scikit-learn.org/stable/user_guide.html.
- SCIKIT-LEARN. *Common pitfalls and recommended practices*. https://scikit-learn.org/stable/common_pitfalls.html.
- ORANGE DATA MINING. *Test and Score*. https://orangedatamining.com/widget-catalog/evaluate/testandscore/.

Referências indicadas no material didático do módulo, consultadas em 14 out. 2026. Registre a data da sua própria consulta quando utilizar novas fontes.

[Voltar ao início](README.md).
