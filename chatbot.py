import random                           #import random library to generate random respone 
import json                             #import json library to access json file's data
from keras.models import load_model     #keras from Tensorflow for train a neural network
import numpy as np                      #To handle array data
import pickle                           #re-load pre-train machine learning models
import nltk                             #Provide text processing libraries 
from nltk.stem import WordNetLemmatizer #to get valid words as the actual word is returned
from playsound import playsound         #play output with sound
import speech_recognition as sr         #Recognize speech text
import tkinter as tk                    #To create GUIs
from tkinter import *                   
from tkinter import filedialog          
from tkinter.ttk import Combobox        #to insert a combobox
import pyttsx3                          #convert text to speech
import os                               #To interact with operating systems
from gtts import gTTS                   #To get google support to recognize text

lemmatizer = WordNetLemmatizer()                    #use to correct words

model = load_model('chatbotmodel.h5')
intents = json.loads(open('intents.json').read())   #load json file in read mode
words = pickle.load(open('words.pkl', 'rb'))
classes=pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):                    #function 
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))


def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if (i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result


print("Bot is ONLINE, Go a head..!!")

def chatbot_response(message):
    ints = predict_class(message, model)
    res = get_response(ints, intents)
    return res

def send():
    message = inputtxt2.get("1.0",END).strip()
    inputtxt2.delete("0.0",END)

    if message != '':
        inputtxt1.config(state=NORMAL)
        inputtxt1.insert(END, "You: " + message + '\n\n')    #message
        inputtxt1.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(message)  #message
        inputtxt1.insert(END, "Bot: " + res + '\n\n')
            
        inputtxt1.config(state=DISABLED)
        inputtxt1.yview(END)
        #my edditing of code 
    else:
        r = sr.Recognizer()

        def SpeakText(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()
        #while(1) removed try catch inside the while loop    
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                #print("Did you say: ", MyText)
                #SpeakText(MyText)
        except sr.RequestError as e:
            print("Could not request result; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occured")
        #coppy pased
        inputtxt1.config(state=NORMAL)
        inputtxt1.insert(END, "You: " + MyText + '\n\n')    #message
        inputtxt1.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(MyText)  #message
        inputtxt1.insert(END, "Bot: " + res + '\n\n')
            
        inputtxt1.config(state=DISABLED)
        inputtxt1.yview(END)
        #copy pased
    #//*****************************

    #text = inputtxt2.get(1.0, "end-1c")
    voice = tts.getProperty('voice')

    def setvoice():
        tts.setProperty('voice', voice[0])
        tts.say(res)
        tts.runAndWait()
        
    if(res):
        speed = 'fast'
        if(speed == 'fast'):
            tts.setProperty('rate', 175)
            setvoice()
        else:
            tts.setProperty('rate', 175)
            setvoice()
 

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
#----------------------------------------------------------------------------------------------------------------------
screen = Tk()                       
screen.title("ChatBot")             
screen.geometry('1000x550+300+200') 
screen.config(bg='white')           

logo_image = PhotoImage(file="iconbot.png")   
screen.iconphoto(False, logo_image)            

#First lable
lbl1 = Label(screen, text='Ask anything from me..!', font=('calibri', 12), bg='white').place(x = 20, y = 80)

#second lable with image
bg1 = PhotoImage(file='iconbot.png')
lable3 = Label(screen, height=180, width=180, bg='gray', image=bg1).place(x = 700, y = 80)

#First textbox
inputtxt2 = Text(screen, font=('calibri', 12), height = 6, width = 75, bg="#eee", border=0)
inputtxt2.place(x = 20, y = 120)

#button for get voice input
printButton2 = Button(screen, text = "Say me", font=('calibri', 12), command = send, width=15, height=2,border=0, bg='#1F456E', fg='white', cursor= 'hand2')
printButton2.place(x = 20, y = 250)

#button for sent text input
printButton1 = Button(screen,text = "Send", font=('calibri', 12), command = send, width=15, height=2,border=0, bg='#1F456E', fg='white', cursor='hand2')
printButton1.place(x = 150, y = 250)

#second image with lable
bg2 = PhotoImage(file='answer01.png')
lable3 = Label(screen, height=424, width=373, bg='gray', image=bg2).place(x = 20, y = 320)

#last lable 
lbl1 = Label(screen, text='Collect your answer from me..!', font=('calibri', 12), bg='white').place(x = 375, y = 360)

#final textbox
inputtxt1 = Text(screen, font=('calibri', 12), height = 6, width = 75, bg="#eee", border=0)
inputtxt1.place(x = 375, y = 390)



screen.mainloop()
