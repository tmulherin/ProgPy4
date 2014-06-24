#!/usr/bin/env python3.3

'''
    Fork basics: start 5 copies of this program running in parallel with
    the original; each copy counts up to 5 on the same stdout stream--forks
    copy process memory, including file descriptors; fork doesn't currently
    work on Windows without Cygwin:  use os.spawnv or multiprocessing on
    Windows instead; spawnv is roughly like fork+exec combinations.
'''

import os, time

def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s]=> %s' % (os.getpid(), i))

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('process %d spawned' % pid)
    else:
        counter(5)
        os._exit(0)

print('Main process exiting')

