### **TEMPLATE** 

# Definição do Projeto de Ciência de Dados 

### **Unidade III - Gestão de Projetos** 

**Equipe: Cléder Rafael Narciso de Araújo Turma: Sistemas de Informação Professor(a): Ranieri Azevedo Magalhães** 

**Data: 16/09/26** 



##### **PBL + trabalho em equipes** 

Defina um problema real, o público-alvo, os objetivos e as perguntas de negócio antes de iniciar a análise. 

**Unidade:** III - Gestão de Projetos **Metodologia:** PBL + trabalho em equipes **Entregável:** Documento de definição do projeto 

**Finalidade:** delimitar um problema real e orientar o desenvolvimento do projeto de Ciência de Dados. Preencha todos os campos com informações objetivas, verificáveis e coerentes entre si. 

## 1. Identificação do projeto 

|**Campo**|**Preenchimento**|
|---|---|
|Título provisório do projeto|MilitarySchedule|
|Curso / disciplina|Sistemas de Informação|
|Turma|Sistemas de Informação|
|Equipe|Cléder Rafael Narciso de Araújo|
|Integrantes e funções iniciais|Cléder Rafael Narciso de Araújo|
|Professor(a)|Ranieri Azevedo Magalhães|
|Data de elaboração|16/09/26|
|Versão do documento|1º Versão|



## 2. Visão geral 

#### 2.1 Resumo do projeto 

Em até 100 palavras, apresente o problema, o público-alvo, a proposta de análise e o resultado esperado. 

###### **Preenchimento:** 

A Banda de Música Militar elabora manualmente, em planilhas e papel, as escalas de serviço previstas no RISG para um efetivo de cerca de 120 militares e aproximadamente 30 turnos mensais. O processo não valida restrições regulamentares, não garante equidade e não deixa rastro de alterações. O projeto desenvolve o MilitarySchedule — sistema web em PHP, MySQL e Bootstrap 5 — e analisa os dados por ele gerados (escalas, ocorrências e log de auditoria) para medir distribuição de serviços, faltas e substituições. Espera-se um sistema em uso, indicadores operacionais em painel e apoio à decisão do encarregado da escala. 

#### 2.2 Declaração do projeto em uma frase 

Nosso projeto utilizará **[dados ou fonte]** para compreender/prever **[fenômeno]** , apoiando **[público ou organização]** na decisão de **[decisão ou ação]** . 

###### **Versão da equipe:** 

Nosso projeto utilizará **os dados de escalas, ocorrências e auditoria da Banda de Música Militar, registrados no banco MySQL do MilitarySchedule** , para compreender **como os serviços regulamentares são distribuídos entre o efetivo e onde ocorrem faltas, atrasos e substituições** , apoiando **o encarregado da escala e o comando da Organização Militar** na decisão de **quem escalar em cada turno, garantindo conformidade com o RISG e equidade na carga de serviço** . 

## 3. Contexto e definição do problema 

#### 3.1 Contexto 

Descreva a situação atual, o ambiente em que o problema ocorre e as evidências iniciais que demonstram sua relevância. 

- Onde o problema ocorre? 

- Quem é afetado? 

- Quais sinais, dados ou relatos indicam sua existência? 

- Por que é importante investigá-lo agora? 

###### **Preenchimento:** 

O problema ocorre na Banda de Música Militar, Organização Militar com efetivo fixo de músicos sujeita ao Regulamento Interno dos Serviços Gerais (RISG), que obriga a distribuição dos serviços de Permanência, Cabo de Dia, Sargento de Dia e Sargento da Barreira entre todos os militares ativos. 

- **Onde ocorre:** na seção administrativa responsável pela confecção da escala mensal, hoje feita em planilhas eletrônicas e registros em papel. 

- **Quem é afetado:** os cerca de 120 militares do efetivo (escalados), o militar encarregado de montar a escala e o comando, responsável pela regularidade do serviço. 

- **Sinais e evidências:** relatos dos militares da Banda sobre as dificuldades do processo manual (coletados na pesquisa); ocorrência de militares em férias, licença ou missão aparecendo na escala; impossibilidade de identificar quem alterou um turno; ausência de qualquer registro consolidado de faltas e substituições. 

- **Por que agora:** já existe um protótipo funcional (Escala v1) em uso informal, sem autenticação e vulnerável a SQL Injection, tratando dados pessoais de militares — situação incompatível com a LGPD e com o princípio de auditabilidade exigido de sistemas de pessoal. 

#### 3.2 Problema central 

Formule o problema de maneira específica, sem antecipar uma solução. 

**Modelo:** [Público/organização] enfrenta [problema observável] no contexto de [situação], produzindo [consequência ou impacto]. 

###### **Problema definido:** 

A Banda de Música Militar enfrenta a elaboração manual e não rastreável das escalas de serviço no contexto das obrigações do RISG sobre um efetivo de aproximadamente 120 militares e 30 turnos mensais, produzindo escalação de militares indisponíveis, distribuição desigual da carga de serviço, retrabalho administrativo e impossibilidade de auditar alterações. 

3.3 Evidências iniciais 

|**Evidência**|**Fonte**|**O que ela indica?**|**Confiabilidade /**<br>**limitação**|
|---|---|---|---|
|1.<br>Relatos<br>dos<br>militares da Banda<br>sobre<br>erros<br>e<br>retrabalho<br>na<br>montagem manual<br>da escala|Levantamento<br>de<br>requisitos junto aos<br>militares da Banda<br>(2025–2026)|O processo manual é<br>percebido como falho<br>e custoso por quem o<br>executa e por quem<br>é escalado|Qualitativa e local;<br>não<br>quantifica<br>frequência dos erros|
|2. Protótipo Escala v1<br>sem<br>autenticação,<br>sem<br>campo<br>`status_militar`<br>e<br>com<br>`real_escape_string`<br>no lugar de prepared<br>statements|Análise do código-<br>fonte do sistema<br>original (Cap. 1.2.1<br>do TCC)|Militares<br>indisponíveis podiam<br>ser escalados e<br>qualquer pessoa com<br>a URL podia alterar<br>dados|Evidência<br>técnica<br>verificável; limitada<br>ao<br>protótipo<br>analisado|
|3.<br>Volume<br>combinatório: ~120<br>militares × ~30<br>turnos<br>mensais,<br>problema classificado<br>como NP-difícil (CSP)|Garey e Johnson<br>(1979); modelagem<br>(X, D, C) no Cap. 2.1<br>do TCC|A montagem manual<br>é inviável de otimizar<br>sem<br>apoio<br>computacional<br>e<br>filtros<br>de<br>elegibilidade|Argumento teórico; o<br>efetivo real que<br>concorre à escala é<br>menor que 120|



## 4. Público-alvo e partes interessadas 

#### 4.1 Público-alvo principal 

|**Aspecto**|**Descrição**|
|---|---|
|Quem são os usuários ou beneficiários?|Militar<br>encarregado<br>da<br>escala<br>(perfil<br>Administrador) e os militares do efetivo escalados<br>(perfil Militar)|
|Quais necessidades possuem?|Montar a escala mensal respeitando o RISG,<br>saber quem está disponível, registrar ocorrências<br>e consultar com antecedência os próprios<br>serviços|
|Como são afetados pelo problema?|O encarregado gasta horas em conferências<br>manuais e responde por erros; os militares<br>sofrem com escalas desiguais, avisos tardios e<br>alterações sem registro|
|Que decisão ou ação poderão tomar com os resultados?|Definir quem escalar em cada turno, remanejar<br>militares<br>indisponíveis,<br>tratar<br>faltas<br>e<br>substituições e corrigir desequilíbrios na carga<br>acumulada|



#### 4.2 Partes interessadas 

|**Parte interessada**|**Interesse no projeto**|**Influência**|**Forma de envolvimento**|
|---|---|---|---|
|Comando<br>da<br>Organização Militar|Regularidade<br>do<br>serviço,<br>conformidade com o<br>RISG<br>e<br>responsabilização<br>rastreável|Alta|Aprovação do uso do<br>sistema e validação<br>das<br>regras<br>de<br>negócio|
|Militar encarregado<br>da<br>escala<br>(Administrador)|Reduzir tempo e<br>erros na montagem<br>da escala mensal|Alta|Usuário-chave: valida<br>requisitos,<br>testa<br>protótipos e opera o<br>sistema|
|Militares do efetivo<br>(escalados)|Equidade<br>na<br>distribuição e acesso<br>antecipado à escala|Média|Entrevistas<br>de<br>levantamento, uso<br>do portal do militar e<br>feedback<br>de<br>usabilidade|



## 5. Objetivos do projeto 

#### 5.1 Objetivo geral 

Escreva um objetivo que indique o que será analisado, para qual finalidade e em qual contexto. Inicie com um verbo no infinitivo. 

###### **Objetivo geral:** 

Desenvolver o MilitarySchedule, sistema web para gestão de escalas de serviço da Banda de Música Militar, com controle de acesso por perfil (RBAC), validação das restrições regulamentares do RISG e rastreabilidade completa das operações por log de auditoria, de modo a apoiar o encarregado da escala na alocação do efetivo. 

#### 5.2 Objetivos específicos 

Defina de três a cinco objetivos mensuráveis e compatíveis com o prazo do projeto. 

|**N**<br>**º**|**Objetivo específico**|**Evidência de conclusão**|
|---|---|---|
|1|Levantar os requisitos funcionais e não funcionais a<br>partir do RISG e da rotina operacional da Banda|Tabelas 2 e 3 do TCC: 10<br>requisitos funcionais e 6 não<br>funcionais, validados com o<br>encarregado da escala|
|2|Modelar o banco relacional MySQL com as entidades<br>`usuario`,`militar`,`tipo_servico`,`escala`,`ocorrencia`e<br>`log_auditoria`|DER completo e dicionário de<br>dados das seis tabelas; script<br>`banco.sql`<br>executado sem<br>erros|



|**N**<br>**º**|**Objetivo específico**|**Evidência de conclusão**|
|---|---|---|
|3|Implementar o sistema em PHP com PDO e prepared<br>statements em todas as operações DML|Código-fonte sem chamadas<br>a`mysqli`/`real_escape_string`;<br>testes de injeção de SQL sem<br>sucesso|
|4|Implementar controle de acesso RBAC com autenticação<br>bcrypt e log de auditoria de todas as operações CRUD|Tentativa de acesso do perfil<br>Militar a módulos do Admin<br>bloqueada; registros em<br>`log_auditoria`com usuário,<br>IP e timestamp|
|5|Construir interface responsiva em Bootstrap 5 com<br>dashboard de indicadores, escala mensal visual e filtros<br>combinados|Telas de dashboard, grade<br>mensal e listagens com filtro<br>por<br>mês<br>e<br>status<br>funcionando em desktop e<br>smartphone|



#### 5.3 Verificação dos objetivos 

Marque após revisar: 

- ☐ São específicos e escritos com clareza. 

- ☐ Podem ser verificados por meio de entregáveis ou métricas. 

- ☐ São viáveis com os dados, recursos e tempo disponíveis. 

- ☐ Estão diretamente relacionados ao problema central. 

- ☐ Consideram os usuários e a decisão que será apoiada. 

## 6. Perguntas de negócio 

As perguntas de negócio orientam a coleta, a análise e a comunicação dos resultados. Evite perguntas que possam ser respondidas apenas com “sim” ou “não”. 

|**Nº**|**Pergunta de**<br>**negócio**|**Decisão ap**|**oiada**|**Dados necessários**|**Análise ou**<br>**indicador**<br>**possível**|
|---|---|---|---|---|---|
|1|Como a carga<br>de serviço está<br>distribuída entre<br>os<br>militares<br>ativos ao longo<br>do mês?|Escolher<br>escalar<br>próximo<br>para equil<br>carga|quem<br>no<br>turno<br>ibrar a|`escala`<br>(militar_id,<br>data,<br>tipo_servico_id),<br>`militar`(status)|Contagem<br>e<br>horas<br>de<br>serviço<br>por<br>militar; desvio<br>em relação à<br>média|
|2|Quais tipos de<br>serviço<br>concentram<br>mais faltas e<br>substituições?|Reforçar<br>redistribui<br>turnos<br>críticos|ou<br>r os<br>mais|`ocorrencia`<br>(tipo,<br>escala_id),<br>`tipo_servico`|Percentual de<br>ocorrências por<br>tipo de serviço|
|3|Que proporção<br>do efetivo está|Antecipar<br>períodos|de|`militar.status_milit`<br>`ar`com histórico de|Proporção de<br>militares ativos|



|**Nº**|**Pergunta de**<br>**negócio**|**Decisão apoiada**|**Dados necessários**|**Análise ou**<br>**indicador**<br>**possível**|
|---|---|---|---|---|
||indisponível<br>(férias, licença,<br>missão)<br>em<br>cada período?|escassez<br>de<br>pessoal apto|alterações no log|sobre o efetivo<br>total, por mês|
|4|Quanto tempo<br>decorre entre o<br>cadastro<br>de<br>uma escala e<br>sua alteração<br>ou<br>cancelamento?|Definir prazo de<br>publicação da<br>escala<br>com<br>menor volume<br>de mudanças|`log_auditoria`(tabela<br>afetada,<br>registro,<br>timestamp)|Intervalo médio<br>entre criação e<br>edição de um<br>mesmo turno|
|5|Quem realiza as<br>alterações nas<br>escalas e em<br>que momento<br>do<br>ciclo<br>mensal?|Definir<br>responsabilidad<br>es e regras de<br>bloqueio<br>da<br>escala publicada|`log_auditoria`<br>(usuário,<br>IP,<br>operação,<br>timestamp)|Distribuição das<br>operações por<br>usuário e por<br>dia do mês|



## 7. Hipóteses iniciais 

Registre suposições que serão investigadas, sem apresentá-las como conclusões. 

|**Hipótese**|**Como poderá ser testada?**|**Resultado que a refutaria?**|
|---|---|---|
|H1. A distribuição de serviços<br>no processo manual é<br>desigual: parte do efetivo<br>assume<br>carga<br>significativamente acima da<br>média|Comparar a contagem de<br>turnos por militar nas escalas<br>históricas (planilhas) e nas<br>geradas pelo sistema|Contagem por militar com<br>dispersão baixa, próxima da<br>distribuição uniforme|
|H2. Uma parcela relevante<br>das escalas do processo<br>manual envolve militares<br>indisponíveis no momento do<br>serviço|Cruzar escalas históricas<br>com registros de férias,<br>licença e missão do período|Nenhum ou pouquíssimos<br>casos de escalação de militar<br>indisponível|
|H3. O filtro automático por<br>`status_militar = 'Ativo'`<br>reduz correções posteriores<br>da escala|Comparar o número de<br>edições por escala antes e<br>depois da adoção do<br>sistema,<br>usando<br>o<br>`log_auditoria`|Volume de edições por<br>escala igual ou maior após a<br>adoção do sistema|



## 8. Dados necessários e viabilidade 

|**Conjunto ou**<br>**fonte de dados**|**Variáveis principais**||**Formato**|**Acesso /**<br>**responsável**|**Qualidade**<br>**esperada**|
|---|---|---|---|---|---|
|Tabela`militar`|nome,|patente,|MySQL / SQL|Administrador|Alta<br>—|



|**Conjunto ou**<br>**fonte de dados**|**Variáveis principais**|**Formato**|**Acesso /**<br>**responsável**|**Qualidade**<br>**esperada**|
|---|---|---|---|---|
|(MilitarySchedu<br>le)|instrumento/função, data de<br>ingresso, telefone, e-mail,<br>`status_militar`||do<br>sistema<br>(encarregado<br>da escala)|cadastro<br>controlado,<br>campos<br>obrigatórios<br>e ENUM de<br>status|
|Tabela`escala`|militar_id,<br>tipo_servico_id,<br>data, hora início/fim, local,<br>status, observação|MySQL / SQL|Administrador<br>do sistema|Alta<br>—<br>integridade<br>referencial e<br>seleção<br>restrita<br>a<br>militares<br>ativos|
|Tabela<br>`ocorrencia`|escala_id,<br> `tipo_ocorrencia`<br>(Falta/Substituição/Atraso/Ou<br>tro), descrição, data|MySQL / SQL|Administrador<br>do sistema|Média/alta —<br>depende do<br>registro<br>tempestivo<br>pelo<br>encarregado|



#### 8.1 Avaliação inicial dos dados 

- **Disponibilidade:** os dados operacionais nascem no próprio sistema, em ambiente local XAMPP; as escalas históricas dependem de autorização da seção administrativa da Banda. 

- **Volume e período coberto:** efetivo de aproximadamente 120 militares e cerca de 30 turnos mensais; base do sistema cobre o período a partir de sua implantação, e as planilhas históricas cobrem os meses anteriores disponíveis. 

- **Dados ausentes, duplicados ou inconsistentes previstos:** nomes grafados de formas diferentes nas planilhas, trocas de serviço anotadas apenas à mão, ocorrências registradas fora do prazo e ausência de horário de fim em registros antigos. 

- **Necessidade de integração entre fontes:** sim — o histórico em planilhas precisa ser padronizado e vinculado ao cadastro de militares do sistema por identificador único. 

- **Restrições legais, contratuais ou institucionais:** dados pessoais de militares, sujeitos à LGPD (RNF06) e a normas internas da OM; qualquer divulgação externa exige anonimização e autorização do comando. 

#### 8.2 Privacidade, ética e segurança 

- ☐ A equipe verificou se há dados pessoais ou sensíveis. 

- ☐ A coleta e o uso dos dados possuem finalidade legítima e explícita. 

- ☐ O acesso será limitado às pessoas autorizadas. 

- ☐ Dados pessoais serão minimizados, anonimizados ou pseudonimizados quando necessário. 

- ☐ Possíveis vieses e impactos sobre grupos serão analisados. 

- ☐ A divulgação dos resultados evitará reidentificação ou exposição indevida. 

###### **Cuidados específicos deste projeto:** 

o cadastro contém nome, patente, telefone e e-mail de militares. Senhas são armazenadas apenas como hash bcrypt com custo mínimo 12 (RNF02) e nunca em texto claro. Todas as consultas usam PDO 

com prepared statements (RNF03). O acesso é segmentado por perfil: o Militar visualiza somente os próprios serviços e o log de auditoria é exclusivo do Administrador. Nas telas, relatórios e no texto do TCC, os militares aparecem com dados fictícios ou identificadores anônimos (ex.: "Militar A"), sem patente combinada com nome real, para evitar reidentificação. A análise de equidade considera o risco de viés por segmento (ex.: sargentos do segmento feminino e masculino na Barreira) e informa o efetivo de cada grupo ao comparar cargas. 

## 9. Escopo do projeto 

|**Dentro do escopo**|**Fora do escopo**|
|---|---|
|CRUD de militares, tipos de serviço, escalas<br>e ocorrências|Geração automática da escala por algoritmo<br>(backtracking)|
|Controle de acesso RBAC com dois perfis e<br>autenticação bcrypt|Integração com sistemas corporativos do<br>Exército (SISG e afins)|
|Escala mensal visual (grade dias × militares)<br>e filtros combinados|Notificação automática por e-mail ou<br>aplicativo de mensagens|



**Restrições conhecidas:** tempo, acesso a dados, ferramentas, infraestrutura, conhecimento técnico ou normas. 

Prazo do TCC (semestre letivo); desenvolvimento por um único aluno, o que limita o volume de funcionalidades; acesso a dados reais de pessoal condicionado à autorização da OM, o que pode exigir uso de dados fictícios nas demonstrações; ambiente de execução limitado ao XAMPP local; normas internas e RISG como restrição de regras de negócio. 

## 10. Resultados e entregáveis previstos 

|**Entregável**|**Descrição**|**Formato**|**Responsável**|**Critério de**<br>**aceite**|
|---|---|---|---|---|
|Base<br>tratada|Base tratada|Banco MySQL com as seis<br>tabelas, integridade<br>referencial e dados de<br>demonstração<br>anonimizados|`banco.sql`+<br>dump|Cléder Araújo|
|Análise<br>exploratória|Análise<br>exploratória|Levantamento da<br>distribuição de serviços<br>por militar, ocorrências<br>por tipo e operações no<br>log|Consultas SQL +<br>capítulo do TCC|Cléder Araújo|
|Visualizaçõe<br>s / painel|Visualizações /<br>painel|Dashboard com cards<br>(militares ativos, escalas,<br>faltas e ocorrências do<br>mês) e grade mensal<br>visual|Aplicação web<br>(PHP +<br>Bootstrap 5)|Cléder Araújo|
|Relatório ou<br>apresentaçã<br>o|Sistema<br>MilitarySchedule|Aplicação com CRUD<br>completo, RBAC, dois<br>portais e log de auditoria|Código-fonte +<br>repositório<br>GitHub|Cléder Araújo|



|**Entregável**|**Descrição**|**Formato**|**Responsável**|**Critério de**<br>**aceite**|
|---|---|---|---|---|
|Outro|Relatório ou<br>apresentação|Monografia em normas<br>ABNT e apresentação<br>para a banca|PDF / slides|Cléder Araújo|



## 11. Critérios de sucesso 

Defina como a equipe saberá se o projeto alcançou seus objetivos. 

|**Critério**|**Indicador ou evidência**|**Meta**|**Forma de verificação**|
|---|---|---|---|
|Relevância para o<br>problema|Fragilidades do Escala<br>v1 corrigidas (Tabela 1<br>do TCC)|10 de 10 itens do<br>comparativo atendidos|Checklist item a item<br>com demonstração em<br>tela|
|Qualidade dos dados|Registros de escala<br>com militar, tipo, data<br>e horário completos e<br>íntegros|100% dos registros<br>sem violação de chave<br>estrangeira ou campo<br>obrigatório vazio|Consultas de<br>verificação no MySQL|
|Qualidade da análise|Perguntas de negócio<br>respondidas com<br>consulta reproduzível|5 de 5 perguntas<br>respondidas|Revisão da orientadora<br>sobre as consultas e<br>resultados|
|Utilidade para o<br>público-alvo|Avaliação do<br>encarregado da escala<br>após uso do protótipo|Parecer favorável<br>quanto à redução de<br>esforço e de erros|Sessão de teste com o<br>usuário-chave e<br>registro de feedback|
|Comunicação dos<br>resultados|Monografia em ABNT e<br>apresentação à banca|Aprovação com todas<br>as seções obrigatórias|Avaliação da banca<br>examinadora|



## 12. Plano inicial de trabalho 

|**Etapa**|**Atividades**<br>**principais**|**Responsável(is)**|**Prazo**|**Dependências**|
|---|---|---|---|---|
|1. Definição|Estudo do RISG,<br>análise do<br>Escala v1,<br>trabalhos<br>correlatos (SISG,<br>FET) e<br>levantamento<br>de requisitos|Cléder Araújo|Mês 1|Acesso aos<br>militares da<br>Banda e ao<br>código do<br>protótipo|
|2. Obtenção dos<br>dados|Definição das<br>entidades,<br>coleta das<br>escalas<br>históricas e<br>montagem do<br>conjunto de<br>demonstração|Cléder Araújo|Mês 2|Autorização da<br>seção<br>administrativa;<br>conclusão da<br>etapa 1|



|**Etapa**|**Atividades**<br>**principais**|**Responsável(is)**|**Prazo**|**Dependências**|
|---|---|---|---|---|
|3. Preparação<br>dos dados|Modelagem do<br>DER, criação do<br>`banco.sql`,<br>padronização e<br>anonimização<br>dos dados<br>históricos|Cléder Araújo|Mês 2–3|Etapa 2|
|4. Análise /<br>modelagem|Implementação<br>dos módulos em<br>PHP/PDO, RBAC,<br>dashboard,<br>grade mensal e<br>log de auditoria|Cléder Araújo|Mês 3–4|Etapa 3;<br>ambiente XAMPP<br>configurado|
|5. Validação|Testes<br>funcionais dos<br>RF01–RF10,<br>teste de injeção<br>de SQL, teste de<br>usabilidade com<br>o encarregado|Cléder Araújo,<br>usuário-chave|Mês 5|Etapa 4|
|6. Comunicação|Redação da<br>monografia em<br>ABNT, revisão<br>com a<br>orientadora e<br>preparação da<br>defesa|Cléder Araújo,<br>Profa. Dra. Kerlla<br>Luz|Mês 5–6|Etapa 5|



## 13. Riscos do projeto 

|**Risco**|**Probabilidade**|**Impacto**|**Estratégia de**<br>**resposta**|**Responsável**|
|---|---|---|---|---|
|Não obter<br>autorização para<br>usar dados reais<br>de pessoal<br>militar|Média|Médio|Trabalhar com<br>base de<br>demonstração<br>anonimizada e<br>validar as regras<br>com o usuário-<br>chave|Cléder Araújo|
|Escalas<br>históricas em<br>planilhas e papel<br>com baixa<br>padronização|Alta|Médio|Limitar a análise<br>histórica a um<br>recorte de<br>meses e<br>documentar as<br>limitações|Cléder Araújo|
|Escopo<br>excessivo para o<br>prazo (tentação<br>de implementar|Média|Alto|Manter a<br>geração<br>automática<br>como trabalho|Cléder Araújo /<br>orientadora|



|**Risco**|**Probabilidade**|**Impacto**|**Estratégia de**<br>**resposta**|**Responsável**|
|---|---|---|---|---|
|o motor<br>automático de<br>escala)|||futuro e priorizar<br>os RF de<br>prioridade Alta||



## 14. Organização da equipe 

|**Integrante**|**Papel principal**|**Responsabilidades**|**Apoio necessário**|
|---|---|---|---|
|Cléder Rafael Narciso<br>de Araújo|Autor e<br>desenvolvedor|Levantamento de<br>requisitos,<br>modelagem,<br>implementação,<br>testes, análise e<br>redação|Orientação<br>metodológica e<br>acesso ao contexto<br>operacional|
|Profa. Dra. Kerlla Luz|Orientadora|Direcionamento<br>técnico e<br>metodológico,<br>revisão dos capítulos<br>e validação das<br>entregas|Disponibilidade de<br>reuniões periódicas<br>de acompanhamento|
|Militar encarregado<br>da escala|Usuário-chave<br>(validador)|Fornecer as regras<br>do RISG na prática,<br>validar requisitos e<br>testar o protótipo|Liberação do<br>comando para<br>participar das<br>sessões|
|Militares da Banda de<br>Música|Fonte de informação|Relatar dificuldades<br>do processo manual<br>e avaliar o portal do<br>militar|Tempo em horário de<br>expediente|



## 15. Validação da definição do projeto 

Antes da entrega, confirme: 

- ☐ O problema é real, relevante e delimitado. 

- ☐ O público-alvo e as partes interessadas estão identificados. 

- ☐ O objetivo geral e os objetivos específicos são coerentes. 

- ☐ As perguntas de negócio orientam decisões concretas. 

- ☐ Há dados potencialmente disponíveis para responder às perguntas. 

- ☐ O escopo é compatível com o prazo e os recursos. 

- ☐ Os critérios de sucesso são mensuráveis. 

- ☐ Riscos, privacidade, ética e segurança foram considerados. 

- ☐ Funções e responsabilidades foram distribuídas. 

## 16. Aprovação e registro de ajustes 

|**Responsável**|**Validação / observação**|**Data**|
|---|---|---|
|Representante da<br>equipe — Cléder Rafael<br>Narciso de Araújo||/    /|
|Professor(a) /<br>orientador(a) — Prof.||/    /|
|Ranieri Azevedo<br>Magalhães|||



Ajustes solicitados após a apresentação inicial 

