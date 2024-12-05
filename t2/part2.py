import copy

path = "input.txt"
with open(path, 'r') as f:
    input_list = f.readlines()

def approach2(levels):
    diffs = [int(levels[i]) - int(levels[i+1]) for i in range(len(levels) - 1)]
    return (all(x > 0 for x in diffs) or all(x < 0 for x in diffs)) \
                and max(diffs) <= 3 and min(diffs) >= -3

acc = 0
for report in input_list:
    # analyzing a single report
    levels = report.split()
    if approach2(levels):
        acc += 1
    else:
        for i in range(len(levels)):
            levels_copy = copy.deepcopy(levels)
            levels_copy.pop(i)
            if approach2(levels_copy):
                acc += 1
                break

print(acc)
