
line = input().rstrip()
visited = [0] * len(line)
def func(start, cur):
    global visited
    if line[start] == ')' and cur == '(':
        visited[start] = 1
        return 1
    elif line[start] == ']' and cur == '[':
        visited[start] = 1
        return 1

    result = 0
    for i in range(start, len(line)-1):
        if cur == '[' and line[i] == ']':
            return result
        if cur == '(' and line[i] == ')':
            return result
        if visited[i] == 1:
            continue
        if line[i] == '(':
            result += (2 * func(i+1, '('))
        elif line[i] == '[':
            result += (3 * func(i+1, '['))
        visited[i] = 1
    #print(result)
    return result
r = 0
for i in range(len(line)):
    if visited[i] == 0:
        r += func(i, '')
        print(r)
print(r)