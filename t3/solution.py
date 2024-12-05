import re

TASK_ID = 2
assert TASK_ID == 1 or TASK_ID == 2

with open ('input.txt', 'r') as f:
    input_code = f.read()

pattern_mul = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
multiplications = list(re.finditer(pattern=pattern_mul, string=input_code))

pattern_do = r"do?(n't)?"
dos = list(re.finditer(pattern=pattern_do, string=input_code))
d_i = 0
d = dos[d_i]

# by default multiplications are enabled
enabled = True

acc = 0
for m in multiplications:
    if d.end() <= m.start():
        # the current do/don't is before than the current mul(.,.)
        # check if it is the last one
        for dd in dos[d_i+1:]:
            if dd.end() <= m.start():
                d_i += 1
            else:
                break

        # the effect of the last do/don't should be active
        d = dos[d_i]
        enabled = d[0] == 'do'

    ls, rs = m.group(1), m.group(2)

    # since we're matching [0-9]+ it can match numbers that starts with a 0 but != 0, that is invalid
    if (ls.startswith('0') and len(ls) > 1) or (rs.startswith('0') and len(rs) > 1):
        print(f"mul({ls},{rs}) is a wrong format")
    elif enabled or TASK_ID == 1:
        acc += int(ls) * int(rs)

print(acc)