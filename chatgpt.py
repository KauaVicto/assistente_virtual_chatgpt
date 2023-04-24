# Instrucoes
# instalar openai com "pip install openai"
# criar uma chave "API key" no site da OpenAI
# substituir a sua chave no codigo

import openai

# Initialize the API key
openai.api_key = "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"

def gerar_resposta(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", ##
        #model="gpt-3.5-turbo-0301", ## ateh 1 junho 2023
        messages=messages,
        max_tokens=1024,
        temperature=1
    )
    return [response.choices[0].message.content, response.usage]

