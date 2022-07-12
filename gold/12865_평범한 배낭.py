import sys
input = sys.stdin.readline

n, k1 = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
'''
mmax = 0
def combination(n, k):
    global mmax, k1
    if k == 1 or len(n) < 1:
        return n


    for j in range(len(n)):
        pick = n[j]
        rest = combination(n[j+1:], k-1)

        result = []
        for i in rest:
            if i[0] + pick[0] > k1:
                continue
            else:
                result.append([i[0] + pick[0], i[1] + pick[1]])
                mmax = max(i[1] + pick[1], mmax)

    return result


for i in range(1, n+1):
    semi = combination(data, i)
'''
#메모리초과가 떳다 어떻게하면 다 계산하지 않고 선택적으로 사용할 수 있을까?
#dp를 이용하자
dp = [[0] * (k1 + 1) for _ in range(n + 1)]


for i in range(1, n+1):
    pick = data[i-1]
    for j in range(1, k1 + 1):
        if j - pick[0] < 0:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-pick[0]] + pick[1])

print(dp[-1][-1])
