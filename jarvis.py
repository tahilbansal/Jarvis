import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pygame

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >0 and hour <12 :
        speak("good morning")
    elif hour >=12 and hour <18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am jarvis how can I help you sir")

def takecommand() :
    ''' It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please..")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("kantadevi7577@gmail.com","kanta@1245")
    server.sendmail("kantadevi7577@gmail.com",to,content)
    server.close()



if __name__ == '__main__':
    speak(f"Hi Tahil")
    wishme()
    while True:
        query = takecommand().lower()

        #logic for executing command and do task
        if 'wikipedia' in query:
            print("Searching wikipedia...\n")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            pygame.mixer.init()
            pygame.mixer.music.load('example.mp3')
            pygame.mixer.music.play()
            # musicdir = r'C:\Users\BHARAT\PycharmProjects\tuts'
            # songs = os.listdir(musicdir)
            # print(songs)
            # os.startfile(os.path.join(musicdir,songs[1]))
            # #  This also works
            # # musicdir = r'C:\Users\BHARAT\PycharmProjects\tuts\0.mp3'
            # # os.startfile(musicdir)

        elif "stop music" in query:
            pygame.mixer.music.stop()
            
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%H:%S")
            # print(datetime.datetime.now())
            speak(f"The time is {strtime}")

        elif 'open code' in query:
            codepath = r"C:\Users\BHARAT\AppData\Local\Programs\Microsoft VS Code\code.exe"
            os.startfile(codepath)
        elif 'email' in query:
            try:
                speak("what you want to send")
                content = takecommand()
                to = "tahilbansal1@gmail.com"
                sendEmail(to,content)
                print("sending...")
                speak("Email has been sent")
            except Exception as e :
                print("e")
                speak("problem occured")






