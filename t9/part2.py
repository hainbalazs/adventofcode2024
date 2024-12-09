import time
with open('input.txt', 'r') as f:
    diskmap = list(f.readline().strip())

def to_str(l):
    out = ""
    for i, s in l:
        out += str(i if i is not None else '.') * s
    return out

start_time = time.time()
view = []
for block_id, block_size in enumerate(diskmap):
    if block_id % 2 == 0:
        view.append((block_id // 2, int(block_size)))
    else:
        view.append((None, int(block_size)))

first_gap = [10 for _ in range(10)]
bw_blocks = [(bid, bsize) for (bid, bsize) in view[::-1] if bid != None]
new_view = list(view)

for b_bid, b_bsize in bw_blocks:
    for k, (x, y) in enumerate(view[::-1]):
        if (x,y) == (b_bid, b_bsize):
            l = len(view) - 1 - k

    first_i = first_gap[b_bsize] if first_gap[b_bsize] != 10 else 0
    for i, (bid, bsize) in enumerate(view):
        j = i
        if j > l:  # cannot be moved
            break 

        if bid is None:
            first_gap[bsize] = min(j, first_gap[bsize])
        
        if bid is None and bsize >= b_bsize:    # found a match, moving
            if bsize == b_bsize:
                view[j] = (b_bid, b_bsize)
                view[l] = (None, bsize)
            else:
                view[j] = (b_bid, b_bsize)
                view[l] = (None, b_bsize)
                view.insert(i+1, (None, bsize - b_bsize))
                first_gap[bsize - b_bsize] = min(first_gap[bsize - b_bsize], j+1)
            break

#print(to_str(view))
checksum, i = 0, 0
for bid, bsize in view:
    for j in range(bsize):
        if bid is not None:
            checksum += i*bid
        i += 1

print(checksum)

end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        
