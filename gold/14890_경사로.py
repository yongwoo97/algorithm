import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

def search(mapp):
    global n, k
    bridge = [[0] * n for _ in range(n)]
    score = 0
    for i in range(n):
        j = 0
        while j < n - 1:
            if mapp[i][j] == mapp[i][j+1]:
                j += 1
            elif mapp[i][j] == mapp[i][j+1] - 1:
                counter = 0
                for e in range(j, -1, -1):
                    if mapp[i][e] == mapp[i][j] and bridge[i][e] == 0:
                        counter += 1
                    else:
                        break
                    if counter >= k:
                        break
                if counter == k:
                    j += 1
                    for x in range(1, k+1):
                        bridge[i][j-x] = 1
                    continue
                else:
                    break
            elif mapp[i][j] == mapp[i][j+1] + 1:
                counter = 0
                for e in range(j+1, j+k+1):
                    if mapp[i][e] == mapp[i][j+1] and bridge[i][e] == 0:
                        counter += 1
                    else:
                        break
                    if counter >= k:
                        break
                if counter >= k:
                    j += 1
                    for x in range(k):
                        bridge[i][x+j] = 1
                    continue
                else:
                    break
            else:
                break
        #print(j)
        if j == n-1:
           # print(i)
            score += 1
    return score

data1 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        data1[i][j] = data[j][i]
#print(data1)
print(search(data) + search(data1))