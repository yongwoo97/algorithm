import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_q = []
min_q = []

for _ in range(n):
    k = int(input())

    if len(max_q) <= len(min_q):
        heapq.heappush(max_q, k * -1)
    else:
        heapq.heappush(min_q, k)

    if len(max_q) > 0 and len(min_q) > 0 and (max_q[0] * -1) > min_q[0]:
        x = heapq.heappop(max_q)
        y = heapq.heappop(min_q)

        heapq.heappush(max_q, y * -1)
        heapq.heappush(min_q, x * -1)

    print(max_q[0] * -1)
