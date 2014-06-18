#!/usr/bin/env python3.3

from sys import argv
from scanfile import scanner

class UnknownCommand(Exception): pass

commands = {'*': 'Ms.', '+':'Mr.'}

def processLine(line):
    try:
        print(commands[line[0]], line[1:-1])
    except:
        raise UnknownCommand(line)
    
filename = 'data2.txt'
if len(argv) == 2: filename = argv[1]
#print(filename)
scanner(filename, processLine)

