from reconhecimento import reconhecimento
from chatgpt import gerar_resposta
from fala import falar




def ChatGpt():
    mensagens = []
    falar('o que deseja?')
    while True:
        # Ask a question
        question = reconhecimento()
        print("Nóis:", question)

        if (question == 'sair'):
            break

        mensagens.append({"role": "user", "content": str(question)})

        answer = gerar_resposta(mensagens)
        print("ChatGPT:", answer[0])
        falar(answer[0])
        mensagens.append({"role": "assistant", "content": answer[0]})

        debugar = False
        if debugar:
            print("Mensagens", mensagens, type(mensagens))
    falar('até mais')


while True:
    frase = reconhecimento()
    print(frase)
    if frase == 'conversar':
        ChatGpt()
    elif frase == 'sair':
        break