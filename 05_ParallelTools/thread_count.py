#!/usr/bin/env python3.3

'''
    Thread basics: start 5 copies of a function running in parallel;
    uses time.sleep so that the main thread doesn't die too early--
    this kills all other threads on some platforms; stdout is shared:
    thread outputs may be intermixed in this version arbitrarily.
'''

import _thread as thread, time

def counter(myID, count):
    for i in range(count):
        time.sleep(1)
        print('[%s]=> %s' % (myID, i))

for i in range(5):
    thread.start_new_thread(counter, (i, 5))

time.sleep(10)
print('Main thread exiting')

