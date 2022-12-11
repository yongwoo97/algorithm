#dp문제 같은데 구현이 살짝 섞여 있는 그런? 타입
#어디 한번 해볼까
#일단 간단하게 예제 한번해봐야지 이게 합당한 풀이 인지
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    data = []
    for _ in range(2):
        line = list(map(int, input().split()))
        data.append(line)

    result = 0


    for i in range(1, m):
        if i == 1:
            data[0][i] += data[1][i-1]
            data[1][i] += data[0][i-1]

        else:
            data[0][i] += max(data[1][i-1], data[1][i-2])
            data[1][i] += max(data[0][i - 1], data[0][i - 2])

    print(max(data[0][-1], data[1][-1]))