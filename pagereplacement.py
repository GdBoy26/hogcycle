frames = int(input("Frames: "))
pages = list(map(int, input("Pages: ").split()))

mem = [-1]*frames
faults = 0
pointer = 0

for p in pages:
    if p not in mem:
        mem[pointer] = p
        pointer = (pointer + 1) % frames
        faults += 1
    print("Page:", p, "=>", mem)

print("Faults:", faults)





frames = int(input("Frames: "))
pages = list(map(int, input("Pages: ").split()))

mem = []
faults = 0

for p in pages:
    if p in mem:
        mem.remove(p)
        mem.append(p)
    else:
        faults += 1
        if len(mem) < frames:
            mem.append(p)
        else:
            mem.pop(0)
            mem.append(p)
    print("Page:", p, "=>", mem)

print("Faults:", faults)






