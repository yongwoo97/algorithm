import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
dp = [0] * (m + 1)
counter = 0
for _ in range(n):
    line = list(map(int, input().split()))
    data.append(line)
    c = 0
    for i in range(m):
        if line[i] != 0:
            c += 1
    if c == 1 or c == 0:
        check = False
        for i in range(m):
            if line[i] != 0:
                if dp[i+1] == 0:
                    dp[i+1] = 1
                    break
                else:
                    check = True
                    break
        if check:
            counter += 1
    else:
        counter += 1
if counter == 0:
    print(0)
else:
    print(counter - 1)



