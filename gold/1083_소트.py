#일단 재귀를 물어보는 문제 같긴해
#다만 사전순 비교는 스트링으로 바꿔서 해보자
#사전순으로 뒷서는건 어떻게 찾지?

n = int(input())
data = list(map(int, input().split()))
s = int(input())

start = 0
while s > 0 and start < n:

    count = 0
    maxx = data[start]

    for i in range(start + 1, min(start + s + 1, n)):
        if data[i] > maxx:
            maxx = data[i]
            count = i - start

    s -= count

    for j in range(count+start, start, -1):
        data[j] = data[j-1]
    data[start] = maxx
   # data[start], data[count + start] = data[count + start], data[start]

    start += 1

print(*data)
#도대체 어떤 차이가 이런 결과물을 만든것이지?
