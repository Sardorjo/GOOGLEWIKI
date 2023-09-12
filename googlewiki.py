# -*- coding: utf-8 -*-
"""
New project

Date: 04/09/2023

Name of project: Translater bot

Created by Sardorbek Khamrakulov
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import wikipedia


root = Tk()
root.title("Google Wiki")
root.geometry('600x400')
root.resizable(False,False)

framel = Frame(root, width=600, height=400, bg="#A4A4A4")
framel.place(x=0, y=0)

l = tk.StringVar()
choose_language = ttk.Combobox(framel, width=2, textvariable=l, state='randomly', font=('verdana', 13, 'bold'))

choose_language['values'] = ( # we added the googletrans languages
                        'ru',
                        'en',
                        "uz",
                        ) 
choose_language.place(x=110, y=110)
choose_language.current(0)
choose_language.config(foreground="#6C6B6B")

Label(framel, text="Google",font=("Helvetica 50 bold"), bg="#A4A4A4", fg="#6C6B6B").place(x=170,y=20)

text_entry1 = Text(width=21, height=1.4, font=("verdena", 14), fg="#6C6B6B")
text_entry1.place(x=165, y=110)

text_entry2 = Text(framel, width=32, height=10, fg="#6C6B6B", font=("verdena", 14))
text_entry2.place(x=110, y=150)

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')
    
def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()
    try:
        text_entry2.delete(1.0, 'end')
        wikipedia.set_lang(cl)
        text_entry2.insert('end', wikipedia.summary(lang_1))
    except:
        messagebox.showerror('Translater AI', 'No such article found!!!')


btn1 = Button(framel, text="🔎", command=translate, relief=RAISED, borderwidth=3, fg="#6C6B6B", cursor="hand2")
btn1.place(x=410, y=110)

btn2 = Button(framel, text="clr", command=clear, relief=RAISED, borderwidth=3, fg="#6C6B6B", cursor="hand2")
btn2.place(x=440, y=110)

mainloop()
