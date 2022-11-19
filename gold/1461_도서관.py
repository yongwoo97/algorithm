#단순 그리디 문제 혹은 완탐문제라고도 할 수 있다.
#이제 혼자서 해결책을 찾아보자
#어떤게 최적해를 보장할까 이걸 생각하는게 제일 힘들어... ㅠ
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
result = 0

if data[0] > 0:
    for k in range(n-1, -1, -1 * m):
        if k == n-1:
            result += abs(data[k])
        else:
            result += abs(data[k]) * 2
elif data[-1] < 0:
    for k in range(0, n, m):
        if k == 0:
            result += abs(data[k])
        else:
            result += abs(data[k] * 2)
else:
    temp = 0
    for i in range(n-1):
        if data[i] < 0 and data[i+1] > 0:
            temp = i
            break
    left = abs(data[0])
    right = abs(data[-1])
    if left > right:
        for k in range(0, temp+1, m):
            if k == 0:
                result += abs(data[k])
            else:
                result += abs(data[k]) * 2
        for k in range(n-1, temp, -1 * m):
            result += abs(data[k]) * 2
    else:
        for k in range(n-1, temp, -1 * m):
            if k == n-1:
                result += abs(data[k])
            else:
                result += abs(data[k]) * 2
        for k in range(0, temp+1, m):
            result += abs(data[k]) * 2








#print(data)
print(result)