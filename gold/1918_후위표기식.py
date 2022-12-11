a = input().rstrip()
stack = []

i = 0
result = ''

while i < len(a):
    cur = a[i]

    if cur == '+' or cur == '-':
        while stack and stack[-1] not in ['(', '+', '-']:
            result += stack.pop()
        if stack and stack[-1] in ['+', '-']:
            result += stack.pop()

    elif cur == '*' or cur == '/':
        while stack and stack[-1] not in ['+', '-', '(', '*', '/']:
            result += stack.pop()
        if stack and stack[-1] in ['*', '/']:
            result += stack.pop()
    elif cur == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
        if stack and stack[-1] in ['*', '/']:
            result += stack.pop()
        i += 1
        continue

    stack.append(cur)
    i += 1

while stack:
    p = stack.pop()
    if p == '(' or p == ')':
        continue
    result += p
print(result)