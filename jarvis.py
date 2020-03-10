import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else :
        speak("Good Evening!")


speak("I am jarvis sir .please tell me how may I help you")


def takecommand() :
    # It take micro phn input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, Language='en-in')
            print(f"User Said:{query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


if __name__ == "__main__":
    wishMe()
    while True:
      query=takecommand().lower()
      if 'wikipedia' in query:
          speak("Searching Wikipedia.....")
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query,sentences=2)
          speak("According to wikipedia")
          print(results)
          speak(results)
      elif 'open youtube' in query:
          webbrowser.open("google.com")
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
      elif 'stack overflow' in query:
          webbrowser.open("stackoverflow.com")
      elif 'open youtube' in query:
          webbrowser.open("google.com")
      elif 'play music' in query:
          music_dir='C:\\Users\\DELL\\Music'
          songs=os.listdir(music_dir)
          print(songs)