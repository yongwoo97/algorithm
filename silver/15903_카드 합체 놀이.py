import sys
n,  m = map(int, input().split())
data = list(map(int,input().split()))
q = []
import heapq
for i in data:
    heapq.heappush(q, i)
count = 0
while count < m:

    x = heapq.heappop(q)
    y = heapq.heappop(q)
    new = x + y

    heapq.heappush(q, new)
    heapq.heappush(q, new)
    count += 1
print(sum(q))