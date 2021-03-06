
# import modules
from datetime import datetime          # datetime module supplies classes for manipulating dates and times
import subprocess                      # subprocess module allows you to spawn new processes
import speech_recognition as sr        # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Parle !")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
Query = r.recognize_google(audio)
print(Query)

while True:  
 compteur += 1  
 if compteur == 1000000:  
  break  
# Run Application with Voice Command Function
def get_app(Q):
    if Q == "time":
        print(datetime.now())
    elif Q == "notepad":
        subprocess.call(['Notepad.exe'])
    elif Q == "calculator":
        subprocess.call(['calc.exe'])
    elif Q == "stikynot":
        subprocess.call(['StikyNot.exe'])
    elif Q == "shell":
        subprocess.call(['powershell.exe'])
    elif Q == "paint":
        subprocess.call(['mspaint.exe'])
    elif Q == "cmd":
        subprocess.call(['cmd.exe'])
    elif Q == "browser":
        subprocess.call(['C:\Program Files\Internet Explorer\iexplore.exe'])
    else:
        print("Sorry ! Try Again")
    return


# Call get_app(Query) Func.
get_app(Query)