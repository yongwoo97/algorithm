import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
score = 0
def dfs(pos, x1, y1):
    global score
    if x1 == n-1 and y1 == n-1:
        score += 1
        return
    if pos == 0:
        for i in range(2):
            if i == 0:
                if y1 + 1 < n and data[x1][y1+1] == 0:
                    dfs(0, x1, y1 + 1)

            elif i == 1:
                if x1 + 1 < n and y1 + 1 < n:
                    if data[x1][y1 + 1] == 0 and data[x1 + 1][y1] == 0 and data[x1+1][y1+1] == 0:
                        dfs(2, x1+1, y1+1)

    elif pos == 1:
        for i in range(2):
            if i == 0:
                if x1 + 1 < n and data[x1+1][y1] == 0:
                    dfs(1, x1 + 1, y1)

            elif i == 1:
                if x1 + 1 < n and y1 + 1 < n:
                    if data[x1][y1 + 1] == 0 and data[x1 + 1][y1] == 0 and data[x1+1][y1+1] == 0:
                        dfs(2, x1+1, y1+1)

    else:
        for i in range(3):
            if i == 0:
                if y1 + 1 < n and data[x1][y1+1] == 0:
                    dfs(0, x1, y1 + 1)

            elif i == 1:
                if x1 + 1 < n and data[x1+1][y1] == 0:
                    dfs(1, x1 + 1, y1)

            elif i == 2:
                if x1 + 1 < n and y1 + 1 < n:
                    if data[x1][y1 + 1] == 0 and data[x1 + 1][y1] == 0 and data[x1+1][y1+1] == 0:
                        dfs(2, x1 + 1, y1 + 1)

dfs(0, 0, 1)
print(score)

#아래 코드는 공통부분을 합쳐줘서 시간초과를 해결한다
#이걸 어떻게 dp로 풀었을까?
# 파이프 옮기기 2번 을 풀면된다.
import sys
input = sys.stdin.readline
n = int(input().strip())
board = []
for i in range(n):
    board.append(list(map(int, input().strip().split())))
#0가로 1세로 2대각
result = 0
def dfs(x2,y2,d):
    global result
    if x2 == n-1 and y2 == n-1:
            result += 1
    if d == 0 or d == 2:
        ny2 = y2 + 1
        if ny2 < n and board[x2][ny2] == 0:
            dfs(x2, ny2, 0)

    if d == 1 or d ==2:
        nx2 = x2 + 1
        if nx2 < n and board[nx2][y2] == 0:
            dfs(nx2, y2, 1)
    nx2 =x2 + 1
    ny2 = y2 +1
    if nx2 < n and ny2 < n and board[nx2][ny2] == 0 and board[nx2][ny2 - 1] == 0 and board[nx2 - 1][ny2] == 0:
        dfs(nx2, ny2, 2)

if board[n-1][n-1] == 1:
    print(0)
else:
    dfs(0,1,0)
    print(result)