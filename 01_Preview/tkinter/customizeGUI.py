#!python

from tkinter import mainloop
from tkinter.messagebox import showinfo
from e003 import MyGUI

class CustomGUI(MyGUI):
    def reply(self):
        showinfo(title='Customized Popup', message='Ouch!!!')

if __name__ == '__main__':
    CustomGUI().pack()
    mainloop()
