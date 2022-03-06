import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    a = tuple(map(int, input().split()))
    q.append(a)
q.sort()
for i in q:
    print(*i)
