#방향 이 중복해서 나오는 사이값을 전체에서 빼준다.
import sys
input = sys.stdin.readline
n = int(input())
d = []
w = []
wi = 0
he = 0
di = {1:0, 2:0, 3:0, 4:0}
for _ in range(6):
    a, b = map(int, input().split())
    d.append(a)
    w.append(b)
    di[a] += 1
    if a == 3 or a == 4:
        he = max(he, b)
    elif a == 1 or a == 2:
        wi = max(wi, b)
result = []
for i in di:
    if di[i] == 2:
        result.append(i)
small = []
start = 0
for i in range(6):
    if d[i] in result:
        small.append(w[i])
    else:
        start = len(small)
if start >= 4:
    small = small[1:3]
elif start == 1:
    small = small[2:]
elif start == 2:
    small = [small[0], small[-1]]
elif start == 3:
    small = small[:2]
elif start == 0:
    small = small[1:3]
tot = ((he*wi) - (small[0] * small[1])) * n
print(tot)