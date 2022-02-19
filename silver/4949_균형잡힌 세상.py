line = input()

while line != '.':
    stack = []
    check = False
    for i in line:
        if i != '(' and i != ')' and i != '[' and i != ']':
            continue
        if i == '(' or i == '[':
            stack.append(i)
        elif not stack:
            if i == ')' or i == ']':
                check =True
                break

        elif stack[-1] == '(' and i == ')':
            stack.pop()
        elif stack[-1] == '[' and i == ']':
            stack.pop()
        else:
            stack.append(i)
    if check:
        print('no')
        line = input()
        continue
    if stack:
        print('no')
    else:
        print('yes')
    line = input()