
s1 = input()
s2 = input()

dp = [[0] * len(s1) for _ in range(len(s2))]

for i in range(len(s2)):
    for j in range(len(s1)):
        if i == 0 and j == 0:
            score = 0
            if s2[i] == s1[j]:
                score = 1
            dp[i][j] = score
            continue
        elif i == 0:
            score = 0
            if s2[i] == s1[j]:
                score = 1
            dp[i][j] = max(dp[i][j-1], score)
        elif j == 0:
            score = 0
            if s2[i] == s1[j]:
                score = 1
            dp[i][j] = max(dp[i-1][j], score)
        else:
            score = 0
            if s2[i] == s1[j]:
                score = 1
            dp[i][j] = max(dp[i-1][j-1] + score, dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])