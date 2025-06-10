
import cohere
COHERE_API_KEY = "0zIapnzQSu4BXmPPkFbL4A0E4HZG9wM6IotodQOn"
client = cohere.Client(COHERE_API_KEY)

def analisar_contexto(dados, ativo):
    texto = f"Analise técnica para {ativo} com preços recentes: {dados[-5:]}"
    response = client.classify(
        model='embed-english-v3.0',
        inputs=[texto],
        examples=[["compra forte", "positivo"], ["venda", "negativo"]]
    )
    label = response.classifications[0].prediction
    return 60 if label == "positivo" else 30
