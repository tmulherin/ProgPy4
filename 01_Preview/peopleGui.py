#!/usr/bin/python3.3
"""
Implement a GUI for viewing and updating class instances stored in a shelve;
the shelve lives on the machine this scriot runs on, as 1 or more local files.
"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve
from os import path

shelvename = 'people-class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
#    window.iconbitmap(path.abspath(r'../../images/python.ico'))
#    imgpath = r"@/home/tim/dev/ProgPy4/01_Preview/python.gif"
#    img = PhotoImage(file=imgpath)
    window.iconbitmap(r"@python.xbm")
#    window.tk.call('wm', 'iconphoto', window._w, img)
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    btnFetch = Button(window, text="Fetch", command=fetchRecord)
    btnFetch.pack(side=LEFT)
    btnUpdate = Button(window, text="Update", command=updateRecord)
    btnUpdate.pack(side=LEFT)
    btnQuit = Button(window, text="Quit", command=window.quit)
    btnQuit.pack(side=RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key] #-> fetch by key, show in GUI
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        from person import Person
        record = Person(name='?', age='?')
   
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))

    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()




