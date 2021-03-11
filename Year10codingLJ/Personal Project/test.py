import speech_recognition as sr
from gtts import gTTS 
import os 
def speech_to_text():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")


        # recognize speech using google

        try:
            print(r.recognize_google(audio))
            return(r.recognize_google(audio))
        


        except Exception as e:
            print("Error :  " + str(e))
            return("Error " + str(e))

def text_to_speech(text):
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("speech.mp3") 
    os.system("afplay speech.mp3")

def recognise_meme(text):
    if text == "you were the chosen one":
        return("it was said you would destroy the sith not join them")
    if text == "hello there":
        return("general kenobi")
    if text == "this program can translate English to Chinese in almost real-time":
        return("该程序可以几乎实时地将英语翻译成中文")
    if text == "open the pod bay doors Hal":
        return("I'm sorry dave, I'm afraid I can't do that")
    if text == "tell me a story the Jedi will not tell you":
        return("'Did you ever hear the Tragedy of Darth Plagueis the wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself.'")
    else:
        return(text)
while(True):
    text_to_speech(recognise_meme(speech_to_text()))
