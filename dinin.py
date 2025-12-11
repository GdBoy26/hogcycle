import threading
import time

forks = [threading.Lock() for _ in range(5)]

def dine(i):
    left = forks[i]
    right = forks[(i+1) % 5]

    print(f"P{i} is thinking")
    time.sleep(1)

    left.acquire()
    right.acquire()

    print(f"P{i} is eating")
    time.sleep(1)

    left.release()
    right.release()

for i in range(5):
    t = threading.Thread(target=dine, args=(i,))
    t.start()
