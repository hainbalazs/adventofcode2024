path = "input.txt"
with open(path, 'r') as f:
    input_list = f.readlines()

tuples = [l.split() for l in input_list]
left_col = [int(x[0]) for x in tuples]
rigth_col = [int(x[1]) for x in tuples]

acc = 0
for l in left_col:
    acc += l * rigth_col.count(l)

print(acc)