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

        for j, i in graph[cur_node]:
            if short_path[cur_node-1] + i > short_path[j-1]:
                continue
            if not visited[j-1]:
                short_path[j-1] = i + short_path[cur_node-1]
                heapq.heappush(q, (i, j))

        visited[cur_node-1] = 1
    return short_path
for _ in range(test):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    data = {i:[] for i in range(1, n+1)}

    rem = 0
    for _ in range(m):
        a,b,c = map(int, input().split())

        if g == a and h == b:
            rem = c
        elif g == b and h == a:
            rem = c

        data[a].append((b,c))
        data[b].append((a,c))

    hubo = []
    for _ in range(t):
        ee = int(input())
        hubo.append(ee)

    r1 = daicktra(data, s, 0)
    r2 = daicktra(data, g, 0)
    r3 = daicktra(data, h, 0)

    # s->g까지 가는거리
    dist1 = r1[g - 1]

    # s->h까지 가는거리
    dist2 = r1[h - 1]

    final = []

    for i in hubo:
        if i == g or i == h:
            final.append(i)
            continue
        if dist1 + rem + r3[i - 1] <= r1[i - 1] and dist2 + rem + r2[i - 1] <= r1[i - 1]:
            final.append(i)
    final.sort()

    print(*final)





