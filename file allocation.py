disk = [0]*20   # 0 = free, 1 = allocated

def allocate_contiguous(start, length):
    if 1 in disk[start:start+length]:
        print("Cannot allocate (space already used)")
        return
    for i in range(start, start+length):
        disk[i] = 1
    print(f"File allocated from {start} to {start+length-1}")

allocate_contiguous(2, 5)
allocate_contiguous(10, 4)

print("Disk:", disk)





disk = [-1]*20   # -1 = free, otherwise next block number

def allocate_linked(blocks):
    for b in blocks:
        if disk[b] != -1:
            print("Block already allocated:", b)
            return
    for i in range(len(blocks)-1):
        disk[blocks[i]] = blocks[i+1]
    disk[blocks[-1]] = -1
    print("Linked List Chain:", blocks)

allocate_linked([3, 7, 9])
allocate_linked([11, 12, 18])

print("Disk:", disk)





index_table = {}   # file_name -> list of blocks
disk = [0]*20

def allocate_indexed(file, blocks):
    for b in blocks:
        if disk[b] == 1:
            print("Block in use:", b)
            return
    index_table[file] = blocks
    for b in blocks:
        disk[b] = 1
    print(f"{file} allocated blocks:", blocks)

allocate_indexed("fileA", [2, 6, 8])
allocate_indexed("fileB", [11, 15])

print("Index Table:", index_table)
