import sys
input = sys.stdin.readline

n = int(input())
peo = [0] + list(map(int, input().split()))
data = {i:[] for i in range(1, n+1)}

for i in range(n):
    line = list(map(int,  input().split()))

    for j in line[1:]:
        data[i+1].append(j)

from itertools import combinations

#print(data)
node = [i for i in range(1, n+1)]

from collections import deque
def bfs(arr, last):
    visited = [0] * (n + 1)
    point1 = arr[0]
    point2 = last[0]

    q = deque()
    q.append(point1)


    result1 = []

    visited[point1] = 1
    while q:
        x = q.popleft()
        result1.append(x)
        for i in data[x]:
            if visited[i] == 0 and i in arr:
                visited[i] = 1
                q.append(i)
              #  result1.append(i)


    q = deque()
    q.append(point2)
    result2 = []

    visited[point2] = 1
    while q:
        x = q.popleft()
        result2.append(x)
        for i in data[x]:
            if visited[i] == 0 and i in last:
                visited[i] = 1
                q.append(i)
              #  result2.append(i)
    p1 = 0
    p2 = 0
    for i in result1:
        p1 += peo[i]

    for i in result2:
        p2 += peo[i]

    if sum(visited) == n:
       # print(p1, p2, result1, result2, 'd')
        return abs(p1 - p2)
    else:
        return -1



minn = float('inf')
for i in range(1, n//2 + 1):
    combi = list(combinations(node, i))
  #  print(combi)
    for j in combi:
        last = [k for k in node if k not in j]
     #   print(j, last, 'h')
        re = bfs(j, last)
     #   print(re, 'result')
        if re != -1:
            minn = min(minn, re)

if minn == float('inf'):
    print(-1)
else:
    print(minn)



