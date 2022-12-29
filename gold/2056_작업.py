#위상정렬 문제 인것 같다.

n = int(input())
degree = [[0, 0] for _ in range(n+1)]
weight = [0] * (n+1)
graph = {i:[] for i in range(1, n+1)}

for e in range(1, n+1):

    line = list(map(int, input().split()))



    wei = line[0]
    weight[e] = wei
    number = line[1]

    start = 2
    for k in range(number):
        idx = start + k
        graph[line[idx]].append(e)
        degree[e][0] += 1


result = 0
visited = [0] * (n + 1)

#print(weight)
def circle(i):
    global result, visited, degree, weight, graph

    if degree[i][0] == 0 and visited[i] == 0:
        visited[i] = 1
        result = max(result, degree[i][1] + weight[i])
        for j in graph[i]:
            degree[j][0] -= 1
            degree[j][1] = max(degree[i][1] + weight[i], degree[j][1])

from copy import deepcopy

while True:
    if sum(visited) == n:
        break
    degree_copy = deepcopy(degree)
    for k in range(1, n+1):

        if degree_copy[k][0] == 0 and visited[k] == 0:
            circle(k)


print(result)
#print(degree)



