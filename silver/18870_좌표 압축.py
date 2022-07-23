import sys

input = sys.stdin.readline

n = int(input())
data = list((map(int, input().split())))

data1 = list(set(data))
data1.sort()

dic = dict()
for i in range(len(data1)):
    dic[data1[i]] = i

result = [dic[i] for i in data]
print(*result)