#!/usr/bin/env python3.3

import threading

class MyThread(threading.Thread):
    def __init__(self, myID, count, mutex):
        self.myID = myID
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)
    
    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s)' % (self.myID, i))
                
stdoutmutex = threading.Lock()
threads = []

for i in range(10):
    thread = MyThread(i, 100, stdoutmutex)
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
    
print('Main thread exiting')    