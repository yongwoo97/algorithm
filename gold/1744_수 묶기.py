n = int(input())
q = []
import heapq

for _ in range(n):
    heapq.heappush(q, int(input()))

count = 0
result = 0
semi = 0
while q and q[0] <= 0:
    x = heapq.heappop(q)
    if count % 2 == 0:
        semi += x
        count += 1
    elif count % 2 == 1:
        semi *= x
        count += 1
        result += semi
        semi = 0
result += semi
q.sort()
if not q:
    print(result)
    exit()

if len(q) % 2 == 0:
    for i in range(0, len(q), 2):
        if q[i] == 1 or q[i+1] == 1:
            result += q[i]
            result += q[i+1]
            continue
        result += q[i] * q[i+1]
else:
    result += q[0]
    for i in range(1, len(q), 2):
        if q[i] == 1 or q[i+1] == 1:
            result += q[i]
            result += q[i+1]
            continue
        result += q[i] * q[i+1]
print(result)