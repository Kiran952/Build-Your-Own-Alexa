# based on version packages need to be downloaded suppose here we are using python 2 if u use python 3 again u have to download the packages

import pyaudio #these pyaudio package work on lower versions of python, before installing this we have to install home brewi
import speech_recognition as sr
import speech_recognition as sr
import  pyttsx3

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:   #source of our audio
        print("listening....  ")   # for to know that alexa is listening our words
        voice = listener.listen((source))   # calling the speech recognition to listen the source
        command = listener.recognize_google(voice)   # passing the voice by using the google api
        command=command.lower()  # using the cammand for alexa words in our speech
        if 'alexa' in command:  #if the user spells alexa then respond other wise no need
             print (command)

except:
    pass  # speech code completes


