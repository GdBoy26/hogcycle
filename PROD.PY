import threading
import time
from queue import Queue

q = Queue(maxsize=5)

def producer():
    for i in range(10):
        q.put(i)
        print("Produced:", i)
        time.sleep(0.5)

def consumer():
    for i in range(10):
        item = q.get()
        print("Consumed:", item)
        time.sleep(1)

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
c.join()
