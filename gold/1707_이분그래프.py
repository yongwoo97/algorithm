import sys
input = sys.stdin.readline

n = int(input())
from collections import deque

def bfs(x, start):
    global visited, graph, check
    q = deque()
    q.append(x)
    visited[x] = 1
    check[x] = start
    while q:
        p = q.popleft()
        for i in graph[p]:
            if visited[i] == 0:
                visited[i] = 1
                check[i] = -1 * check[p]
                q.append(i)
            else:
                if check[i] != check[p] * -1:
                    return False

    return True
for _ in range(n):
    a, b = map(int, input().split())
    graph = {i:[] for i in range(1, a+1)}
    for _ in range(b):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [0] * (a+1)
    check = [0] * (a+1)


    checker = False
    for k in range(1, a+1):
        if visited[k] == 0:
            result = bfs(k, 1)
            if not result:
                print('NO')
                checker = True
                break
    if checker:
        continue
    print('YES')
