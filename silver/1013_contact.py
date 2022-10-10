import sys, re
input = sys.stdin.readline
n = int(input())

p = re.compile('(100+1+|01)+$')

for _ in range(n):
    line = input().rstrip()

    if p.match(line):
        print('YES')
    else:
        print('NO')