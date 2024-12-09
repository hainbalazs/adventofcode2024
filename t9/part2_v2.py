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
bw_blocks = [(bid, bsize) for (bid, bsize) in view[::-1] if bid is not None]
last_visited = [idx for idx, block in enumerate(view) if block[0] is not None]

for b_bid, b_bsize in bw_blocks:
    #print(to_str(view))
    # Optimization 1: keep a pointer to the index of the next file to be moved to the front
    l = last_visited.pop()

    # Optimization 2: keep a map where the first freespace with all possible sizes were
    first_i = first_gap[b_bsize] if first_gap[b_bsize] != 10 else 0

    # only iterate between the two
    for j in range(first_i, l + 1):
        bid, bsize = view[j]

        if bid is None:
            first_gap[bsize] = min(j, first_gap[bsize])  # Update gap tracker

        if bid is None and bsize >= b_bsize:  # Found a match
            if bsize == b_bsize:
                view[j] = (b_bid, b_bsize)
                view[l] = (None, bsize)
            else:
                view[j] = (b_bid, b_bsize)
                view[l] = (None, b_bsize)
                view.insert(j + 1, (None, bsize - b_bsize))
                first_gap[bsize - b_bsize] = min(first_gap[bsize - b_bsize], j + 1)

                for lvi in range(len(last_visited)):
                    if last_visited[lvi]  >= j+1:
                        last_visited[lvi] += 1
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
        
