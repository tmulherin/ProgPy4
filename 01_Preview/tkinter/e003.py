#!python

from tkinter import *
from tkinter.messagebox import showinfo

class MyGUI(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='Poput', message='Buttton pressed!')

if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()

