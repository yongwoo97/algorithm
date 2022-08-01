import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(edge, (c, a, b))

parent = [i for i in range(n+1)]
visited = [0] * (n+1)
minn = 0
def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
result = 0

for n in range(m):

    w, x, y = heapq.heappop(edge)
    if find(x) != find(y):
        union(x, y)
        result += w
print(result)