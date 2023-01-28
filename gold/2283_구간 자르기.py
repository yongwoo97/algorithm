
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = []
result = []


set = set()
for _ in range(n):
    line = list(map(int, input().split()))
    data.append(line)
    set.add(line[1])
set = list(set)
set.sort()
rr = 0
i = 0
j = set[rr]

#종료 조건은 어떻게 해줘야 하지?
while i <= j:
    count = 0
    for x, y in data:
        right = min(j, y)
        left = max(i, x)
        if left < right:
            count += (right - left)
    print(i, j)
    if count == k:
        result.append([i, j])
        rr += 1
        if rr > len(set) - 1:
            rr = len(set) - 1
        j = set[rr]

    elif count > k:
        i += 1
    elif count < k:
        rr += 1
        if rr > len(set) - 1:
            rr = len(set) - 1
        j = set[rr]
print(result)
if not result:
    print(0, 0)
else:
    result.sort()
    print(*result[0])