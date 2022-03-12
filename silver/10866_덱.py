import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())

for _ in range(n):
    line = input().split()
    #print(line)
    if len(line) > 1:
        if line[0] == 'push_back':
            q.append(int(line[1]))
        else:
            q.appendleft(int(line[1]))
    else:
        if line[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif line[0] == 'back':
            if q:
                print(q[-1])
            else:
                print(-1)
        elif line[0] == 'size':
            print(len(q))
        elif line[0] == 'pop_front':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif line[0] == 'pop_back':
            if q:
                print(q.pop())
            else:
                print(-1)
        else:
            if q:
                print(0)
            else:
                print(1)