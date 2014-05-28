#!python

from tkinter import *
from e003 import MyGUI

#==> main app window
mainwin = Tk()
lblMain = Label(mainwin, text = __name__)
lblMain.pack()

#==> popup window
popup = Toplevel()
lblPopup = Label(popup, text='Attach')
lblPopup.pack(side=LEFT)
MyGUI(popup).pack(side=RIGHT)
mainwin.mainloop()
