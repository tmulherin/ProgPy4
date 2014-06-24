#!/usr/bin/env python3.3

"Forks child process until you type 'q'"

import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0)
    
def parent():
    count = 0 
    while True:
        count += 1
        newpid = os.fork()
        print("count is %d, pid is %d" % (count, newpid))
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        
        if input() == 'q': break
parent()        