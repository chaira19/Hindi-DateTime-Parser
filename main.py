import stack
from stack import *

import parser
from parser import *

## get the input
## input or raw_input
 
import speech_recognition as sr
 
# Record Audio
r = sr.Recognizer()
m = sr.Microphone()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    string=r.recognize_google(audio)
    #time.sleep(1)
    
    #stop_listening = r.listen_in_background(m, callback)
   
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
print(string)

## convert inpurt to lower case
string = string.lower()

## split the input into words(list)
words = string.split(" ")

## get the dictinary of stacks
Final = stack_algo(words)

# empty function makes empty

## Get parsed dictionary from Final Dictionary
Answer = get_parsed(Final={})

import pyttsx3
import time
eng=pyttsx3.init()
eng.say(Answer)
eng.runAndWait()

emails = get_emails_parsed(words)

if len(emails)!=0:

        print (emails)



