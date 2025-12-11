n = int(input("Enter number of processes: "))
bt = []
for i in range(n):
    bt.append(int(input(f"Burst time P{i+1}: ")))

wt = [0]*n
tat = [0]*n

for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

for i in range(n):
    tat[i] = wt[i] + bt[i]

print("\nProcess | BT | WT | TAT")
for i in range(n):
    print(f"P{i+1}\t {bt[i]}\t {wt[i]}\t {tat[i]}")





n = int(input("Enter number of processes: "))
bt = []
for i in range(n):
    bt.append((int(input(f"Burst time P{i+1}: ")), i+1))

bt.sort()  

wt = [0]*n
tat = [0]*n

for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1][0]

for i in range(n):
    tat[i] = wt[i] + bt[i][0]

print("\nProcess | BT | WT | TAT")
for i in range(n):
    print(f"P{bt[i][1]}\t {bt[i][0]}\t {wt[i]}\t {tat[i]}")





n = int(input("Enter number of processes: "))
bt = []
for i in range(n):
    bt.append(int(input(f"Burst time P{i+1}: ")))

qt = int(input("Enter time quantum: "))
rem = bt[:]
t = 0
wt = [0]*n
tat = [0]*n

queue = list(range(n))

while queue:
    p = queue.pop(0)
    if rem[p] > qt:
        t += qt
        rem[p] -= qt
        queue.append(p)
    else:
        t += rem[p]
        wt[p] = t - bt[p]
        tat[p] = t
        rem[p] = 0

print("\nProcess | BT | WT | TAT")
for i in range(n):
    print(f"P{i+1}\t {bt[i]}\t {wt[i]}\t {tat[i]}")
