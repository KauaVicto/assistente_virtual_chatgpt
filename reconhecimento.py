import speech_recognition as sr


def reconhecimento():
    rec = sr.Recognizer()

    # print(sr.Microphone().list_microphone_names())
    with sr.Microphone(1) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Diga o que deseja: ")
        audio = rec.listen(mic)
        try:
            texto = rec.recognize_google(audio, language='pt-BR')
            return texto
        except sr.UnknownValueError:
            print('Não Entendi')