# Fase 5: Avaliação

## Objetivo central

Verificar se os resultados atendem aos critérios da Fase 1, usando o teste uma única vez, em países que o modelo não viu.

## Checklist de execução

- [x] **Avaliar os resultados**
  - [x] A (teste: 943 linhas, 41 países): MAE de 0,0901 em log10 (erro típico de ×1,23) e R² de 0,9667. Referência: MAE 0,5915 (×3,90). **Critério atendido.**
  - [x] B (teste: 533 janelas, 41 países): acurácia 0,7842 (418 acertos), referência 0,6660, AUC 0,8286. Matriz: 284 / 71 / 44 / 134. Sensibilidade 0,7528; precisão 0,6537. **Critério atendido.**
  - [x] C: silhueta 0,533 com 3 grupos. Os grupos são descritíveis (renda baixa, média e alta com muita energia e metano), mas um tem só 8 países e outro é heterogêneo (99). **Critério atendido em parte.**
- [x] **Rever o processo**
  - [x] Sem vazamento: imputação dentro do `Pipeline`; atributos da classificação só do ano inicial ou anteriores; as emissões por combustível não entram na regressão; nenhum país nos dois lados da separação.
- [x] **Determinar os próximos passos**
  - [x] Ver `07-conclusoes-e-limitacoes.md`.

## Caso prático (o que os resultados dizem)

- **O PIB per capita sozinho** prevê o CO₂ per capita com erro típico de cerca de ×1,65 na validação. Acrescentar a energia per capita baixa para ×1,23 no teste, mas isso é quase mecânico (queimar combustível emite CO₂).
- **Quem reduz em 10 anos:** o efeito dominante é o nível inicial: países que emitiam muito por pessoa tenderam a reduzir. Os que já vinham aumentando nos 5 anos anteriores tenderam a continuar. São **associações**, não causas.
- **Brasil** (previsto por um modelo ajustado sem ele): emite 2,29 t/pessoa em 2022 e o modelo previu 3,96. Ficou abaixo do previsto nos 23 anos do painel (em média 0,62 vez o esperado). **Hipótese não testada:** matriz elétrica majoritariamente renovável. Entre 2012 e 2022 reduziu 9,6% (de 2,53 para 2,29 t), contra 3,7% do mundo. O modelo acertou 7 das 13 janelas do Brasil.
- **Resíduos:** não há curva evidente; os pontos aparecem em faixas porque o erro de cada país se repete ao longo dos anos.
- **Incerteza:** os 41 países de teste são um único sorteio. A incerteza da acurácia da classificação é de cerca de ±13 pontos percentuais se contarmos países, e de cerca de ±3,5 se contarmos janelas como independentes (o que elas não são).

## Entregável

Relatório de avaliação: seções 5A, 5B e 4C do notebook; figuras em `figuras/`.

## Controle

| Campo | Valor |
|---|---|
| Status | Concluído |
| Responsável | Cléder Rafael Narciso de Araújo |
| Prazo | 25/11/2026 |
| Observações | Os valores do teste foram calculados uma vez; as comparações extras por conjunto de atributos são só descritivas. |

> Status possíveis: Não iniciado, Em andamento, Concluído, Bloqueado.


**Próxima fase:** `06-implantacao.md`
