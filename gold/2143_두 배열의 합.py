import sys
input = sys.stdin.readline

t = int(input())
alen = int(input())
Aarr = list(map(int, input().split()))
blen = int(input())
Barr = list(map(int, input().split()))

Asum = []
Bsum =[]
for i in range(alen):
    s = Aarr[i]
    Asum.append(s)
    for j in range(i+1, alen):
        s += Aarr[j]
        Asum.append(s)
for i in range(blen):
    s = Barr[i]
    Bsum.append(s)
    for j in range(i + 1, blen):
        s += Barr[j]
        Bsum.append(s)

import bisect
Bsum.sort()
Asum.sort()
result = 0
for i in range(len(Asum)):
    pivot = Asum[i]
    left = bisect.bisect_left(Bsum, t - pivot)
    right = bisect.bisect_right(Bsum, t - pivot)
    result += (right - left)
print(result)