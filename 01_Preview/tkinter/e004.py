#!python

from tkinter import *
from tkinter.messagebox import showinfo
from os import path, system 

system('cls')

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')

top.iconbitmap(path.abspath('../../../text_x_python.ico'))

lblInput = Label(top, text="Enter your name:")
lblInput.pack(side=TOP)
entInput = Entry(top)
entInput.pack(side=TOP)
btnSubmit = Button(top, text="Submit", command=(lambda: reply(entInput.get())))
btnSubmit.pack(side=RIGHT)

top.mainloop()


