
# gui developmen for chatbot

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyttsx3

root = tk.Tk()
root.title('Welcome to chatBot')
root.geometry('1100x691+300+200')
root.configure(bg="black")
root.resizable(False, False)

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say: ", MyText)
                SpeakText(MyText)
        except sr.RequestError as e:
            print("Could not request result; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occured")

def gotonext():
    screen = Toplevel(root)
    screen.title("ChatBot")
    screen.geometry('1000x550+300+200')
    screen.config(bg='white')
    root.withdraw()
        
    tts = pyttsx3.init()
    def printInput():
        text = inputtxt2.get(1.0, "end-1c")
        voice = tts.getProperty('voice')

        def setvoice():
            gender = 'male'
            
            if(gender == 'male'):
                tts.setProperty('voice', voice[0])
                tts.say(text)
                tts.runAndWait()
            else:
                tts.setProperty('voice', voice[1])
                tts.say(text)
                tts.runAndWait()
        if(text):
            speed = 'fast'
            if(speed == 'fast'):
                tts.setProperty('rate', 175)
                setvoice()
            else:
                tts.setProperty('rate', 175)
                setvoice()

    logo_image = PhotoImage(file="iconbot.png")
    screen.iconphoto(False, logo_image)
    # TextBox Creation

    lbl1 = Label(screen, text='Ask anything from me..!', font=('calibri', 12), bg='white').place(x = 20, y = 80)

    bg1 = PhotoImage(file='iconbot.png')
    lable3 = Label(screen, height=180, width=180, bg='gray', image=bg1).place(x = 700, y = 80)

    inputtxt2 = Text(screen, font=('calibri', 12), height = 6, width = 75, bg="#eee", border=0)
    inputtxt2.place(x = 20, y = 120)

    printButton2 = Button(screen, text = "Ask me", font=('calibri', 12), command = SpeakText, width=15, height=2,border=0, bg='#1F456E', fg='white', cursor= 'hand2')
    printButton2.place(x = 20, y = 250)

    printButton1 = Button(screen,text = "Send", font=('calibri', 12), command = printInput, width=15, height=2,border=0, bg='#1F456E', fg='white', cursor='hand2')
    printButton1.place(x = 150, y = 250)

    bg2 = PhotoImage(file='answer01.png')
    lable3 = Label(screen, height=424, width=373, bg='gray', image=bg2).place(x = 20, y = 320)

    lbl1 = Label(screen, text='Collect your answer from me..!', font=('calibri', 12), bg='white').place(x = 375, y = 360)

    inputtxt1 = Text(screen, font=('calibri', 12), height = 6, width = 75, bg="#eee", border=0)
    inputtxt1.place(x = 375, y = 390)

    printButton1 = Button(screen,text = "Hear me", font=('calibri', 12), command = printInput, width=15, height=2,border=0, bg='#1F456E', fg='white', cursor='hand2')
    printButton1.place(x = 850, y = 330)

    screen.mainloop()

logo_image = PhotoImage(file="iconbot.png")
root.iconphoto(False, logo_image)

img = PhotoImage(file='aiselection.png')
Label(root, image=img, bg='white').place(x=0, y=0)

btn = Button(root, text="Get started with ChatBot", font=("Arial", 20),width=30, height=2, bg='#eee', cursor = "hand2", command=gotonext).place(x = 85, y= 520)

imga = PhotoImage(file='arror.png')
Label(btn, image=imga).place(x = 490, y = 538)

root.mainloop()
