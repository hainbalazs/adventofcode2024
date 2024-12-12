with open('input.txt', 'r') as f:
    inputs = [int(i) for i in f.readline().strip().split()]

T = 25

def split_until_can(n, i):
    sn = str(n)
    ln = len(sn)
    if ln % 2 != 0 or i == T:
        return ((n, i),)
    else:                    
        return (*split_until_can(int(sn[:ln // 2]), i+1), *split_until_can(int(sn[ln // 2:]), i+1))
    

# memoization part - precompute single digit numbers
dp = {i: [] for i in range(10)}

for i in range(1,10):
    num = [i]
    for t in range(T):
        new_num = []
        for num_i in num:
            sn, ln = str(num_i), len(str(num_i))
            if num_i == 0:
                new_num.append(1)
            elif ln % 2 == 0:
                new_num.extend([int(sn[:ln // 2]), int(sn[ln // 2:])])
            else:
                new_num.append(num_i * 2024)
        
        dp[i].append(new_num)
        num = new_num
            
dp[0] = [[1], *dp[1][:-1]]

# solving the problem
stack = [(i,0) for i in inputs[::-1]]
result = []


while len(stack) > 0:
    num, t = stack.pop()
    while t < T:
        if num in dp:
            future = dp[num][T - t - 1]
            for f in future[:0:-1]:
                stack.append((f, T))
            num, t = future[0], T
        else:
            sn, ln = str(num), len(str(num))
            if num == 0:
                num, t = 1, t+1
            elif ln % 2 == 0:
                seq = split_until_can(num, t)
                for s in seq[:0:-1]:
                    stack.append(s)
                num, t = seq[0]
            else:
                num, t = num * 2024, t + 1

    result.append(num)

#print(result)
print(len(result))