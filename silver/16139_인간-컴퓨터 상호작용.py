import sys
input = sys.stdin.readline

str1 = input().rstrip()
n = int(input())
di = {chr(i):[0] * (len(str1)+1) for i in range(97, 123)}

for i in range(1, len(str1) + 1):
    di[str1[i-1]][i] = di[str1[i-1]][i-1] + 1
    for j in range(97, 123):
        if chr(j) != str1[i-1]:
            di[chr(j)][i] = di[chr(j)][i-1]

for _ in range(n):
    a, b, c = input().rstrip().split()
    print(di[a][int(c)+1] - di[a][int(b)])