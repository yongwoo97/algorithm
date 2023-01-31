import sys
input = sys.stdin.readline

v, m = map(int, input().split())
d = 60 * v * m

count = 2
data = []
graph = {i:[] for i in range(1002)}
sx, sy = map(float, input().split())
data.append([0, sx, sy])
ex, ey = map(float, input().split())
data.append([1, ex, ey])
def dist(x1, y1, x2, y2):
    return ((abs(x1-x2) ** 2) + (abs(y2 - y1) ** 2)) ** 0.5

if dist(sx, sy, ex, ey) < d:
    while True:
        line = input()
        if not line:
            break
    print("Yes, visiting 0 other holes.")
    exit()

while True:
    line = input()
    if not line.strip():
        break
    x, y = map(float, line.split())
    for idx, xx, yy in data:
        #print(idx, xx, yy, count)
        if dist(x, y, xx, yy) < d:
            graph[idx].append(count)
            graph[count].append(idx)
    data.append([count, x, y])
    #()
    count += 1
from collections import deque

#print(graph)
def bfs():
    global graph
    q = deque()
    q.append([0, 0])
    dp = [0] * 1002
    dp[0] = 1

    while q:
        idx, cnt = q.popleft()

        for i in graph[idx]:
            if dp[i] == 0:
                q.append([i, cnt + 1])
                dp[i] = cnt + 1
    #print(dp)
    return dp[1]

result = bfs()
if result == 0:
    print("No.")
else:
    print(f"Yes, visiting {result - 1} other holes.")