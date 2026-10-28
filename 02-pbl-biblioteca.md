<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL — Biblioteca em Foco

## Identificação

- Estudante ou equipe: **Cléder Rafael Narciso de Araújo (atividade individual)**
- Turma: **Ciência de Dados e Aprendizagem de Máquina — quarta-feira, noturno**
- Data de realização: **28/10/2026**
- Integrantes e contribuições (se em equipe): **Não se aplica: realizado individualmente. Se houver equipe, incluir os nomes na tabela de colaboração abaixo.**

## Situação-problema

Uma biblioteca universitária enfrenta filas em horários específicos e baixa utilização de alguns serviços. A coordenação deseja melhorar o atendimento e planejar recursos. Este é um cenário didático.

**Público-alvo:** estudantes usuários, equipe de atendimento e gestão.

**Questão norteadora:** como os dados podem orientar o planejamento da biblioteca e a oferta de serviços sem identificar ou discriminar seus usuários?

## Investigação em equipe

1. Delimitem o problema e a decisão a apoiar.
2. Registrem o que já sabem e o que precisam investigar.
3. Formulem duas perguntas de negócio.
4. Definam a unidade de análise, os atributos e o alvo, quando houver.
5. Justifiquem a abordagem e indiquem se uma análise descritiva já seria suficiente.
6. Proponham avaliação, cuidados com os dados e limitações.

## Canvas da equipe

| Campo | Registro |
| --- | --- |
| Problema e decisão | Há filas em certos horários e serviços pouco usados. A decisão a apoiar é como distribuir a equipe de atendimento por horário e quais serviços divulgar, reorganizar ou rever. |
| Público-alvo | Estudantes usuários (beneficiários), equipe de atendimento (executa) e gestão (decide). |
| O que sabemos | Pelo enunciado: as filas se concentram em horários específicos e alguns serviços têm baixa utilização. Não sabemos quais horários, quais serviços nem os motivos; tudo isso precisa ser levantado. |
| O que precisamos investigar | Em que dias e horários as filas ocorrem; quanto tempo as pessoas esperam; quais serviços têm baixo uso e se isso decorre de falta de divulgação, de horário inadequado ou de baixa necessidade; o que os usuários dizem em pesquisa de satisfação. |
| Pergunta de negócio 1 | Quantos atendimentos devemos esperar por hora em cada dia da semana, para dimensionar a equipe de balcão? |
| Pergunta de negócio 2 | Existem perfis de uso dos serviços da biblioteca (por exemplo, quem usa só o acervo, quem usa salas de estudo, quem usa o acervo digital) que ajudem a decidir onde divulgar ou melhorar serviços pouco utilizados? |
| Unidade de análise e período | Pergunta 1: uma hora de funcionamento de um dia (série de horas ao longo de pelo menos um semestre inteiro, incluindo períodos de provas). Pergunta 2: um usuário, com dados agregados e pseudonimizados do mesmo período. |
| Atributos, unidades e origem pretendida | Pergunta 1: dia da semana, hora, semana do calendário acadêmico, proximidade de provas, número de atendentes (origem: sistema de empréstimo e escala interna). Pergunta 2: número de empréstimos, visitas, reservas de sala e acessos digitais por usuário no período (origem: sistema da biblioteca, com identificador pseudonimizado). |
| Alvo e momento em que será conhecido, ou ausência de alvo | Pergunta 1: alvo numérico, número de atendimentos na hora, conhecido ao fim da hora; usamos os atributos de calendário, que são conhecidos antes. Pergunta 2: ausência de alvo. |
| Abordagem e justificativa | Pergunta 1: regressão (supervisionada), pois o alvo é uma quantidade medida no histórico. Pergunta 2: agrupamento (não supervisionado), pois não há categorias prévias. Antes de qualquer modelo, fazer análise descritiva. |
| Alternativa sem ML | Uma análise descritiva (tabela e mapa de calor de atendimentos por dia e hora, média por período de provas e fora delas) já pode orientar a escala da equipe. Pesquisa de satisfação e conversa com usuários ajudam a entender serviços pouco usados. |
| Como avaliar a proposta | Regressão: separar treino e teste respeitando a ordem do tempo (treinar em semanas anteriores e testar em semanas posteriores); comparar o MAE (em atendimentos por hora) com uma referência simples, como a média histórica do mesmo dia e hora; examinar resíduos. Agrupamento: avaliar estabilidade dos grupos em amostras diferentes e se a equipe consegue interpretá-los e usá-los. Em ambos, verificar se a decisão de escala melhorou o tempo de espera. |
| Privacidade e limitações | Usar identificadores pseudonimizados ou dados agregados, coletar só o necessário, restringir acesso e definir prazo de retenção. Não usar atributos sensíveis nem perfis para restringir serviços a alguém. Limitações: períodos atípicos (greves, reformas) distorcem o histórico; a demanda que não aparece (quem desistiu da fila) não é registrada; perfis de uso não explicam motivos. |

## Registro de colaboração

| Integrante | Papel | Contribuição |
| --- | --- | --- |
| Cléder Rafael Narciso de Araújo | Autor único | Delimitação do problema, perguntas de negócio, definição de dados, abordagem e cuidados com privacidade. |

## Conclusão da equipe

**Proposta:** Começar por análise descritiva da demanda por dia e hora, que já orienta a escala. Em seguida, estimar a demanda por hora com regressão simples (calendário e proximidade de provas), comparada com a média histórica, e usar agrupamento apenas para entender perfis de uso dos serviços pouco utilizados, com dados pseudonimizados e revisão humana das decisões.

**Dúvida ainda aberta:** Os serviços pouco usados são desconhecidos por falta de divulgação ou realmente pouco necessários? Os dados de uso sozinhos não respondem; é preciso ouvir os usuários.

**Feedback recebido e melhoria realizada:** Ainda não recebido, por se tratar de trabalho individual sem apresentação realizada até o momento. Registrar aqui o retorno da professora ou dos colegas e a melhoria feita.

## Síntese para apresentação de dois minutos

A biblioteca tem filas em certos horários e serviços pouco usados. Proponho duas perguntas: quantos atendimentos esperar por hora (regressão, comparada com a média histórica) e que perfis de uso existem (agrupamento). Antes de modelar, uma análise descritiva já ajuda na escala da equipe. Os dados serão pseudonimizados e de acesso restrito, e as decisões terão revisão humana. O principal limite é que os dados mostram o uso, não os motivos de quem não usa.

## Entrega

Canvas preenchido e síntese para apresentação de dois minutos. Avaliar coerência da pergunta, dados, abordagem, responsabilidade e colaboração. [Voltar ao início](README.md).
