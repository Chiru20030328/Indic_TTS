import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
#import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import maincode as fvo
#import trans as ret

bgcolor="#56f0ed"
bgcolor1="#cc4806"
fgcolor="black"


def Home():
        global window
        
        
        def clear():
                
            print("Clear1")
            txt.delete(0, 'end') 
            txt1.delete(0, 'end') 
            
        def selection_changed(event):
                selection = combo.get()
                label1.config(text = selection)
        
        
            

        window = tk.Tk()
        var = IntVar()
        window.title("Multilingual Text To Speech Using AI")
        

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="Multilingual Text To Speech Using AI " ,bg=bgcolor  ,fg=fgcolor  ,width=70  ,height=2,font=('times', 25, 'italic bold underline')) 
        message1.place(x=50, y=10)

        lbl = tk.Label(window, text="Enter Your Text",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=150, y=150)
        
        txt = tk.Entry(window,width=50,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=400, y=150)
        lbl1 = tk.Label(window, text="Choose Language",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=150, y=220)
        combo = ttk.Combobox(window,values=["Assamese", "Bangla", "Boro", "Gujarati","Hindi", "Kannada", "Malayalam", "Manipuri", "Marathi","Oriya", "Rajasthani", "Tamil", "Telugu"])
        combo.bind("<<ComboboxSelected>>", selection_changed)
        combo.place(x=400, y=220)
        label1 = tk.Label(window, text="",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        label1.place(x=600, y=210)

        lbl1 = tk.Label(window, text="Converted Text",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=150, y=340)
        
        txt1 = tk.Entry(window,width=50,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=400, y=355)

        

        

        


        def lan1toeng():
                lang=label1.cget("text")
                #gen=label.cget("text")
                #gen1=int(gen)
                inptext=txt.get()
                print("Lang==",lang)
                #print("gen==",gen)
                print("inptext==",inptext)
                intext=txt.get()
                langcode=''
                if lang=="Assamese":
                        langcode='as'
                if lang=="Bangla":
                        langcode='bn'
                if lang=="Boro":
                        langcode='br'
                if lang=="Gujarati":
                        langcode='gu'
                if lang=="Hindi":
                        langcode='hi'
                if lang=="Kannada":
                        langcode='kn'
                if lang=="Malayalam":
                        langcode='ml'
                if lang=="Manipuri":
                        langcode='mni'
                if lang=="Marathi":
                        langcode='mr'
                if lang=="Oriya":
                        langcode='or'
                if lang=="Rajasthani":
                        langcode='raj'
                if lang=="Tamil":
                        langcode='ta'
                if lang=="Telugu":
                        langcode='te'
                #print("Gender=",gen)
                print("Lang=",lang)
                print("Langcode=",langcode)
                res=fvo.process(inptext,langcode)
                print("Result--",res)
                txt1.delete(0, 'end')
                txt1.insert('end',res)  
                


                


        

        browse = tk.Button(window, text="Convert", command=lan1toeng  ,fg="white"  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=250, y=500)


        clearButton = tk.Button(window, text="Clear", command=clear  ,fg="white"  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=620, y=500)
         
        

        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"   ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=990, y=500)

        window.mainloop()
Home()

