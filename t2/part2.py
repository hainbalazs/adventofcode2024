path = "input.txt"
with open(path, 'r') as f:
    input_list = f.readlines()

def solution(levels):
    diffs = [int(levels[i]) - int(levels[i+1]) for i in range(len(levels) - 1)]
    postives = sum([x > 0 for x in diffs])
    negatives = sum([x < 0 for x in diffs])
    nulls = diffs.count(0)

    if (postives == 0 or negatives == 0) and nulls == 0 and max(diffs) <= 3 and min(diffs) >= -3:
        return True
    
    if 

acc = 0
for report in input_list:
    # analyzing a single report
    levels = report.split()
    if solution(levels):
        acc += 1
    

print(acc)
