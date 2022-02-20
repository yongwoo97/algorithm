n = int(input())
data = list(map(int, input().split()))

counter = 0
for i in data:
    if i == 1:
        continue
    count = False
    for j in range(2, i):
        if i % j == 0:
            count = True
            break
    if not count:
        counter += 1
print(counter)