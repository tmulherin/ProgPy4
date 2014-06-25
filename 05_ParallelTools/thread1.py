#!/usr/bin/env python3.3

import _thread as thread

def child(tid):
    print('Hello from thread', tid)
    
def parent():
    i = 0
    while True:
        i += 1
        thread.start_new_thread(child, (i,))
        if input() == 'q': break
        
parent()


