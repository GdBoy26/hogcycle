import threading

def hello():
    for i in range(3):
        print("Hello from thread")

t = threading.Thread(target=hello)
t.start()
t.join()

print("Main thread finished")





import threading

count = 0
lock = threading.Lock()

def add():
    global count
    for i in range(1000):
        with lock:
            count += 1   # safe

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final count (correct):", count)
