import sys

input = sys.stdin.readline
n = int(input())
s = {i:0 for i in range(1, 21)}
for _ in range(n):
    com = input().split()
    if len(com) > 1:
        com[1] = int(com[1])
    if com[0] == 'add':
        s[com[1]] = 1
    elif com[0] == 'check':

        if s[com[1]]:
            print(1)
        else:
            print(0)
    elif com[0] == 'remove':
        if s[com[1]]:
            s[com[1]] = 0
        else:
            continue
    elif com[0] == 'toggle':
        if s[com[1]]:
            s[com[1]] = 0
        else:
            s[com[1]] = 1
    elif com[0] == 'all':
        s = {i:1 for i in range(1, 21)}
    elif com[0] == 'empty':
        s = {i:0 for i in range(1, 21)}
