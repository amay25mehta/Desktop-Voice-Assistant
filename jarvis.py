import pyttsx3  
import speech_recognition as sr       #  text to speech module
import datetime
import pyaudio
import wikipedia                         
import webbrowser                    #to open browser for chrome
import os
import smtplib                      #to send emails
import sys



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)





def speak(audio):        #speak function
    engine.say(audio)
    engine.runAndWait()


def wishMe():                                    #wish you when program starts
    hour=int(datetime.datetime.now().hour)      #getting the hour of the day
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")    
    else:
        speak("Good Evening!")   

    speak("Im Jarvis Sir,Please tell me how may I help you")     


def takeCommand():                             #take microphone input from the user and returns string output
        r = sr.Recognizer()                      #Creates a new ``Recognizer`` instance, which represents a collection of speech recognition 

        with sr.Microphone() as source:
             print("Listening....") 
             r.adjust_for_ambient_noise(source=source)
             audio = r.listen(source)
                

            
        

        try:    #using try incase of some error
            print("Recognizing......")
            query = r.recognize_google(audio)   #using google speech recongnition
            print(f"User input: {query}" )
                #return voice input into string output

        except: 
            print("Enable to recognize your voice")
            return "None"
        return query
        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amaythegreatmehta@gmail.com', 'stisvtiktexlxpbm')
    server.sendmail('amaythegreatmehta@gmail.com', to, content)
    server.close()        



if __name__ == '__main__':
    wishMe()

    while True:
        query=takeCommand().lower()


        #logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")            
            results = wikipedia.summary(query, sentences=2)   #to search wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")   

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir="E:\\Music\\English"     
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")    

        elif 'open code' in query:
            codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "amaythegreatmehta2@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")  

        elif  'quit' in query:
            sys.exit()


        else:
            print("Could not recognize the command,Please speak again")    
                     




  

