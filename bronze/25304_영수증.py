import sys
input =sys.stdin.readline

tot = int(input())
n = int(input())
s = 0
for _ in range(n):
    p, a = map(int,input().split())
    s += (p*a)
if s == tot:
    print('Yes')
else:
    print('No')