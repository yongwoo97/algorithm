import sys
input = sys.stdin.readline

line = input().rstrip()

from collections import deque
visited = [0] * len(line)

stack = []

for i in range(len(line)):
    if line[i] == '(':
        stack.append(i)
    elif line[i] == ')':
        x = stack.pop()
        visited[x] = i


def func(start, end):
    global line
    i = start
    count = 0
    while i < end:
       # print(i)
        if i < end -1 and line[i+1] == '(':
            count += (int(line[i]) * func(i+2, visited[i+1]))
            i = visited[i+1] + 1
        else:
            count += 1
            i += 1
    return count

print(func(0, len(line)))
