#동전뒤집기
#이건 그때 뒤집는 문제랑 비슷해 (전구 켜기)
#완탐하기 보단 정답을 정해놓고 역추적으로 접근하는게 옳다
#홀짝 행을 다 홀로만들거나 짝으로 만들었을때 열에 남아있는 홀짝의 갯수를 카운팅해주면 답이된다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    line = list(map(int, list(input().rstrip())))
    data.append(line)
result = float('inf')
row = []
for i in range(n):
    semi = 0
    for j in range(m):
        semi += data[i][j]
    row.append(semi % 2)
col = []
for i in range(m):
    semi = 0
    for j in range(n):
        semi += data[j][i]
    col.append(semi % 2)

#col을 전부 홀 수로 만들어보자
count_col = 0
for i in col:
    if i % 2 == 0:
        count_col += 1

if count_col % 2 == 1:
    for i in range(n):
        if row[i] == 0:
            row[i] = 1
        else:
            row[i] = 0

#열이 전부 홀수 인경우에는 행의 홀수 개수가 홀수개 만큼 존재해야만 한다.
check1 = False
count_row = 0
for i in row:
    if i % 2 == 1:
        count_row += 1

if count_row % 2 == 1:
    result = min(result, count_col + count_row)
else:
    check1 = True

row = []
for i in range(n):
    semi = 0
    for j in range(m):
        semi += data[i][j]
    row.append(semi % 2)
col = []
for i in range(m):
    semi = 0
    for j in range(n):
        semi += data[j][i]
    col.append(semi % 2)
#이제 열을 모두 짝수로 바꿔보자
count_col = 0
for i in col:
    if i % 2 == 1:
        count_col += 1

if count_col % 2 == 1:
    for i in range(n):
        if row[i] == 0:
            row[i] = 1
        else:
            row[i] = 0

#짝수로 바뀐 경우에 행의 홀수 갯수는 짝수개 만큼 존재해야 한다.
check2 = False
count_row = 0

for i in row:
    if i % 2 == 1:
        count_row += 1
#print(count_col, count_row)
if count_row % 2 == 0:
    result = min(result, count_col + count_row)
else:
    chekc2 = True

if check1 and check2:
    print(-1)
else:
    print(result)
