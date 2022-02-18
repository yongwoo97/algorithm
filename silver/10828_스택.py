n = int(input())
order = [input() for _ in range(n)]
stack = []
for j in order:
    k = j.split()
    if len(k) >= 2:
        stack.append(int(k[-1]))
    elif k[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif k[0] == 'size':
        print(len(stack))
    elif k[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif k[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

