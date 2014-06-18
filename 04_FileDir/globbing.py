#!/usr/bin/env python3.3

import glob, os

dirname = r'/home/tim/dev/'

for file in glob.glob(dirname + '*/*/*'):
    head, tail = os.path.split(file)
    print(head, tail, '=>', ('/home/tim/dev/other/' + tail))
    
input()