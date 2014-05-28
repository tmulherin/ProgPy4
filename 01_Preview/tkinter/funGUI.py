#!python

from tkinter import *
import random
fontsize = 30
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']

def onSpam():
    popup = Toplevel()
    color = random.choice(colors)
    lbl = Label(popup, text='Popup', bg='black', fg=color)
    lbl.pack(fill=BOTH)
    mainLabel.config(fg=color)

def onFlip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250, onFlip)

def onGrow():
    global fontsize
    fontsize += 5
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(100, onGrow)

main = Tk()
mainLabel = Label(main, text = 'Fun GUI', relief=RAISED)
mainLabel.config(font=('arial', fontsize, 'italic'), fg='cyan', bg='navy')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)
btnSpam = Button(main, text='Spam', command=onSpam)
btnSpam.pack(fill=X)
btnFlip = Button(main, text='Flip', command=onFlip)
btnFlip.pack(fill=X)
btnGrow = Button(main, text='Grow', command=onGrow)
btnGrow.pack(fill=X)
main.mainloop()



    