import sys
input = sys.stdin.readline

n = int(input())
tx, ty = map(int, input().split())
k = int(input())
root = {i:[] for i in range(1, 101)}
for _ in range(k):
    a, b = map(int, input().split())
    root[a].append(b)
    root[b].append(a)

from collections import deque
def bfs(start, score, end):
    global root
    visited = [0] * 101
    q = deque()
    q.append((start, score))
    visited[start] = 1
    while q:
        pop, pop_s = q.popleft()
        if pop == end:
            return pop_s
        for i in root[pop]:
            if not visited[i]:
                q.append((i, pop_s+1))
                visited[i] = 1

    if not visited[end]:
        return -1
print(bfs(tx, 0, ty))