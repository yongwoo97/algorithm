import sys
input = sys.stdin.readline

top = [list(map(int, list(input().rstrip()))) for _ in range(4)]
k = int(input())

def left(arr):
    temp = arr[0]
    arr.append(temp)
    return arr[1:]

def right(arr):
    temp = [arr[-1]]
    arr = temp + arr
    return arr[:-1]


for _ in range(k):
    a, b = map(int, input().split())

    ridx = a - 1 + 1
    leftidx = a - 1 - 1
    turntable = [0] * 4
    turntable[a-1] = b
    while True:
        if 0 <= ridx < 4:
            if top[ridx-1][2] + top[ridx][6] == 1:
                turntable[ridx] = -1 * turntable[ridx-1]
                ridx += 1
            else:
                break
        else:
            break

    while True:
        if 0 <= leftidx < 4:
            if top[leftidx+1][6] + top[leftidx][2] == 1:
                turntable[leftidx] = -1 * turntable[leftidx+1]
                leftidx -= 1
            else:
                break
        else:
            break

    for i in range(4):

        if turntable[i] == -1:
            top[i] = left(top[i])

        elif turntable[i] == 1:
            top[i] = right(top[i])

        else:
            continue
result = 0

for i in range(4):
    if top[i][0] == 1:
        if i == 0:
            result += 1
        elif i == 1:
            result += 2
        elif i == 2:
            result += 4
        elif i == 3:
            result += 8
print(result)