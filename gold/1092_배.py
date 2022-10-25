#전형적인 그리디 문제인데
#어떤식으로 택배 문제랑 엮어서 풀 수 있을까?
#내가 제대로된 풀이를 알기는 아는것일까?
#이런 종류의 문제에는 조건이 있다. 반례가 숨어있다는 것
#어떤 반례인가 조건에 맞지 않는 크레인은 쉬면 안된다.
#가장 효율적인 전략을 구성하는것은 현실세계와 가장 인접한 풀이방법이라고 할 수 있다.
#그럼 어떤식으로 구현이 가능할까?
import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
k = int(input())
t = list(map(int, input().split()))
c.sort()
d = [0] * n
for i in range(k):
    for j in range(n):
        if t[i] <= c[j]:
            d[j] += 1
            break

if max(t) > c[-1]:
    print(-1)
else:

    count = 0
    while True:
        #print(d)
        if sum(d) == 0:
            break
        for i in range(n-1, -1, -1):
            if d[i] > 0:
                d[i] -= 1
            elif d[i] == 0:
                for j in range(i-1, -1, -1):
                    if d[j] > 0:
                        d[j] -= 1
                        break
        count += 1

    print(count)



