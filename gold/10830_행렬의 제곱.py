import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
data = [list(map(int, input().split())) for _ in range(a)]

remem = []

while b != 1:
    if b % 2 == 0:
        b = b // 2
        remem.append(2)
    else:
        b -= 1
        remem.append(1)
remem = remem[::-1]

def square(d):
    n = len(d)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cell = 0
            for t in range(n):
                cell += d[i][t] * d[t][j]
            result[i][j] = cell

    return result

def normal(d1, d2):
    n = len(d1)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cell = 0
            for t in range(n):
                cell += d1[i][t] * d2[t][j]
            result[i][j] = cell

    return result

r = data
for i in remem:
    if i == 2:
        r = square(r)
    else:
        r = normal(r, data)

for j in r:
    j = list(map(lambda x : x % 1000, j))
    print(*j)

#########################
#아래는 블로그 풀이
#재귀를 응용했다. 난 왜 이생각을 못했을까?
#후
'''
import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000

    return Z

def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    tmp = square(A, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

result = square(A, B)
for r in result:
    print(*r)
'''