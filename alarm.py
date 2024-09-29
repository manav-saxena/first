import pyttsx3
from datetime import datetime
import os
timenow = datetime.now().strftime("%H:%M") 

def speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

extractedtime = open("alarm.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("alarm.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timeset = timeset.replace("mana", "")
    timeset = timeset.replace("set a alarm", "")
    alarmtime = str(timenow)
    print(alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == alarmtime:
            speech("alarm ringing sir")
            os.startfile("music.mp3")

