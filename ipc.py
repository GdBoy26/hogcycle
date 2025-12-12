import os

r, w = os.pipe()     # create pipe

pid = os.fork()

if pid > 0:          # parent
    os.close(r)
    msg = b"Hello Child"
    os.write(w, msg)
    os.close(w)

else:                # child
    os.close(w)
    output = os.read(r, 20)
    print("Child received:", output.decode())
    os.close(r)





from multiprocessing import Process, Semaphore
import time

sem = Semaphore(1)

def worker(name):
    sem.acquire()
    print(name, "entered critical section")
    time.sleep(1)
    print(name, "leaving")
    sem.release()

p1 = Process(target=worker, args=("Process-1",))
p2 = Process(target=worker, args=("Process-2",))

p1.start()
p2.start()

p1.join()
p2.join()






from multiprocessing import Process, Value

def child(num):
    num.value = 99

num = Value('i', 10)   # shared integer

p = Process(target=child, args=(num,))
p.start()
p.join()

print("Parent reads:", num.value)
