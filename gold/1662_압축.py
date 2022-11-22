import sys
input = sys.stdin.readline

line = input().rstrip()

from collections import deque
def func(a):

    q = deque()
    i = 0
    count = ''
    while True:
        #print(q)
        if q and q[-1] == ')':
            q.pop()
            semi = ''
            while True:
                x = q.pop()
                if x == '(':
                    x1 = int(q.pop())
                    semi *= x1
                    q.append(semi)
                    break
                else:
                    semi += x
        elif i < len(a):
            q.append(a[i])
            i += 1
        elif not q and i >= len(a):
            break
        else:
            k = q.pop()
            count += k
    return count

print(len(func(line)))