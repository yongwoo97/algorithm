import sys
input = sys.stdin.readline
def comb(n, m):
    if not n:
        return []
    if len(n) == m:
        hap = []
        for i in n:
            hap += i
        return [hap]
    if m == 1 or len(n) == 1:
        return n
    if m == 0:
        return []

    semi = []
    for i in range(len(n)):
        first = n[i]
        next = comb(n[i+1:], m-1)
        for j in next:
            semi.append(first + j)
    return semi

N, M = map(int, input().split())
data = []
chicken = []
home = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            chicken.append([i, j])
        elif line[j] == 1:
            home.append([i, j, float('inf')])
    data.append(line)

c = comb(chicken, M)
minn = float('inf')
from copy import deepcopy

for i in c:
    home1 = deepcopy(home)
    for j in range(len(i) // 2):
        x = i[2 * j]
        y = i[2 * j + 1]
        for k in home1:
            dist = abs(k[0] - x) + abs(k[1] - y)
            if k[2] > dist:
                k[2] = dist
    su = 0
    for j in home1:
        su += j[2]
    if minn > su:
        minn = su

print(minn)

