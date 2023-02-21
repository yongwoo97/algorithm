def func(arr):

    sum1 = 0
    sum2 = 0
    for i in range(6):
        sum1 += arr[i][0]
        sum2 += arr[i][2]

    if sum1 != sum2:
        return 0

    for i in range(6):
        semi = 0
        for j in range(3):
            semi += arr[i][j]

        if semi != 5:
            return 0
    count = 0
    minus = 1
    for i in range(6):
        count += arr[i][1] * minus
        minus *= -1
    if count != 0:
        return 0
    return 1

result = []
for i in range(4):
    line = list(map(int, input().split()))
    data = []
    for j in range(0, len(line), 3):
        data.append(line[j:j+3])
    result.append(func(data))
print(*result)
