from collections import deque
import sys

input = sys.stdin.readline
maxx = 100000
dist = [0] * (maxx + 1)

q = deque()
a, b = map(int, input().split())


def bfs():
    global q, b
    while q:
        cur = q.popleft()
        if cur == b:
            print(dist[cur])
            break
        else:
            for i in [cur - 1, cur + 1, cur * 2]:
                if i >= 0 and i <= maxx and dist[i] == 0:
                    dist[i] = dist[cur] + 1
                    q.append(i)


q.append(a)
bfs()
