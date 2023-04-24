import gtts
from playsound import playsound
import os

    

def falar(texto):
    fala = gtts.gTTS(texto, lang='pt-br')
    fala.save('fala.mp3')
    playsound('fala.mp3')
    
    if os.path.exists('fala.mp3'):
        os.remove('fala.mp3')