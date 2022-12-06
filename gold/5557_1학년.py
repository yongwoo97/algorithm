n = int(input())
data = list(map(int, input().split()))
'''
count = 0
def func(a, i):
    global data, count, n

    if a > 20:
        return
    elif a < 0:
        return

    if i == n - 2:
        if a + data[i] == data[n-1]:
            count += 1
            return
        elif a - data[i] == data[n-1]:
            count += 1
            return
        else:
            return


    func(a + data[i], i + 1)
    func(a - data[i], i + 1)

func(0, 0)
print(count)
'''

#이 문제는  dp로 풀어야함
#dp의 형식을 떠올리는게 조금 어려운데... 음... 어떻게 하면될까?
#아래와 같이 하면된다.

dp = [[0] * 21 for _ in range(n-1)]


for i in range(n-1):

    if i == 0:
        dp[i][data[i]] += 1
        continue
    for j in range(21):
        if dp[i-1][j] > 0:
            if 0 <= j + data[i] <= 20:
                dp[i][j + data[i]] += dp[i-1][j]
            if 0 <= j - data[i] <= 20:
                dp[i][j - data[i]] += dp[i-1][j]
#print(data[-1])
print(dp[-1][data[-1]])