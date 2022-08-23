import sys
input = sys.stdin.readline

str1 = input().rstrip()
n = int(input())
di = {chr(i):[0] * len(str1) for i in range(97, 123)}

for i, j in enumerate(str1):
    if i == 0:
    di[j][i] = di[]