import cohere

COHERE_API_KEY = "0zIapnzQSu4BXmPPkFbL4A0E4HZG9wM6IotodQOn"
client = cohere.Client(COHERE_API_KEY)

def analisar_contexto(dados, ativo):
    prompt = f"""
Você é um assistente financeiro. Diga se o seguinte contexto é POSITIVO ou NEGATIVO para o ativo {ativo}, pensando em comprar ou vender no curto prazo (1 minuto).
Contexto: {dados}
Resposta (apenas uma palavra: POSITIVO ou NEGATIVO):
"""

    response = client.generate(
        model="command",
        prompt=prompt.strip(),
        max_tokens=5,
        temperature=0.3,
        stop_sequences=["\n"]
    )

    texto_resposta = response.generations[0].text.strip().upper()
    if "POSITIVO" in texto_resposta:
        return "positivo"
    elif "NEGATIVO" in texto_resposta:
        return "negativo"
    else:
        return "neutro"
