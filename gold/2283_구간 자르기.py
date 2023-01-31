
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = [0] * 1000001
result = []

for _ in range(n):
    a, b = list(map(int, input().split()))
    for e in range(a+1, b+1):
        data[e] += 1
for i in range(1, len(data)):
    data[i] += data[i-1]

i = 0
j = 0

while j < len(data):
    check = False
    c = data[j]
    if c < k:
        j += 1
    elif c == k:
        result.append([i, j])
        break
    elif c > k:
        for e in range(j-1, -1, -1):
            if data[j] - data[e] == k:
                result.append([e, j])
                check = True
                break
            elif data[j] - data[e] < k:
                continue
            else:
                break
        if check:
            break
        j += 1

if not result:
    print(0, 0)
else:
    result.sort()
    print(result[0][0], result[0][1])