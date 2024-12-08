with open('input.txt') as f:
    input_lines = f.readlines()


def solve(s, nums, part_id=2):
    if len(nums) == 1:
        return s == nums[0]
    
    s1 = s - nums[-1]
    b1 = s1 > 0

    s2 = s / nums[-1]
    b2 = s % nums[-1] == 0

    s3 = str(s)[:-len(str(nums[-1]))]
    b3 = part_id == 2 and (s3 != '') and str(s).endswith(str(nums[-1]))

    result = False
    for si, bi in ((s1, b1), (s2, b2), (s3, b3)):
        if bi:
            result = result or solve(int(si), nums[:-1], part_id)

    return result


acc = 0
for line in input_lines:
    s, rs = line.split(':')
    s = int(s.strip())
    nums = [int(n.strip()) for n in rs.split()]
    if solve(s, nums):
        acc += s

print(acc)


