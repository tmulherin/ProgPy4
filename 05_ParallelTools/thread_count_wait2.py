#!/usr/bin/env python3.3
"""
    Use simple shared global data (not mutexes) to know when threads
    are done in parent/main thread; threads share list but not its items,
    assumes list won't move in memory once it has been initiated.
"""

import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10

def counter(myID, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s)' % (myID, i))
        stdoutmutex.release()
    exitmutexes[myID] = True  #signal main thread
    
for i in range(10):
    thread.start_new_thread(counter, (i, 100))
    
while False in exitmutexes: pass

print('Main thread exiting')    