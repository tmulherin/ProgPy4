#!c:\Python\Python.exe

import os

print('setenv.....', end=' ')
print(os.environ['USERNAME'])

os.environ['USERNAME'] = "Fred"
os.system('python echoenv.py')

os.environ['USERNAME'] = "Ethyl"    
os.system('python echoenv.py')

os.environ['USERNAME'] = input('?')
print(os.popen('python echoenv.py').read())

