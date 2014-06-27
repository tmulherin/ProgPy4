#!/usr/bin/env python3.3
numConsumers = 2
numProducers = 4
numMessages = 4

import _thread as thread, queue, time

safePrint = thread.allocate_lock()
dataQueue = queue.Queue()

def producer(idnum, dataQueue):
    for msgnum in range(numMessages):
        time.sleep(idnum)
        dataQueue.put('[prducer id = %d, count=%d]' % (idnum, msgnum))
        
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
                
if __name__ == '__main__':
    for i in range(numConsumers):
        thread.start_new_thread(consumer, (i, dataQueue))
    for i in range(numProducers):
        thread.start_new_thread(producer, (i, dataQueue))
    time.sleep(((numProducers-1) * numMessages) - 1)
    print('Main thread exit')

#Arguments vs Globals