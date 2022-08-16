import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
s1 = input().rstrip()
s2 = input().rstrip()

dp = [[0] * len(s2) for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0:
            if s1[i] == s2[j]:
                score = 1
            else:
                score = 0
            dp[i][j] = max(score, dp[i][j-1])
            continue
        if j == 0:
            if s1[i] == s2[j]:
                score = 1
            else:
                score = 0
            dp[i][j] = max(score, dp[i-1][j])
            continue
        if s1[i] == s2[j]:
            score = 1
        else:
            score = 0
        maxx = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + score)
        dp[i][j] = maxx

data = []
def dfs(x, y):
    
    #여기 분기처리에 문제가 있을것 같은데
    global data, s1, s2, dp
    if x == 0 and y == 0:
        if s2[x] == s1[y]:
            data.append(s2[x])
        return
    if x > 0 and y > 0:
        if s2[x] == s1[y]:
            data.append(s2[x])
            dfs(x-1, y-1)
        elif dp[y][x] == dp[y][x-1]:
            dfs(x-1, y)
        elif dp[y][x] == dp[y-1][x]:
            dfs(x, y-1)

    elif x == 0 and y > 0:
        if dp[y][x] - 1 == dp[y-1][x]:
            data.append(s2[x])
        dfs(x, y-1)
    elif y == 0 and x > 0:
        if dp[y][x] - 1 == dp[y][x-1]:
            data.append(s2[x])
        dfs(x-1, y)



dfs(len(s2)-1, len(s1)-1)
data.reverse()
print(len(data))
if len(data) == 0:
    exit()
print(''.join(data))
