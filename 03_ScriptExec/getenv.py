#!c:\Python\Python.exe

from os import environ

myKeys = []

for key in environ.keys():
    myKeys.append(key)
 
maxlength = max(len(key) for key in myKeys)
myKeys.sort()

for key in myKeys:
    print(key.ljust(maxlength), '==> ', environ[key])
    
