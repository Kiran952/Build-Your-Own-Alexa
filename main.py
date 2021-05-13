# based on version packages need to be downloaded suppose here we are using python 2 if u use python 3 again u have to download the packages

import pyaudio #these pyaudio package work on lower versions of python, before installing this we have to install home brewi
import speech_recognition as sr # for speech recognition
import pyttsx3 # for printy the text
import pywhatkit #package for to automate the data
import datetime #built in package
import wikipedia # wikipedia for get the data from wikipedia
import pyjokes #for to get the jokes



listener = sr.Recognizer()
engine = pyttsx3.init()  # here we alexa will spell it out init= intilize
#for to declare alexa female voice
voices = engine.getProperty('voices')  #Voices = we declared  a variable
engine.setProperty("voice",voices[1].id)  #we will get the all vocies with is second    index position of 1


def talk (text):
    engine.say(text)  # for to say (speak)
    engine.runAndWait()   # it is prebuild in python for to run the code and wait

def take_command():  # defining the function
   try:
       with sr.Microphone() as source: #source of our audio
           print("listening....  ")   # for to know that alexa is listening our words
           voice = listener.listen((source))   # calling the speech recognition to listen the source
           command = listener.recognize_google(voice)   # passing the voice by using the google api
           command=command.lower()  # using the cammand for alexa words in our speech
           if 'alexa' in command: #if the user spells alexa then respond other wise no need
               command=command.replace('alexa','')  # here we are giving this incase if user spels ex:alexa open alexa video in you tube in this case there is confusion in for alexa so we given like this so that alexa word will revoke form the string.
               print (command)  # for to talk the command

   except:
        pass  # speech code completes
   return command


def run_alexa():
    command = take_command() # take command from the user
    print(command)
    if 'play' in command:
        song = command.replace('play','')#here ex:alexa play beliver song it will play word alexa so we mention like this
        talk('playing '+ song)  # it will print playing text  + song
        pywhatkit.playonyt(song)   # as per pywhatkit package it will get fetch the data from youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  #for to get the present  time= %p = am or pm
        print(time)
        talk('Current time is ' + time)
    elif 'who is the ' in command:
        person = command.replace("who is the ",'')
        info = wikipedia.summary(person,1)
        print(info)
        talk('who is the '+info)
    elif 'date' in command:
        talk('sorry i have a headache')
    elif 'are you single 'in command:
        talk(' i am in relationship with siri ')
    elif 'joke 'in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk('please say the command again.')
while True:
    run_alexa()




