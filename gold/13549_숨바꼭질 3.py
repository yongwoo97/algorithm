import sys, heapq
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())


q = []
result = [float('inf')] * 100001
result[n] = 0
heapq.heappush(q, (0, n))

while q:
    cost, current = heapq.heappop(q)

    if current == k:
        break

    for i in range(3):
        if i == 0 and current > 0 and current <= 100000:
            if result[current-1] > cost:
                result[current-1] = cost + 1
                heapq.heappush(q, (cost+1, current-1))
        elif i == 1 and current >= 0 and current < 100000:
            if result[current+1] > cost:
                result[current+1] = cost + 1
                heapq.heappush(q, (cost+1, current+1))
        elif i == 2 and (2*current) <= 100000:
            if result[current*2] > cost:
                result[current*2] = cost
                heapq.heappush(q, (cost, current*2))

print(result[k])




'''
while q:
   # print(len(q))
    x, y = q.popleft()
    if x == k:
        result[x] = y
        break
    if result[x] < y:
        continue
    if result[x] > y:
        result[x] = y

    direction = [-1, 1, 2]
    for i in range(3):
        if i == 2 and (x*2) < 100001 and result[(x*2)] == float('inf'):
           # if result[(x*2)] < y:
            #    continue
            q.append((x*2, y))
            continue
        if (x+direction[i]) < 100001 and (x+direction[i]) >= 0 and result[(x+direction[i])] == float('inf'):
            #if result[x+direction[i]] < y+1:
            #    continue
            q.append((x+direction[i], y + 1))

print(result[k])
'''