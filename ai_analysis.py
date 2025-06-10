import cohere

COHERE_API_KEY = "0zIapnzQSu4BXmPPkFbL4A0E4HZG9wM6IotodQOn"
client = cohere.Client(COHERE_API_KEY)

def analisar_contexto(dados, ativo):
    texto = f"Analisando o ativo {ativo}. {dados}"

    response = client.classify(
        inputs=[texto],
        examples=[
            ["mercado em alta", "positivo"],
            ["subida de preço", "positivo"],
            ["compra forte", "positivo"],
            ["mercado em baixa", "negativo"],
            ["queda de preço", "negativo"],
            ["venda forte", "negativo"]
        ]
    )

    return response.classifications[0].prediction
