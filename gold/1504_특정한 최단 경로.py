import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

def func(start, end, g):
    q = []
    result = [float('inf')] * len(g)
    check = [0] * len(g)
    result[start] = 0

    heapq.heappush(q, (0, start))

    while q:

        wei, next = heapq.heappop(q)
        check[next] = 1
        for x, y in g[next]:
            if x > result[y]:
                continue

            new = wei + x

            if new < result[y]:
                result[y] = new
                if check[y] == 0:
                    heapq.heappush(q, (new, y))

    return result[end]

final1 = 0
final1 += func(1, v1, graph)
final1 += func(v1, v2, graph)
final1 += func(v2, v, graph)

final2 = 0
final2 += func(1, v2, graph)
final2 += func(v2, v1, graph)
final2 += func(v1, v, graph)

final = min(final1, final2)
if final == float('inf'):
    print(-1)
else:
    print(final)