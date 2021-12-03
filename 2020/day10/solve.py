#!/usr/bin/env python3

nums = []
with open("input") as f:
    nums = list(map(int, f))

#
# def dfs(l, acc):
#     if len(l) == len(acc):
#         return check(acc)
#
#     for i in range(len(l)):
#         if (i not in acc) and (l[i] - l[acc[-1]] < 4):
#             newacc = acc + [i]
#             r = dfs(l, newacc)
#             if r:
#                 return r
#     1/0

ones = 0
threes =1
nums.sort()
for i, e in enumerate(nums):
    if i == 0:
        if e - 0 == 1:
            ones += 1
        elif e - 0 == 3:
            threes += 1

    if e - nums[i-1] == 1:
        ones += 1

    elif e - nums[i-1] == 3:
        threes += 1

    # print(e - nums[i-1])

print(ones * threes)
