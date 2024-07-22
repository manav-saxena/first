import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening pls speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing")
            data = recognizer.recognize_google(audio)
            return data

        except sr.UnknownValueError:
            print("not undertanding")

def speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

 

if __name__ == '__main__':  
   # if sptext().lower() == "hey mana":
        data1=sptext().lower()
        if "your name" in data1:
            name = "my name is mana"
            speech(name)
        elif "old are you" in data1:
             age  = " i am 2 year old"
             speech(age)

        elif "time" in data1:
             time = datetime.datetime.now().strftime("%I:%M %p")
             speech(time)

        elif "youtube" in data1:
             webbrowser.open("https://www.youtube.com/")

        elif "google" in data1:
             webbrowser.open("https://www.google.co.uk/") 


             
        elif "joke" in data1:
             jokes_1 = pyjokes.get_joke(language="en", category="neutral")
             speech(jokes_1)


        elif "exit" in data1:
            speech("thank you")