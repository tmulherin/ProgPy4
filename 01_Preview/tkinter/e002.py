#!python

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='Popup', message='Button Pressed')

window = Tk()
button = Button(window, text='Press', command=reply)
button.pack()
window.mainloop()
