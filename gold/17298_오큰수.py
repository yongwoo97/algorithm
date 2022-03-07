n = int(input())
arr = list(map(int, input().split()))
d = [-1] * n

stack = []
for i, j in enumerate(arr):
    if not stack:
        stack.append((i, j))
        continue
    b = stack[-1][1]
    if b < j:
        while stack and b < j:
            a, b = stack.pop()
            d[a] = j
            if stack:
                a, b = stack[-1]
            else:
                break
        stack.append((i, j))
    else:
        stack.append((i, j))
print(*d)
