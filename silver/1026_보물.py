import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
b.reverse()

total = 0
for i in range(n):
    total += (a[i] * b[i])
print(total)