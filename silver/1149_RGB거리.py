import sys
input = sys.stdin.readline

n = int(input())

r = []
g = []
b = []

for _ in range(n):
    a, e, c = map(int, input().split())
    r.append(a)
    g.append(e)
    b.append(c)

#일단 초기화 시켜주고
dp1 = [r[0]]
dp2 = [g[0]]
dp3 = [b[0]]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            minn = min(dp2[i-1], dp3[i-1]) + r[i]
            dp1.append(minn)
        elif j == 1:
            minn = min(dp1[i-1], dp3[i-1]) + g[i]
            dp2.append(minn)
        else:
            minn = min(dp1[i-1], dp2[i-1]) + b[i]
            dp3.append(minn)
print(min(dp1[-1], dp2[-1], dp3[-1]))
