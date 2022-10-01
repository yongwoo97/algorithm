from itertools import permutations
n = int(input())
a = list(map(int, input().split()))

from copy import deepcopy
a1 = deepcopy(a)
a1.sort()

p = []
for i in range(n):
    idx = a1.index(a[i])
    p.append(idx)
    a1[idx] = -1
print(*p)


