# Conclusões, limitações e próximos passos

## O que o estudo mostra

1. **Desenvolvimento e emissão andam juntos.** O log do PIB per capita tem correlação de 0,925 com o log do CO₂ per capita nas 3.772 linhas. Só com o PIB, o erro típico da previsão é de cerca de ×1,65; com energia per capita, de ×1,23 em países de teste.
2. **Reduzir emissões em 10 anos é parcialmente previsível.** Em 533 janelas de países que o modelo não viu, o classificador acerta 78% (referência: 67%). O fator mais forte é o nível inicial de emissão.
3. **Os grupos são moderadamente definidos.** Pela silhueta, três grupos (56, 99 e 8 países), mas o do meio é muito heterogêneo.
4. **O Brasil emite menos que o previsto** para seu PIB e energia em todos os anos de 2000 a 2022, o que sugere (hipótese) o peso das fontes renováveis na eletricidade.

## Limitações

- **Só CO₂ de combustíveis e indústria.** Fica de fora a mudança no uso da terra, que no Brasil é relevante.
- **Só 164 países com PIB**, e um único sorteio de 41 países de teste. Os resultados mudariam com outro sorteio.
- **Observações repetidas.** As 23 linhas de cada país são parecidas, e as 13 janelas de cada país se sobrepõem. Por isso o tamanho efetivo da amostra é mais próximo de 164 países que de 3.772 ou 2.132 linhas.
- **Associação não é causa.** Os coeficientes descrevem o que acompanha o quê.
- **A janela de 10 anos inclui 2020 (pandemia)** e crescimento populacional, que reduz o valor per capita sem reduzir o total. Isso não foi separado.
- **Carvão e gás ausentes foram imputados pela mediana**, mas podem significar "zero".
- **O CO₂ é medido no país onde ocorre a emissão**, não onde o bem é consumido (comércio internacional não entra).

## Próximos passos

- Incluir a participação de energias renováveis na eletricidade para testar a hipótese sobre o Brasil.
- Repetir o sorteio dos países de teste várias vezes e informar a variação dos resultados.
- Comparar o CO₂ por consumo (`consumption_co2_per_capita`) com o CO₂ por produção, que cobre só 54% dos países.

## Uso de ferramentas de IA

Usei o Claude (Anthropic) como assistente para montar a estrutura do projeto, escrever o código e redigir os textos. Os números foram calculados pelo código (`scripts/analise.py`) e conferidos pelos testes. Assumo a responsabilidade pelo conteúdo e o revisei antes de entregar.
