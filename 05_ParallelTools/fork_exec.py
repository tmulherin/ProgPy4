#!/usr/bin/env python3.3

import os

parm = 0

while True:
    parm += 1
    pid = os.fork()
    if pid == 0:
        os.execlp('python3', 'python3', 'fork1.py', str(parm))
        assert False, 'error starting program'
    else:
        print('Child is', pid)
        if input() == 'q': break
        