#!/usr/bin/env python3.3
numConsumers = 1
numProducers = 4
numMessages = 4

import threading , queue, time

safePrint = threading.Lock()
dataQueue = queue.Queue()

def producer(idnum, dataQueue):
    for msgnum in range(numMessages):
        time.sleep(idnum)
        dataQueue.put('[Message %d, from Producer=%d]' % (msgnum, idnum))
        
def consumer(idnum, dataQueue):
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safePrint:
                print('Consumer', idnum, 'got==>', data)
waitfor = []               
if __name__ == '__main__':
    for i in range(numConsumers):
        thread = threading.Thread(target=consumer, args=(i, dataQueue))
        thread.daemon = True
        thread.start()
    for i in range(numProducers):
        thread = threading.Thread(target=producer, args=(i, dataQueue))
        waitfor.append(thread)
        thread.start()
    for thread in waitfor: thread.join()
    print('Main thread exit')

#Arguments vs Globals