#이건 어떻게 풀더라?
#일단 union find부터


def find(x):
    if x != dp[x]:
        return find(dp[x])
    return x

def union(x, y):

    px = find(x)
    py = find(y)

    if px > py:
        dp[px] = py
    else:
        dp[py] = px

n, m = map(int, input().split())
edge = []
dp = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append([c, a, b])
edge.sort()

result = 0
visited = [0] * (n+1)
cur = 0
for i in range(m):
    c, a, b = edge[i]
    if find(a) == find(b):
        continue
    union(a, b)
    result += c
    cur = c

print(result-cur)
