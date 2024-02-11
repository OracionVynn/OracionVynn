"""This program will be a personal virtual assistant program that will be a multipurpose tool that can be used from anything that I am abled to program it to do...Written and developed by Adrian Simon(Oracion Vynn)"""

"""Libraries to run"""
import pyttsx3
import speech_recognition as sr
import time
from openpyxl import * #load workbook in excel
import random # to allow replies to questions
import datetime

"""Variables """
r = sr.Recognizer()
keywords = [("reversii", 1), ("hey reversii", 1), ] # Setting up our "wake" words
source = sr.Microphone() # setting up our microphone


"""Functions"""
def Speak(text):
    rate = 100 # Sets the default speech rate
    engine = pyttsx3.init() # Initialize our speech engine
    voices = engine.getProperty('voices') # sets the speech properties
    engine.setProperty('voices', voices[0].id) # Gender and type of voice
    engine.setProperty('rate', rate+50) # Adjust the speech rate
    engine.say(text) # tells python to speak variable "text"
    engine.runAndWait() # waits for speech to finish before continuing the program
    
def callback(recognizer, audio):
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords) #uses sphinx as the speech recognizer
        print(speech_as_text) #prints what was said on the screen
        if "reversii" in speech_as_text or "hey reversii": #starter names
            Speak("Yes sir?") # calls "Speak" and acknowledges the user
            recognize_main() #runs the recognize_main function
    except sr.UnknownValueError: # If nothing is understood.
        print("I didn't quite catch that sir.") #Prints an error message
        
def start_recognizer(): #initial keyword call
    print("Waiting for keyword...reversii or hey reversii") #prints to screen
    r.listen_in_background(source, callback) #sets off recognition sequence
    time.sleep(1000000) #keeps loop running
    
def recognize_main(): # main reply call function
    r = sr.Recognizer() # sets r variable
    with sr.Microphone() as source: # sets microphone
        print("Say something...") # prints to screen
        audio = r.listen(source) # sets audio variable
    data = "" # assign user voice entry to "data" variable
    try:
        data = r.recognize_google(audio) #now uses google speech recognition
        data.lower() # makes all voice entries show up in lowercase
        print("You said: " + data) # shows what user said and what was recognized.
#Greetings----------------------------------------------------------------
        # if "hello" in data:
        if data in hello_list:
            hour=datetime.datetime.now().hour
            if hour>=0 and hour<=12:
                Speak("Good morning, sir")
            elif hour>=12 and hour<18:
                Speak("Good afternoon, sir")
            else:
                Speak("Good evening, sir")
            time.sleep(2)
        elif data in how_are_you:
            Speak(random.choice(reply_how_are_you))
            time.sleep(2)
        elif "What is the time" in data:
            strTime=datetime.datetime.now().strftime("%H:%M")
            Speak(f"the time is {strTime}")
            time.sleep(2)
        elif "What day is it" in data:
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}   
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                Speak("The day is " + day_of_the_week)
                time.sleep(2)
        else: # what happens if none of the if statements are true
            Speak("I'm sorry sir, I did not understand your request") # calls Speak function and says something
    except sr.UnknownValueError: # whenever you have a try statement you have an exception rule
        print("Reversii did not understand your request") 
    except sr.RequestError as e: # if you get a request error from Google speech engine
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
def excel():
    wb = load_workbook("OracionVynn/OracionVynn/R.E.V.E.R.S.I.I/input.xlsx") #Opens the excel document for data
    wu = wb.get_sheet_by_name("User") #sets the sheet in excel for user prompt
    wr = wb.get_sheet_by_name("Replies") #sets the sheet in excel for replies
    
    global hello_list
    global how_are_you
    urow1 = wu["1"] #hello
    urow2 = wu["2"] #how are you
    hello_list = [urow1[x].value for x in range(len(urow1))]
    how_are_you = [urow2[x].value for x in range(len(urow2))]
    
    global reply_hello_list
    global reply_how_are_you
    rrow1 = wr["1"] #how are you
    rrow2 = wr["2"] #how are you
    reply_hello_list = [rrow1[x].value for x in range(len(rrow1))]
    reply_how_are_you_list = [rrow2[x].value for x in range(len(rrow2))]
        
            
"""Main program"""
while 1: # This starts a loop so the speech recognition is always listening to you
    start_recognizer() # calls first function "start_recognizer"
    
    
# Notes