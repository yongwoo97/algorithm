import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int , list(input().rstrip()))) for _ in range(n)]

maxx = -1
for i in range(n):
    for j in range(m):
        for k in range(-1 * (n), n):
            for e in range(-1 * (m), m):

                if k == 0 and e == 0:

                    continue
                #건너 띌 수 k, e가 정해졌어
                cnt = 0
                pick = ''
                while True:
                    ni = i + (k * cnt)
                    nj = j + (e * cnt)
                    if 0 <= ni < n and 0 <= nj < m:
                        pick += str(data[ni][nj])
                        cnt += 1
                        result = int(pick)
                        result = result ** (1 / 2)
                        if result % 1 == 0:
                            maxx = max(int(pick), maxx)
                    else:
                        break



print(maxx)