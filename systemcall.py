import os

pid = os.fork()

if pid == 0:
    print("Child:", os.getpid())
else:
    print("Parent:", os.getpid(), "created child:", pid)





import os, time

pid = os.fork()

if pid == 0:
    time.sleep(1)
    print("Child done.")
else:
    os.wait()
    print("Parent waited for child.")





import os

print("Before exec")
os.execvp("ls", ["ls"])    # replaces program





import sys

print("Exiting program")
sys.exit(0)





import os
print("Process ID:", os.getpid())




import os
print("User ID:", os.getuid())




import os

try:
    os.setuid(os.getuid())   # setting same UID
    print("setuid successful")
except PermissionError:
    print("setuid not permitted")





import os

print("Old nice:", os.nice(0))
print("New nice:", os.nice(5))   # increase priority value





import time

print("Sleeping...")
time.sleep(2)
print("Awake!")




x = bytearray(1024)   # allocate memory
print("Memory allocated:", len(x), "bytes")

