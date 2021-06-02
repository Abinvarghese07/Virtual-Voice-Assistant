import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb
import pywhatkit
import pyjokes
import pyautogui
import time
import wikipedia as wiki
import selenium
from selenium import webdriver
web_path = ('C:\Program Files\Google\Chrome\Application',None)

address = pyttsx3.init()
listener = sr.Recognizer()

address.say('hello i am jarvis')
address.say('how can i help you')
address.runAndWait()



def jarvis_preprocessing():
    try:
        with sr.Microphone() as source:
            print('listening....')
            listener.pause_threshold = 3
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            address.say(command)
            address.runAndWait()


        if 'how are you' in command:
            address.say('i am doing good thank you')
            address.say('i hope your doing good too')
            address.runAndWait()

        elif 'single' in command:
            address.say('well i am in a relationship with wifi he he he he')
            address.runAndWait()


        elif 'time' in command:

            time_py = datetime.datetime.now().strftime('%I : %M : %p')
            print(time_py)
            address.say('the current time is ' + time_py)
            address.runAndWait()

        elif 'date' in command:
            date_py = datetime.datetime.now().strftime('%d : %m : %y')
            print(date_py)
            address.say('the present date is' + date_py)
            address.runAndWait()


        elif 'whatsapp' in command:
            address.say('opening whatsapp')
            whatsapp_web = wb.open('https://web.whatsapp.com/')
            address.say(whatsapp_web)
            address.runAndWait()


        elif 'gmail' in command:
            address.say('opening gmail')
            mail = wb.open('https://mail.google.com/mail/u/0/#inbox')
            address.say(mail)
            address.runAndWait()


        elif 'youtube' in command:
            address.say('opening youtube')
            youtube_path = wb.open('https://www.youtube.com/')
            address.say(youtube_path)
            address.runAndWait()


        elif 'instagram' in command:
            address.say('opening instagram')
            ig_path = wb.open('https://www.instagram.com/')
            address.say(ig_path)
            address.runAndWait()


        elif 'mail' in command:
            address.say('opening mail')
            mail_path = wb.open('https://mail.google.com/mail/u/0/#inbox')
            address.say(mail_path)
            address.runAndWait()


        elif 'meet' in command:
            address.say('opening meet')
            meet_path = wb.open('https://meet.google.com/')
            address.say(meet_path)
            address.runAndWait()



        elif 'netflix' in command:
            address.say('opening netflix')
            netflix_path = wb.open('https://www.netflix.com/browse')
            address.say(netflix_path)
            address.runAndWait()



        elif 'linkedin' in command:
            address.say('opening linkedin')
            li_path = wb.open('https://www.linkedin.com/feed/')
            address.say(li_path)
            address.runAndWait()



        elif 'search' in command:
            address.say('searching')
            address.runAndWait()
            print(command)
            wb.open(command)


        elif 'play' in command:
            address.say('jarvis is now playing')
            address.runAndWait()
            print(command)
            pywhatkit.playonyt(command)


        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            address.say(joke)
            address.runAndWait()



        elif 'wikipedia' in command:
            wiki_info = wiki.summary(command,3)
            print(wiki_info)
            address.say(wiki_info)
            address.runAndWait()


        elif 'who' in command:
            address.say('searching')
            address.runAndWait()
            wb.open(command)


        elif 'facebook' in command:
            address.say('opening facebook')
            address.runAndWait()
            wb.open('https://www.facebook.com/')
            time.sleep(4)
            for i in range(1):
                pyautogui.typewrite('akkuklm@gmail.com')
                break

                pyautogui.press('enter')
                pyautogui.typewrite('imakku223')
                pyautogui.press('enter')











        else:
            pyttsx3.speak('sorry i did not hear you')
























    except:
        pass


while True:
        jarvis_preprocessing()










