import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [i for i in range(n+1)]
def find(x):
    if dp[x] == x:
        return x
    return find(dp[x])

def union(x, y):

    xx = find(x)
    yy = find(y)

    if xx < yy:
        dp[yy] = dp[xx]
    else:
        dp[xx] = dp[yy]

count = 0
result = 0


graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()

for i in graph:
    if count == n-1:
        break
    c, a, b = i
    aa = find(a)
    bb = find(b)
    #print(aa, bb)
    if aa != bb:
        union(aa, bb)
        count += 1
        result += c
    #print(count, result)
print(result)

