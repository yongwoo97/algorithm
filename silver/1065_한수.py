import sys

input = sys.stdin.readline
n = int(input())

def func(k):
    s = str(k)
    if k < 10:
        return 1
    init = 0
    check = False
    for i in range(1, len(s)):
        diff = int(s[i]) - int(s[i-1])
        if i == 1:
            init = diff
        else:
            if init != diff:
                check = True
            else:
                continue

    if check:
        return 0
    else:
        return 1


cnt = 0
for i in range(1, n+1):
    cnt += func(i)
print(cnt)