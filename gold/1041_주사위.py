import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

ju = [i for i in range(6)]

minn = float('inf')
comb2 = list(combinations(ju, 2))
for i in comb2:
    x, y = i
    if x + y == 5:
        continue
    else:
        minn = min(minn, data[x] + data[y])
comb2 = list(combinations(ju, 3))

minn2 = float('inf')
for i in comb2:
    x, y, z = i
    if x + y == 5 or y + z == 5 or x + z == 5:
        continue
    else:
        minn2 = min(minn2, data[x] + data[y] + data[z])



if n == 1:
    print(sum(data) - max(data))
else:
    three = 4 * minn2
    one = (4 * (n - 2) * (n-1)) + ((n-2) * (n-2))
    r_one = one * min(data)
    two = (4 * (n-1)) + ((n-2) * 4)
    r_two = two * minn

    print(three + r_one + r_two)

