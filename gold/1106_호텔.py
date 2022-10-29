#단순한 그리디 문제같은데? 복병이 있나?
#최소라고 했으니 완전그리디한 문제보다는 dp를 활용해야 하나?
#우선순위 큐를 활용하는것도 나쁘지 않을것 같아. 이건 dp문제다

import sys
input = sys.stdin.readline
n, c = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(c)]

peo = {}
p = [float('inf')] * (6000)

for k, e in data:
    if e in peo:
        peo[e] = min(peo[e], k)
    else:
        peo[e] = k


p[0] = 0

for i in range(1, 2000):
    for j in peo:
        if 0 < i -j:
            p[i] = min(p[i-j] + peo[j], p[i])
        else:
            if j >= i:
                p[i] = min(p[i], peo[j])

print(p[n])

