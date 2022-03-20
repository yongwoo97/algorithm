import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
for _ in range(n):
    function = input().rstrip()
    length = int(input().rstrip())
    arr = deque(input().rstrip()[1:-1].split(','))
    if length == 0:
        arr = deque()

    check = False
    r_counter = 0
    for j in function:
        if j == 'R':
            r_counter += 1
        else:
            if not arr:
                print('error')
                check = True
                break
            if r_counter % 2 == 1:
                arr.pop()
            else:
                arr.popleft()
    if check:
        continue
    if r_counter % 2 == 1:
        arr.reverse()
    print('['+','.join(arr)+']')
