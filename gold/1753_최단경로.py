#다익스트라 문제인데 어떻게 풀까?
'''
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())

graph = {i:[] for i in range(1, v+1)}

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

result = [float('inf')] * (v+1)
result[start] = 0
from collections import deque
def bfs(i):
    global graph
    q = deque()
    for x in range(len(graph[i])):
        q.append([i] + graph[i][x])

    while q:
        sta, end, count = q.popleft()
        if result[sta] + count < result[end]:
            result[end] = result[sta] + count
        for j in graph[end]:
            q.append([end] + j)


bfs(start)
for i in result[1:]:
    print(i)



'''
#메모리 초과로 한번 틀림
#heapq를 이용한 다익스트라 알고리즘

import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1].append((c, b-1))

q = []

result = [INF] * (v)
result[start-1] = 0

heapq.heappush(q, (0, start-1))

while q:

    weight, next = heapq.heappop(q)
    if result[next] < weight:
        continue
    for x, y in graph[next]:
        new = x + weight
        if result[y] > new:
            result[y] = new
            heapq.heappush(q, (new, y))

for i in result:
    if i == INF:
        print('INF')
    else:
        print(i)