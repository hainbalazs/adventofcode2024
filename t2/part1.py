def approach1(levels):
    el1, el2 = int(levels[0]), int(levels[1])
    if el1 == el2:
        # unsafe moving on
        return False
    
    trend = "neg" if el1 > el2 else "pos"
    e = el1
    good = True

    for el in levels[1:]:
        el = int(el)
        if (trend == "neg" and not (0 < e - el <= 3)) or (trend == "pos" and not (0 < el - e <= 3)):
            good = False
            break
        e = el

    if good:
        return True
    
    return False

def approach2(levels):
    diffs = [int(levels[i]) - int(levels[i+1]) for i in range(len(levels) - 1)]
    return (all(x > 0 for x in diffs) or all(x < 0 for x in diffs)) \
                and max(diffs) <= 3 and min(diffs) >= -3

    
def solution(*args, approach=1):
    if approach == 1:
        return approach1(*args)
    else:
        return approach2(*args)
    

path = "input.txt"
with open(path, 'r') as f:
    input_list = f.readlines()

acc = 0
for report in input_list:
    # analyzing a single report
    levels = report.split()
    if solution(levels, approach=2):
        acc += 1
    

print(acc)
