import time, sys, Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

m = QueueManager(address=('127.0.0.1', 5000), authkey='abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

def f(x):
    return x*x	

for i in range(0, 10):
    try:
        n = task.get(timeout=1)
        r = map(f, [n])
        print "run task %d*%d:%d" %(n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print 'task queue is empty'
        
print 'thread exit'
