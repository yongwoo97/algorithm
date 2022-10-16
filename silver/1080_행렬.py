#첫번째 풀이는 일단 brute force로 간다. 떠오른 접근법부터 시작해

import sys
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
b = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def confirm(t, e):
    global n , m
    for i in range(n):
        for j in range(m):
            if t[i][j] != e[i][j]:
                return 0
    return 1

count = 0
for i in range(n):
    for j in range(m):
        if confirm(a, b):
            print(count)
            exit()
        if i + 2 < n and j + 2 < m:
            if a[i][j] != b[i][j]:
                count += 1
                for x in range(3):
                    for y in range(3):
                        if a[i+x][j+y] == 0:
                            a[i + x][j + y] = 1
                        else:
                            a[i + x][j + y] = 0



        else:
            continue
print(-1)