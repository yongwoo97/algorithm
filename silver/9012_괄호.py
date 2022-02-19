n = int(input())

stack = []
re = [list(input()) for _ in range(n)]
for re1 in re:
    stack = []
    for i in re1:
        if i == '(':
            stack.append(i)
        elif not stack:
            stack.append(')')
        elif stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(')')
    if stack:
        print('NO')
    else:
        print('YES')