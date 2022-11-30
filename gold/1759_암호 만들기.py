n, m = map(int, input().split())
data = input().split()

mo = []
ja = []
for i in data:
    if i in ['i', 'a', 'e', 'o', 'u']:
        mo.append(i)
    else:
        ja.append(i)

result = []
from itertools import permutations, combinations

for i in range(2, n):
    for j in range(len(mo), 0, -1):
        if i + j == n:
            ja_list = list(combinations(ja, i))
            mo_list = list(combinations(mo, j))
            for k in ja_list:
                for e in mo_list:
                    semi = list(k) + list(e)
                    semi.sort()
                    result.append(''.join(semi))
result.sort()
for i in result:
    print(i)

from copy import deepcopy
def comb(a, b):
    result = []
    if b == 1:
        for e in a:
            result.append([e])
        return result



    for i in range(len(a)-1):
        pivot = [a[i]]
        semi = comb(a[i+1:], b-1)

        for e in semi:
            s = pivot + e
            result.append(s)

    return result

def perm(a, b):
    result = []

    if b == 1:
        for e in a:
            result.append([e])
        return result

    for i in range(len(a)):
        pivot =[a[i]]
        semi = perm(a[:i] + a[i+1:], b-1)
        for e in semi:
            result.append(pivot + e)
    return result
print(perm(['a', 'b', 'c', 'd'], 3))