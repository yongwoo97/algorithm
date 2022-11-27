#dfs 그래프 순회
#더 좋은 방법이 있을까?
#가중치를 1로 두고 플로이드 와샬써도 됨 그런데 뭐가 효율적일지는 고민을 해봐야지

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = {i:[] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


from collections import deque
def func(start, count):
    global graph, visited, counter


    q = deque()
    q.append([start, count])
    visited[start] = 1

    while q:
        x, y = q.popleft()

        counter[x] = y

        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append([i, y + 1])


m = float('inf')
result = 0
for i in range(1, n+1):
    visited = [0] * (n+1)
    counter = [0] * (n+1)

    func(i, 0)
    if sum(counter) < m:
        result = i
        m = sum(counter)

print(result)