import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime  # pip install DateTime
import os  # pip install os-sys
import subprocess  # pip install subprocess.run
import webbrowser as wb  # pip install pycopy-webbrowser
import pyautogui  # pip install PyAutoGUI
import wikipedia  # pip install wikipedia
import pyjokes  # pip install pyjokes
from time import sleep
import random
from random import randint

engine = pyttsx3.init()  # initialise pyttsx3 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0-2 range for different voices
voicespeed = 150  # setting speed
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print(e)
        return "---"
    return query


def time():
    time = datetime.datetime.now().strftime("%I %M %p")  # In 12 hour format
    speak(time)
    print(time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    print(day, month, year)
    speak(day)
    speak(month)
    speak(year)


def greetings():
    speak("Welcome back sir")
    speak('Extracting all the necessary files')
    speak('Collecting data')
    speak('Executing Raphael')
    speak('Done')
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("good night")
    speak("how can i help you")


# Open chrome/website
def open_chrome():
    url = "https://www.google.co.in/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    speak("Opening chrome")
    wb.get(chrome_path).open(url)


# Open microsoft edge
def open_edge():
    url = ""
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    speak("Opening edge")
    wb.get(edge_path).open(url)

    
# Open animixplay
def open_animixplay():
    url = "https://animixplay.to/?from=com"
    speak("Opening animixplay...")
    wb.open(url)    
    
if __name__ == "__main__":
    
    greetings()
    
    try:

        while True:
            
            query = takeCommand().lower()
            print(query)
            
            # Interactions
            if "hello" in query:
                speak('Hello Master Keshav. How may I help you?')
            
            elif "time" in query:
                time()

            elif "date" in query:
                date()

            elif "completed" in query:
                speak("Congratulations Sir ! Please have some rest or come up with a new schedule")

            # All features brief
            elif "what can you do" in query:
                speak("Try saying open chrome or play music")
                speak('Do you want me to mention all the features?  Please complete the if else statement Sir')
                
            # open chrome
            elif "open chrome" in query:
                open_chrome()
                takeCommand()
                    
            elif "open edge" in query:
                open_edge()
                takeCommand()
                    
            # Chrome search
            elif "search" in query:
                speak("say the name of any website")
                chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
                search = takeCommand().lower()
                speak("Opening....")
                speak(search)
                wb.get(chromepath).open_new_tab(search + ".com")
                takeCommand()
                
            # Open youtube    
            elif "open youtube" in query:
                url = "https://www.youtube.com/"
                speak('opening youtube')
                wb.open(url)
                takeCommand()

            # Open Specific Whatsapp group
            elif "open english appreciation group" in query:
                url = "https://chat.whatsapp.com/DS72zocnWzK4iyWNUTc7YX"
                speak('opening whatsapp group')
                wb.open(url)

             # Wikipedia search
            elif "wikipedia" in query:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(result)
                print(result)
                
            # Play Music
            elif "play music" in query:
                url = "C:/Users/Keshav Mandal/Music/All songs"
                music = os.listdir(url)
                random.shuffle(music)
                speak("Playing music")
                os.startfile(os.path.join(url, music[45]))
                
            elif "next song" in query:
                url = "C:/Users/Keshav Mandal/Music/All songs"
                music = os.listdir(url)
                random.shuffle(music)
                speak("Okay")
                os.startfile(os.path.join(url, music[45]))
        
            # elif "play music" in query:
            #    url = "https://wynk.in/music/search"
            #    wb.open(url)
            #    speak('say the name of the song')
            #    pyautogui.hotkey('winleft','h')
            #    sleep(3)
            #    pyautogui.hotkey('enter')
            #    pyautogui.hotkey('space')
            
            # Open animixplay
            elif "open anime stream" in query:
                open_animixplay()
            
            # Open my blog
            elif "my blog profile" in query:
                url = "https://www.blogger.com/profile/11275715488977087335"
                speak('Okay')
                wb.open(url)
                
            elif "poetry" in query:
                url = "https://www.blogger.com/blog/posts/5171621245488448794"
                speak('Okay')
                wb.open(url)
                
            elif "program" in query:
                url = "https://www.blogger.com/blog/posts/8192399780571400307"
                speak('Okay')
                wb.open(url)
                
            # Play specific video from specific time
            elif "play motivation" in query:
                url = "https://youtu.be/dms6eeENe1I"
                speak('playing selected youtube short')
                wb.open(url)
                sleep(2)
                pyautogui.press('f')
              
            elif "play video" in query:
                url = "https://youtu.be/67TobaDateE?t=1091"
                speak('playing selected video from youtube')
                wb.open(url)
                sleep(2)
                pyautogui.press('f')
                
            elif "play youtube short" in query:
                url = "https://www.youtube.com/shorts/faylYt1k1Vo"
                speak('playing selected youtube short')
                wb.open(url)
                
            elif "play random youtube short" in query:
                url = "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiuuOO3-Zf8AhUkk2YCHZ07CP4YABAAGgJzbQ&ohost=www.google.com&cid=CAESbOD2ea-78BgA67zMsMlwBhmbn1XbND2t5n3bU6HH1z6l4zTZsbkS0gQhNNzjj1aaH3bI8Cmz77lK_ZXVuqMqsLXsy1TvylmeKmmSwFE0qIMVfzWZb0hjQhmhUfbqbl7F7oiL887jQsj-QCNP3A&sig=AOD64_165Hu-vBsc0eRB-nhCF4gvp7pmng&q&adurl&ved=2ahUKEwiu1t23-Zf8AhVi2HMBHe1cBCYQ0Qx6BAgJEAE"
                speak('playing youtube shorts')
                wb.open(url)
                
            elif "play devotional song" in query:
                url = "https://youtu.be/O-0AxROPI64"
                speak('playing selected music video')
                wb.open(url)
                sleep(2)
                pyautogui.press('f')
                
            elif "play anime music video" in query:
                url = "https://youtu.be/V_MX0HiIgRQ"
                speak('playing selected music video')
                wb.open(url)
                sleep(2)
                pyautogui.press('f')
              
            # Open specific pdf file
            elif "open pdf" in query:
                url = "file:///C:/Users/Keshav%20Mandal/OneDrive/Documents/CS-2%20Journal%20%20(1).pdf"
                speak("Opening pdf...")
                wb.open(url)
               
            # PLay Game
            elif "play game" in query:
                url = "C:/Program Files/Genshin Impact/launcher.exe"
                speak("Okay. Let's play Genshin Impact!")
                wb.open(url)
                sleep(2)
                pyautogui.hotkey('left')
                pyautogui.hotkey('enter')
               
            # Open Screenshot photos Folder   
            elif "open screenshot folder" in query:
                url = "C:/Users/Keshav Mandal/OneDrive/Pictures/Screenshots"
                speak("Opening folder")
                wb.open(url)
            
            # Microphone setup settings
            elif "microphone" in query:
                speak("Okay!")
                pyautogui.hotkey('winleft', 'u')
                sleep(3)
                pyautogui.hotkey('ctrl', 'e')
                str = 'sound'
                for i in str:
                    pyautogui.press(i)
                sleep(2)
                pyautogui.press('down')
                sleep(2)
                pyautogui.press('enter')
                # for j in range(1, 4, 1):
                #    pyautogui.press('down')
                # pyautogui.press('enter')
                sleep(2)
                for k in range(1, 13, 1):
                    pyautogui.press('tab')
                speak("Now you can setup the microphone you want.")    
            
            # Launch software
            elif "open notepad" in query:
                speak("opening notepad")
                location = "C:/WINDOWS/system32/notepad.exe"
                notepad = subprocess.Popen(location)

            elif "close notepad" in query:
                speak("closing notepad") 
                notepad.terminate()
                
            elif "open whatsapp" in query:
                speak("opening whatsapp")
                location = "C:/Users/Keshav Mandal/AppData/Local/WhatsApp/WhatsApp.exe"
                whatsapp = subprocess.Popen(location)
                
            elif "open command prompt" in query:
                speak("opening command prompt")
                pyautogui.hotkey('ctrl', 'shift', 'c')
                
            # Random jokes
            elif "jokes" in query:
                speak(pyjokes.get_jokes())

            # Logout/Shutdown/Restart
            elif "logout" in query:
                speak('logging out in 5 seconds')
                sleep(5)
                os.system("shutdown - l")

            elif "shutdown" in query:
                speak('shutting down in 5 seconds')
                sleep(5)
                os.system("shutdown /s /t 1")
                # pyautogui.hotkey('winleft','x')
                # pyautogui.hotkey('u')     
                # pyautogui.hotkey('u')
         
            elif "restart" in query:
                speak('restarting in 5 seconds')
                sleep(5)
                os.system("shutdown /r /t 1")
                # pyautogui.hotkey('winleft','x')
                # pyautogui.hotkey('u')
                # pyautogui.hotkey('r')
                url = "C:/Users/Keshav Mandal/AppData/Local/Programs/Microsoft VS Code/Code.exe"
                wb.open(url)
                
            #-------------------PYAUTOGUI FEATURES--------------------->
            elif "hidden menu" in query:
                # Win + X :open the hidden menu
                speak('Opening hidden menu')
                pyautogui.hotkey('winleft', 'x')
                
            elif "task manager" in query:
                # Ctrl + shift + Esc : open task manager
                speak('Opening task manager')
                pyautogui.hotkey('ctrl', 'shift', 'esc')
                
            elif "task view" in query:
                # Win + Tab : open the task view
                speak('Opening task view')
                pyautogui.hotkey('winleft', 'tab')
                
            elif "take screenshot" in query:
                # Win + prtscr : take screenshot
                pyautogui.hotkey('winleft', 'prtscr')
                speak("Done")        
                
            elif "adjust screenshot" in query:
                # Win + shift + s: take snip
                pyautogui.hotkey('winleft', 'shift', 's')
                speak("Done") 
                
            elif "go to home screen" in query:
                # win + d : go to home screen
                pyautogui.hotkey('winleft', 'd')
                speak("Done") 

            elif "open settings" in query:
                # win + i : open settings
                speak("Opening settings...")
                pyautogui.hotkey('winleft', 'i')
                
            elif "open file explorer" in query:
                # win + e : open file explorer
                speak("Opening file explorer...")
                pyautogui.hotkey('winleft', 'e')
                
            elif "close the app" in query:
                # Alt + F4 : close the app
                pyautogui.hotkey('alt', 'f4')
                speak("Done")     

            elif "create new desktop" in query:
                # win + ctrl + d : create new desktop
                pyautogui.hotkey('winleft', 'ctrl', 'd')
                speak("Done") 
                
            elif "close tab" in query:
                # ctrl + w : close recent chrome tab
                pyautogui.hotkey('ctrl', 'w')
                speak("Done")
            
            elif "enter" in query:
                # win + d : enter
                pyautogui.hotkey('enter')
                
            elif "left" in query:
                # > : move left
                pyautogui.hotkey('left')
                
            elif "right" in query:
                # < : move right
                pyautogui.hotkey('right')
            
            elif "top" in query:
                # ^ : move up
                pyautogui.hotkey('up')
                
            elif "down" in query:
                # v : move down
                pyautogui.hotkey('down')        
                
            elif "exit" in query:
                # alt + x : exit terminal
                pyautogui.hotkey('alt', 'x')
                speak("done")
                
            elif "delete" in query:
                # delete : delete
                pyautogui.hotkey('delete')
                
            elif "voice typing" in query:
                # winleft + h : voice typing
                pyautogui.hotkey('winleft', 'h')
                
            elif "create new tab" in query:
                # ctrl + t : create new tab
                pyautogui.hotkey('ctrl', 't')
                
            elif "recover recent tab" in query:
                # ctrl + shift + t : recover recent tab
                pyautogui.hotkey('ctrl', 'shift', 't')
                
            elif "close all tabs" in query:
                # ctrl + shift + w : close all tabs
                pyautogui.hotkey('ctrl', 'shift', 'w')
                
            # Empty
            elif "nothing" in query:
                break

    except Exception:
        speak("Something went wrong !")
        speak("Please try again !")
        takeCommand()
        
    speak("Okay! Have a nice day Sir")
