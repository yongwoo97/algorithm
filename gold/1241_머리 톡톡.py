import sys
input = sys.stdin.readline

n = int(input())
data = [0] * 10000001
num = []
for _ in range(n):
    line = int(input())
    num.append(line)
    data[line] += 1

for i in num:
    count = 0

    k = 1
    while k * k <= i:
        if i % k == 0:
            if k * k != i:
                count += data[k] + data[i // k]
            else:
                count += data[k]
        k += 1

    print(count-1)
