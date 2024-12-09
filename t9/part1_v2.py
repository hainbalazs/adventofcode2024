import time

with open('input.txt', 'r') as f:
    diskmap = list(f.readline().strip())

def strip_free_space(l):
    while l[-1] == '.':
        l.pop()

    return l

start_time = time.time()

diskmap_view = []
for block_id2, block_size in enumerate(diskmap):
    if block_id2 % 2 == 0:
        diskmap_view += [str(block_id2 // 2)] * int(block_size)
    else:
        diskmap_view += ['.'] * int(block_size)

n_dots = diskmap_view.count('.')
n_blocks = len(diskmap_view) - n_dots

strip_free_space(diskmap_view)
defragmented = []
for block in diskmap_view:
    if block == '.':
        defragmented.append(diskmap_view.pop())
        strip_free_space(diskmap_view)
    else:
        defragmented.append(block)

checksum = 0
for i, block in enumerate(defragmented):
    checksum += i*int(block)

print(checksum)
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")