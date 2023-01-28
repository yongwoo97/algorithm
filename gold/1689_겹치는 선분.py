import sys
import heapq

n = int(input())
q = []
for _ in range(n):
    line = list(map(int, input().split()))
    heapq.heappush(q, line)
max_1 = 0
max_2 = 0

start, end = heapq.heappop(q)

max_1 = end
check = True
count = 1
result = 0
result = max(result, count)
while q:
    x, y = heapq.heappop(q)
    if check:
        if x < max_1:
            count += 1
        elif x > max_1:
            max_1 = y
            check = True
            result = max(result, count)
            count = 1
            continue
        if y > max_1:
            max_2 = max_1
            max_1 = y
        else:
            max_2 = y
        check = False
        continue
    if x < max_2:
        count += 1
        result = max(result, count)
    elif x > max_1:
        max_1 = y
        check = True
        result = max(result, count)
        count = 1
        continue

    if y > max_1:
        max_2 = max_1
        max_1 = y
    elif max_1 > y > max_2:
        max_2 = y
    else:
        continue
result = max(result, count)
print(result)


