n = int(input())
data = list(map(int, input().split()))

result = [0] * n

for i in range(n):
    count = 0
    for j in range(n):
        if count >= data[i]:
            count = j
            break
        if result[j] > i + 1 or result[j] == 0:
            count += 1


    for j in range(count, n):
        if result[j] == 0:
            result[j] = i + 1
            break





print(*result)