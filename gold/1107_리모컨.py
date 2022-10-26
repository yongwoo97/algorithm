import sys
input = sys.stdin.readline

target = input()
num = int(input())
if num != 0:
    data = list(map(int, input().split()))
if target == '100':
    print(0)
    exit()

button = [1] *10
for i in data:
    button[i] = 0

int_target = int(target)


count = 0

from copy import deepcopy
copy_target = list(deepcopy(target))
for e, i in enumerate(target):
    int_i = int(i)
    if button[int_i]:
        count += 1
    else:
        for k in range(1, 11):

            next_step = -1
            pre_step = -1

            if 0 <= int_i + k < 11:
                if data[int_i + k]:
                    next_step = int_i + k

            if 0 <= int_i - k < 11:
                if data[int_i - k]:
                    pre_step = int_i - k

            n_next_step = str(next_step)
            temp_target1 = copy_target[e]
            n_pre_step = str(pre_step)

            n_num = ''.join(copy




