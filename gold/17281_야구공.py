import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

max_score = 0

def game(line):
    idx = 0
    score = 0
    for i in line:
       # print(i)
        outcount = 0
        b1, b2, b3 = 0, 0, 0
        while outcount < 3:
            if i[line_up[idx]] == 0:
                outcount += 1
            elif i[line_up[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif i[line_up[idx]] == 2:
                score += b3
                score += b2
                b1, b2, b3 = 0, 1, b1
            elif i[line_up[idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif i[line_up[idx]] == 4:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0

            idx = (idx + 1) % 9
    return score

maxx = 0
for i in permutations(range(1, 9), 8):
    line_up = list(i[:3]) + [0] + list(i[3:])
    #print(line_up)
    maxx = max(maxx, game(data))
print(maxx)