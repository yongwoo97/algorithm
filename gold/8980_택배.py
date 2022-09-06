import sys
input = sys.stdin.readline

n, k = map(int, input().split())
i = int(input())
data = []
for _ in range(i):
    line = list(map(int, input().split()))
    data.append(line)
data.sort(key= lambda x : (x[1], x[0]))

arr = [0] * (n + 1)
score = 0
for i in data:
    a, b, c = i
    maxx = 0
    residue = 0
    for j in range(a, b):
        maxx = max(arr[j], maxx)
        #잔여 용량
        residue = k - maxx
        if c >= residue:
            c = residue
    score += c
    for j in range(a, b):
        arr[j] += c

print(score)





