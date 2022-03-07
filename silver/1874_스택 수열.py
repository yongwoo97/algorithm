import sys
input = sys.stdin.readline

n = int(input())
stack = []
arr = []
for _ in range(n):
    k = int(input())
    arr.append(k)

point = 0
mem = []
for i in range(1, n + 1):
    while stack:
        if stack[-1] == arr[point]:
            mem.append('-')
            stack.pop()
            point += 1
        else:
            break
    mem.append('+')
    stack.append(i)



while stack:

    if stack[-1] == arr[point]:
        stack.pop()
        mem.append('-')
        point += 1
    else:
        print('NO')
        exit()

for i in mem:
    print(i)
