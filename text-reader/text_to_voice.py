import pyttsx3
import pdfplumber
import keyboard
import time

reading = True
page = 0

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def readPage():
    # Read the file
    with pdfplumber.open('frankenstein.pdf') as temp:
        text = temp.pages[page]
        print(text.extract_text())
    # Control the rate. Higher rate = more speed
    audio = text.extract_text().replace ("\n", "")
    engine.say(audio)
    engine.runAndWait()

while(reading):
    if keyboard.is_pressed('a'):  # if key 'q' is pressed 
        print('You Pressed A Key!')
        time.sleep (0.5)
        if page>0:        
            page=page-1
            text = "Anterior"
        else:
            text = "No hay página anterior"
        engine.say(text)
        readPage()   
    elif keyboard.is_pressed('d'):
        print('You Pressed D Key!')
        time.sleep (0.5)
        text = "Siguiente"
        engine.say(text)
        page=page+1
        readPage()
    elif keyboard.is_pressed('s'):
        print('You Pressed S Key!')
        time.sleep (0.5)
        text = "Leer página actual"
        engine.say(text)
        readPage()    
    elif keyboard.is_pressed('w'):
        print('You Pressed W Key!')
        time.sleep (0.5)
        text = "El programa se cerrará"
        engine.say(text)
        reading=False

    engine.runAndWait()    
    