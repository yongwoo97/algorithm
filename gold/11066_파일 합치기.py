import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    #정렬을하고 양끝단 끼리 합친다, 배열을 계속 줄여나가면서 비용 업데이트
    price = 0
    long = int(input())
    data = list(map(int, input().split()))

    while True:
        if len(data) == 1:
         #   price += data[0]
            break
        data.sort()
        nd = []
        j = len(data) - 1
        for i in range(len(data)//2):
            price += data[i] + data[j-i]
            nd.append(data[i] + data[j-i])
        if len(data) % 2 == 1:
            nd.append(data[len(data)//2])
        data = nd
    print(price)