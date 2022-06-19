n, m = map(int, input().rstrip().split())

first = [list(map(int, input().rstrip().split())) for _ in range(n)]

mm, k = map(int, input().rstrip().split())

second = [list(map(int, input().rstrip().split())) for _ in range(m)]

result = []
for i in range(n):
    semi = []
    for j in range(k):
        re = 0
        for e in range(m):
            re += first[i][e] * second[e][j]
        semi.append(re)
    result.append(semi)

for i in result:
    print(*i)
