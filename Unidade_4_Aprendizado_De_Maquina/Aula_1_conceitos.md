<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Aula 1 — Conceitos e classificação de problemas

## Identificação

- Estudante ou equipe: **Cléder Rafael Narciso de Araújo (atividade individual)**
- Turma: **Ciência de Dados e Aprendizagem de Máquina — quarta-feira, noturno**
- Data de realização: **28/10/2026**
- Integrantes e contribuições (se em equipe): **Não se aplica: atividade individual.**

## Objetivos

Distinguir programação tradicional e Machine Learning, identificar atributos e alvo e diferenciar classificação, regressão e agrupamento.

## 1. Explicação com suas palavras

1. Como um modelo aprende com dados? **Ele recebe exemplos (atributos e, quando há, o resultado conhecido) e ajusta seus parâmetros internos para reduzir o erro nesses exemplos. O objetivo não é decorar os exemplos, e sim captar padrões que funcionem em dados novos. Por isso o desempenho se mede em dados que não participaram do aprendizado.**
2. Qual diferença entre algoritmo e modelo? **O algoritmo é o procedimento de aprendizado (por exemplo, o método que constrói uma árvore de decisão). O modelo é o resultado desse procedimento depois de rodar sobre dados específicos: a árvore já construída, com suas perguntas e limiares, que recebe um registro novo e devolve uma previsão. O mesmo algoritmo, com dados diferentes, gera modelos diferentes.**
3. Compare uma regra de bloqueio de palavra com um modelo de spam. **A regra é escrita por uma pessoa ("se a mensagem contém a palavra X, bloqueie"). Ela é transparente e previsível, mas só pega o que foi previsto e é fácil de contornar com pequenas variações. O modelo de spam aprende, a partir de mensagens já revisadas como spam ou legítimas, uma combinação de sinais (palavras, links, remetente, formato) e se adapta a padrões novos quando é retreinado. Em troca, depende de bons exemplos, pode errar nos dois sentidos e é mais difícil de explicar.**
4. Dê um exemplo de atributo e alvo e defina o momento da previsão. **No laboratório: atributos são frequência, nota e entregas até a semana 4; o alvo é `evasao_fim_semestre` (1 evadiu, 0 permaneceu). O momento da previsão é o fim da semana 4, usando apenas o que já é conhecido nesse instante; o alvo só é conhecido no fim do semestre.**
5. (Complemento) Diferença entre IA, Ciência de Dados e ML. **IA é o campo amplo de sistemas que realizam tarefas associadas à inteligência (inclui sistemas de regras). Ciência de Dados é o processo de extrair conhecimento de dados: coleta, limpeza, análise, comunicação e, quando útil, modelagem. ML é o subconjunto de IA em que o sistema aprende padrões a partir de dados. Exemplo: um filtro de spam é IA; a análise que mostra em que horários chegam mais spams é Ciência de Dados; o classificador treinado com mensagens rotuladas é ML.**

## 2. Quadro comparativo

| Critério | Supervisionado | Não supervisionado |
| --- | --- | --- |
| Presença de alvo no treino | Sim: cada exemplo traz o resultado conhecido (rótulo ou valor). | Não: só há atributos, sem resultado a prever. |
| Pergunta que pode responder | "Qual será o resultado para este caso?" (evadirá? quanto será vendido?) | "Que estrutura existe nos dados?" (há grupos, perfis, casos atípicos?) |
| Tipo de saída | Uma categoria (classificação) ou um número (regressão). | Grupos, regiões densas, pontuação de atipicidade ou representação reduzida. |
| Tarefas e exemplo | Classificação: spam ou legítima. Regressão: estimar empréstimos por semana. | Agrupamento: descobrir perfis de acesso ao ambiente virtual. |
| Dados necessários | Atributos mais alvo conhecido para muitos casos passados. | Apenas atributos, em quantidade e qualidade suficientes. |
| Forma de avaliação | Comparar previsões com o alvo real em dados de teste: acurácia, matriz de confusão, sensibilidade, MAE, R². | Não há gabarito: usa-se coerência interna dos grupos, estabilidade, interpretabilidade e utilidade para quem decide. |
| Limitação | Rotular custa caro e o rótulo pode ser enviesado ou tardio; o modelo reproduz o padrão do histórico. | Os grupos não têm significado garantido, dependem de escolhas (número de grupos, escala) e exigem interpretação humana. |

## 3. Situações-problema

Os casos são cenários didáticos. Escolha **pelo menos cinco** e justifique sua classificação pelo significado do alvo ou por sua ausência.

| Caso | Situação-problema |
| --- | --- |
| 1 Educação | Prever evadiu/permaneceu com histórico rotulado de turmas anteriores. |
| 2 Saúde | Estimar o tempo de espera em minutos a partir de registros de atendimento. |
| 3 Comércio | Descobrir perfis de compra sem categorias prévias de clientes. |
| 4 Finanças | Prever inadimplente/adimplente com contratos e desfechos conhecidos. |
| 5 Segurança digital | Distinguir spam/legítima com mensagens já revisadas. |
| 6 Comércio | Estimar o total de vendas em reais na próxima semana. |
| 7 Educação | Agrupar perfis de acesso ao ambiente virtual sem rótulo de evasão. |
| 8 Saúde | Classificar exames em categorias previamente definidas por especialistas. |

| Caso escolhido | Alvo ou ausência de alvo | Categoria, quantidade ou grupos? | Abordagem e justificativa | Dados necessários e limitação |
| --- | --- | --- | --- | --- |
| 1 Educação | Alvo: evadiu/permaneceu, conhecido no fim do período em turmas passadas. | Categoria (duas classes). | Aprendizado supervisionado, classificação: há rótulo histórico e a pergunta é qual classe. | Frequência, notas, entregas até a data da previsão e o desfecho final. Limitação: evasão tem causas que os dados não captam; risco de rotular e tratar estudantes de forma injusta. |
| 2 Saúde | Alvo: tempo de espera em minutos. | Quantidade (número contínuo). | Supervisionado, regressão: o resultado é um valor numérico medido em atendimentos passados. | Horário, dia, tipo de serviço, equipe disponível, fila no momento e tempo real de espera. Limitação: eventos raros (surtos) fogem do padrão e as previsões perdem validade fora do que foi observado. |
| 3 Comércio | Ausência de alvo: não há categorias prévias. | Grupos (perfis de cliente). | Não supervisionado, agrupamento: a meta é descobrir estrutura, não prever um rótulo. | Frequência, valor e variedade de compras por cliente, em escala comparável. Limitação: os grupos dependem de escolhas técnicas e só valem se forem interpretáveis e úteis. |
| 5 Segurança digital | Alvo: spam ou legítima, definido por revisão humana. | Categoria (duas classes). | Supervisionado, classificação: há mensagens já revisadas para aprender. | Texto, remetente, links e a revisão de cada mensagem. Limitação: os spammers mudam de estratégia, a revisão pode errar e bloquear mensagem legítima tem custo. |
| 6 Comércio | Alvo: total de vendas em reais na semana seguinte. | Quantidade (número contínuo). | Supervisionado, regressão (com atenção à ordem temporal, por haver sazonalidade). | Vendas semanais anteriores, promoções, calendário e preços. Limitação: previsão para períodos fora do histórico (crise, evento novo) é uma extrapolação pouco confiável. |
| 7 Educação | Ausência de alvo: sem rótulo de evasão. | Grupos (perfis de acesso). | Não supervisionado, agrupamento: descobrir padrões de uso sem desfecho definido. | Registros de acesso (frequência, horários, tempo, recursos usados). Limitação: um grupo não diz por que os estudantes se comportam assim, e rotular grupos pode estigmatizar. |

## 4. Raciocínio crítico

“Detectar fraude” define sozinho o tipo de aprendizado? Compare o uso de exemplos rotulados e a busca de operações atípicas sem rótulos. **Não. O objetivo "detectar fraude" admite as duas formulações e o que decide é quais dados existem. Se a instituição tem um histórico de operações confirmadas como fraude ou legítimas, pode treinar um classificador supervisionado: ele reconhece padrões já conhecidos e é avaliável com métricas (sensibilidade, precisão), mas sofre com poucas fraudes em relação ao total (classes desbalanceadas), com rótulos que chegam tarde e com fraudes novas que não se parecem com as passadas. Sem rótulos, pode-se usar detecção de anomalias (não supervisionada): ela busca operações atípicas e pode revelar esquemas inéditos, mas "atípico" não significa "fraudulento" (uma compra grande e legítima também é rara), gera muitos alertas falsos e é difícil de avaliar sem gabarito. Na prática, combinam-se as abordagens: anomalias geram casos para análise humana e os casos confirmados viram rótulos para treinar um modelo supervisionado.**

## Entrega

Salve este arquivo preenchido. Critérios: distinção conceitual, pertinência dos dados, justificativa e clareza. [Voltar ao início](README.md).
