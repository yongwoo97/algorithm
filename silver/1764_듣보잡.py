import sys

input = sys.stdin.readline
n, k = map(int, input().split())

di = dict()
for _ in range(n+k):
    name = input().rstrip()
    if name in di:
        di[name] +=1
    else:
        di[name] = 1

result = []
for i in di:
    if di[i] == 2:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)