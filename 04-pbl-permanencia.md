<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL integrador — Apoio à Permanência

## Identificação

- Estudante ou equipe: **Cléder Rafael Narciso de Araújo (atividade individual)**
- Turma: **Ciência de Dados e Aprendizagem de Máquina — quarta-feira, noturno**
- Data de realização: **28/10/2026**
- Integrantes e contribuições (se em equipe): **Não se aplica: atividade individual.**

## Contexto

Uma instituição quer compreender sinais associados à evasão e oferecer apoio antes do fim do semestre. Público-alvo: estudantes matriculados e equipe de apoio acadêmico. O cenário é didático e a prática usa dados sintéticos.

**Questão norteadora:** como identificar situações que merecem atenção e oferecer apoio, reconhecendo erros do modelo e dificuldades que os dados não capturam?

## Proposta da equipe

### 1. Delimitação

- Problema e público: **Parte dos estudantes abandona o curso ao longo do semestre, muitas vezes sem que a instituição perceba a tempo. O público são estudantes matriculados (que podem receber apoio) e a equipe de apoio acadêmico (que acompanha os convites).**
- Decisão que o resultado pode apoiar: **Quais estudantes a equipe de apoio deve procurar primeiro, com um convite voluntário, na semana 4 do semestre. O modelo orienta a ordem de contato; ele não decide sobre o estudante.**
- Definição de evasão, unidade e horizonte: **Evasão: o estudante deixa de frequentar ou cancela a matrícula até o fim do semestre (`evasao_fim_semestre` = 1); permanência = 0. Unidade: um estudante em um semestre. Horizonte: previsão ao fim da semana 4, desfecho no fim do semestre. Em uma investigação real, essa definição deve ser fixada antes da coleta (por exemplo, como tratar trancamento temporário).**

### 2. Perguntas de negócio

1. **Com as informações disponíveis até a semana 4 (frequência, nota e entregas), quais estudantes têm maior chance de evadir até o fim do semestre e merecem um convite de apoio?**
2. **Quais sinais (baixa frequência, nota baixa, poucas entregas) mais se associam à evasão, para orientar o tipo de apoio oferecido?**

### 3. Dados necessários

| Dado | Papel no projeto | Disponível quando? | Origem pretendida | Necessidade e risco |
| --- | --- | --- | --- | --- |
| Frequência até a semana 4 (%) | Atributo | Fim da semana 4 | Diário de classe/sistema acadêmico | Necessário; risco de registro incompleto e de interpretar falta justificada como desinteresse. |
| Nota até a semana 4 (0 a 10) | Atributo | Fim da semana 4 | Sistema acadêmico | Necessário; há ausências (5% no conjunto), e notas variam por professor e disciplina. |
| Entregas até a semana 4 (0 a 8) | Atributo | Fim da semana 4 | Ambiente virtual de aprendizagem | Necessário; depende de como cada disciplina cobra atividades. |
| Evasão no fim do semestre | Alvo | Fim do semestre | Secretaria acadêmica | Necessário apenas para treinar e avaliar; definição ambígua pode distorcer o modelo. |
| Identificador do estudante | Vínculo para o contato | Sempre | Secretaria | Não entra no modelo; só a equipe autorizada acessa, para realizar o convite; risco de exposição. |

Diferencie dados usados na simulação e dados que seriam necessários para uma investigação real: **Na simulação, são usados 600 registros fictícios com três atributos e o alvo, gerados por uma função que define as relações, sem identificadores. Em uma investigação real seriam necessários dados de várias turmas e períodos, com definição formal de evasão, informações sobre cursos e contexto (por exemplo, trabalho e deslocamento, se o estudante consentir e houver base legal), registro de quem recebeu apoio e o resultado, avaliação temporal e aprovação ética e de proteção de dados.**

### 4. Abordagem e algoritmo

- Classificação, regressão ou outra formulação, com justificativa: **Classificação binária supervisionada: o alvo é uma categoria (evadiu ou permaneceu) e há histórico rotulado.**
- Algoritmo introdutório escolhido: **Árvore de decisão (com imputação pela mediana), pois produz perguntas simples que a equipe de apoio consegue ler e discutir.**
- Referência simples: **`DummyClassifier` que sempre prevê a classe mais frequente (permaneceu).**

### 5. Avaliação

- Preparação, divisão e validação: **Imputação aprendida só no treino (Pipeline); divisão estratificada de 75% treino (450) e 25% teste (150), semente 42; escolha da profundidade por validação cruzada estratificada de 5 partes no treino; teste usado uma vez ao final. Em dados reais, a divisão deveria respeitar o tempo (treinar em turmas passadas e testar em turma posterior).**
- Métricas e razão da escolha: **Acurácia (visão geral), matriz de confusão e sensibilidade da classe 1, porque o erro mais custoso é deixar de apoiar quem evadiria; precisão, para saber quantos convites seriam desnecessários. A acurácia sozinha não basta, pois depende da proporção das classes.**
- Resultados efetivamente calculados e link da evidência: **Árvore com profundidade 5 e folha mínima 10: acurácia de treino 0,8133, de validação 0,7222 ± 0,0391, de teste 0,7800 (referência: 0,5933). Matriz do teste: TN=75, FP=14, FN=19, TP=42; sensibilidade 0,6885; precisão 0,75. Evidências: [notebooks/laboratorio-equipe.ipynb](notebooks/laboratorio-equipe.ipynb), [matriz](assets/matriz-confusao.png) e o registro em [03-aula2-laboratorio.md](03-aula2-laboratorio.md).**
- Erros relevantes e consequências: **Os 19 falsos negativos são estudantes em risco que não seriam procurados; os 14 falsos positivos receberiam um convite desnecessário (baixo custo, pois é voluntário). Como o teste tem só 150 registros e uma única divisão, os números têm incerteza e não devem ser lidos como garantia.**

### 6. Limites e proteção

- Por que os resultados não demonstram causalidade? **O modelo capta associações entre atributos e desfecho. Baixa frequência pode ser consequência de problemas externos (trabalho, saúde, transporte, dificuldades financeiras) que também levam à evasão, ou a própria decisão de sair pode reduzir a frequência. Além disso, as associações do conjunto foram definidas pela simulação.**
- Por que dados sintéticos não validam uso institucional? **Eles não trazem a complexidade, o ruído, os vieses nem a diversidade de estudantes reais; as relações são as que o autor da simulação escolheu. O resultado mostra o funcionamento do método, não que ele funcionaria na instituição.**
- Que grupos podem ser mal representados? Como investigar isso com evidências apropriadas? **Grupos pouco numerosos ou com padrões diferentes (por exemplo, estudantes que trabalham, de cursos noturnos, com deficiência, de ingresso por cotas, ou de cursos com poucos alunos) podem ter mais erros. Investigar com dados reais autorizados, comparando sensibilidade, falsos positivos e falsos negativos por grupo, com amostras suficientes, e envolvendo estudantes e especialistas. Este conjunto sintético não tem grupos, portanto não permite afirmar equidade.**
- Como minimizar dados, restringir acesso e definir retenção? **Usar apenas os atributos necessários, não coletar dados sensíveis sem justificativa e base legal, manter identificadores separados dos dados do modelo, liberar acesso apenas à equipe de apoio autorizada, com registro de acessos, e apagar ou anonimizar os dados após um prazo definido (por exemplo, ao fim do período de avaliação do projeto).**
- Como garantir revisão humana e contestação? **A sinalização é só um aviso: um profissional de apoio avalia o caso antes de qualquer contato; o estudante pode recusar o convite, pedir esclarecimento e solicitar correção ou exclusão de seus dados; nenhuma consequência acadêmica pode decorrer automaticamente da previsão.**

### 7. Recomendações de apoio

- Ação voluntária proposta: **Convite personalizado, feito por uma pessoa da equipe de apoio, para uma conversa e oferta de opções (monitoria, plantão de dúvidas, orientação de estudos, apoio social), sem condicionar nada ao aceite.**
- Como acolher estudantes não sinalizados pelo modelo: **Manter canais abertos para qualquer estudante pedir ajuda, divulgar os serviços para toda a turma e orientar professores a encaminhar casos que percebam, já que o modelo deixa passar parte dos casos (sensibilidade de cerca de 69% no teste).**
- O que precisa ser verificado antes de aplicação real: **Validação com dados reais e avaliação temporal; análise por grupos; definição formal de evasão; aprovação do comitê de ética e do encarregado de proteção de dados (LGPD); teste piloto com acompanhamento; medir se o apoio melhora a permanência, e não apenas se o modelo acerta; plano de revisão periódica.**

Previsões não são certezas. Priorize apoio e revisão humana, sem punições ou decisões automáticas prejudiciais.

## Apresentação de cinco minutos

| Tempo | Conteúdo | Responsável |
| --- | --- | --- |
| 1 minuto | Problema e dados | Cléder Rafael Narciso de Araújo |
| 2 minutos | Método e resultados | Cléder Rafael Narciso de Araújo |
| 1 minuto | Limitações | Cléder Rafael Narciso de Araújo |
| 1 minuto | Recomendações de apoio | Cléder Rafael Narciso de Araújo |

## Contribuições

| Integrante | Contribuição verificável |
| --- | --- |
| Cléder Rafael Narciso de Araújo | Execução do laboratório ([notebook](notebooks/laboratorio-equipe.ipynb)) e redação desta proposta. Trabalho individual, com apoio de IA declarado em [06-autoavaliacao.md](06-autoavaliacao.md). |

[Voltar ao início](README.md).
