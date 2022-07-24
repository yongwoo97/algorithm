import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dp = [float('inf')] * n

def bellmanford(start):
    global graph, dp, n, m
    dp[start-1] = 0
    for i in range(n):
        if i == n-1:
            copy_dp = dp[:]
            #print(id(copy_dp), '^^', id(dp))
        for j in range(m):
            a, b, c = graph[j]
            if dp[b-1] > dp[a-1] + c:
                dp[b-1] = dp[a-1] + c
        if i == n-1 and copy_dp == dp:
            return True
    return False

result = bellmanford(1)
if not result:
    print(-1)
    exit()
#print(dp)
for i in dp[1:]:
    if i == float('inf'):
        print(-1)
    else:
        print(i)

