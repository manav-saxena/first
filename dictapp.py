import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

def speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "wordpad", "vscode": "code"}

def openapp(query):
    speech("launching sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace(",mana", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"http://www.{query}")
    else:
        keys = list(dictapp.keys())  # Use keys() method
        for apps in keys:
            if apps in query:
                os.system(f"start {dictapp[apps]}")

def close(query):
    speech("closing sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speech("all tab closed")
    else:
        keys = list(dictapp.keys())  # Use keys() method
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
