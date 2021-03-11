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

while(True):
    text_to_speech(speech_to_text())