n = int(input())
data = list(map(int, input().split()))

result = [0] * n

real_max = 0
for i in range(n):
    maxx = 0
    for j in range(i-1, -1, -1):
        if data[j] < data[i]:
            maxx = max(result[j], maxx)
        else:
            continue
    result[i] = maxx + 1
    real_max = max(real_max, maxx + 1)

print(real_max)

