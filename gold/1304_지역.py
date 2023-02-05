#일단 고속도로는 고정이니까 앞에서부터 나누면 되고 뒤로 오는게 있는지 확인만하면된다.
#이래서 brute force인데 나는 왜 생각을 못했을까.


import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = {i:[] for i in range(1, n+1)}
for i in range(1, n):
    graph[i].append(i+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(start):
    global group, visited
    r = True

    for i in graph[start]:
        print(start, i, group[start], group[i])
        if group[i] < group[start]:
            return False
        if visited[i] == 0:
            visited[i] = 1
            r = dfs(i)
            if not r:
                return False
    return r
maxx = 1
for i in range(1, n+1):
    if n % i == 0:
        group = [0]
        for j in range(1, i+1):
            group += [j] * (n // i)
        visited = [0] * (n+1)
        visited[n // i] = 1

        result = dfs(n // i)
        print(n // i, result, i)
        if result:
            maxx = max(maxx, i)
print(maxx)