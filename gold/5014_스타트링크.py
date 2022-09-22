import sys
from collections import deque
import heapq
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
dp = [-1] * 1000001
ud = [u, (-1 * d)]
def bfs():
    global dp
    q = []
    heapq.heappush(q, (abs(g-s), s, 0))

    while q:
        wei, node, count = heapq.heappop(q)
        if node == g:
            dp[node] = count
            return
        for i in range(2):
            next_node = node + ud[i]
            next_wei = abs(next_node - g)
            if 1 <= next_node <= f and dp[next_node] == -1:
                heapq.heappush(q, (next_wei, next_node, count + 1))
                dp[next_node] = count + 1


bfs()
if dp[g] == -1:
    print('use the stairs')
else:
    print(dp[g])


