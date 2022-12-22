bracket = input()

stack = []
visited = [0] * len(bracket)

def func(word):
    r = 0
    for i in range(word, len(bracket)):
        if visited[i] == 1:
            continue
        if bracket[i] == '(':
            stack.append(bracket[i])
            visited[i] = 1
            r += func(i+1)
        elif bracket[i] =='[':
            stack.append(bracket[i])
            visited[i] = 1
            r += func(i+1)
           # return r
        elif bracket[i] == ')' and stack and stack[-1] == '(':
            stack.pop()
            visited[i] = 1
            return 2 * max(1, r)
        elif bracket[i] == ']' and stack and  stack[-1] == '[':
            stack.pop()
            visited[i] = 1
            return 3 * max(1, r)
        else:
            print(0)
            exit()
    return r
r = func(0)
if stack:
    print(0)
else:
    print(r)