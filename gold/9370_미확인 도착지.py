import sys
import heapq
input = sys.stdin.readline

test = int(input())
def daicktra(graph, start, cnt):

    visited = [0] * (len(graph))
    short_path = [float('inf')] * (len(graph))
    q = []
    heapq.heappush(q, (cnt, start))
    short_path[start-1] = 0
    visited[start-1] = 0
    while q:
        wei, cur_node = heapq.heappop(q)
        if short_path[cur_node-1] < wei:
            continue
        for j, i in graph[cur_node]:
            if short_path[j-1] > i + short_path[cur_node-1]:
                short_path[j-1] = i + short_path[cur_node-1]
                heapq.heappush(q, (i, j))

        visited[cur_node-1] = 1
    return short_path
for _ in range(test):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    data = {i:[] for i in range(1, n+1)}

    for _ in range(m):
        a,b,c = map(int, input().split())

        if g == a and h == b:
            c -= 0.1
        elif g == b and h == a:
            c -= 0.1

        data[a].append((b,c))
        data[b].append((a,c))

    hubo = []
    for _ in range(t):
        ee = int(input())
        hubo.append(ee)

    r1 = daicktra(data, s, 0)
    final = []
    for i in hubo:
        if r1[i-1] == float('inf'):
            continue
        elif type(r1[i-1]) == float:
            final.append(i)
    final.sort()
    print(*final)





