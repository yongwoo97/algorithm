import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i:[] for i in range(1, 10001)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(cur):
    global graph
    count = 0

    if not graph[cur]:
        return 0

    q = deque()
    q.append(cur)

    visited = [0] * 10001
    visited[cur] = 1
    count += 1

    while q:
        x = q.popleft()


        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                count += 1

    return count

reuslt = []
maxx = 1
for i in range(1, 10001):
    semi = bfs(i)
    if semi > maxx:
        result = []
        result.append(i)
        maxx = semi
    elif semi == maxx:
        result.append(i)
    else:
        continue
result.sort()
print(*result)