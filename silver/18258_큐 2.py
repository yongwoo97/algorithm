import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    i = input().rstrip().split()
    if i[0] == 'push':
        q.append(int(i[1]))
    elif i[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif i[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(q))
    elif i[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif i[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)

