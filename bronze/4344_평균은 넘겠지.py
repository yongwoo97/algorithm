#슬픈 진실을 깨우쳐주게 하기위한 문제
#이게 수학이다

n = int(input())
test = [list(map(int, input().split())) for _ in range(n)]

for k in test:

    avg = sum(k[1:]) / k[0]
    count = 0
    for j in k[1:]:
        if j > avg:
            count += 1
    result = round(count/k[0] * 100, 3)
    print(f'{result:0.3f}%')