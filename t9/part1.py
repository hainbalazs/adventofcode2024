import time
with open('input.txt', 'r') as f:
    diskmap = list(f.readline().strip())

start_time = time.time()
checksum, ci = 0, 0
start, end = 0, len(diskmap) - 1

if end % 2 != 0:
    end -= 1

while start <= end:
    if start % 2 == 0:
        # actual file
        block_id = start // 2
        block_size = int(diskmap[start])

        for i in range(block_size):
            checksum += ci*block_id
            ci += 1

        start += 1
    else:
        # free space
        block_id = end // 2
        block_size = int(diskmap[end])
        capacity = int(diskmap[start])

        if block_size > capacity:
            diskmap[end] = str(block_size - capacity)
            for i in range(capacity):
                checksum += ci * block_id
                ci += 1
            
            start += 1
        elif block_size == capacity:
            for i in range(capacity):
                checksum += ci * block_id
                ci += 1

            start += 1
            end -= 2
        else:
            for i in range(block_size):
                checksum += ci * block_id
                ci += 1

            diskmap[start] = str(capacity - block_size)
            end -= 2
print(checksum)
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        
