import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening, please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return ""
        
def alarm(query):
    timehere = open("alarm.txt","a")
    timehere.write(query)
    timehere.close
    os.startfile("alarm.py")

def speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__': 
    print("Say 'hey mana' to start.")
    while True:
        command = sptext().lower()
        if "hey mana" in command:
            print("How can I help you?")
            data1 = sptext().lower()
            if "your name" in data1:
                name = "My name is Mana."
                speech(name)

            elif "old are you" in data1:
                age = "I am 2 years old."
                speech(age)

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I:%M %p")
                speech(time)

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "google" in data1:
                webbrowser.open("https://www.google.co.uk/")

            elif "joke" in data1:
                joke = pyjokes.get_joke(language="en", category="neutral")
                speech(joke)

            elif "open" in data1:
                try:
                    from dictapp import openapp
                    query = data1.replace("open", "").strip()
                    openapp(query)
                except ImportError:
                    speech("Application module not found.")

            elif "close" in data1:
                try:
                    from dictapp import close
                    query = data1.replace("close", "").strip()
                    close(query)
                except ImportError:
                    speech("Close module not found.")

            elif "exit" in data1:
                speech("Thank you. Goodbye!")
                break

            else:
                speech("I didn't understand that command.")
