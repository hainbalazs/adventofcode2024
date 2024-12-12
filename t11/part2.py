with open('input.txt', 'r') as f:
    inputs = [int(i) for i in f.readline().strip().split()]

def solve2(number, t, memo):
    if t == 0:
        return 1
    
    if (number, t) in memo:
        return memo[(number, t)]
    
    sn, ln = str(number), len(str(number))
    if number == 0:
        x = solve2(1, t-1, memo)
    elif ln % 2 == 0:
        ls = solve2(int(sn[:ln // 2]), t-1, memo)
        rs = solve2(int(sn[ln // 2:]), t-1, memo)
        x = ls + rs
    else:
        x = solve2(number * 2024, t-1, memo)

    memo[(number, t)] = x
    return x
    
acc = 0
T = 75
dp = {}
for n in inputs:
    acc += solve2(n, T, dp)

print(acc)
