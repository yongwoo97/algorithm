line = list(map(int, input().split()))
data = [1, 1, 2, 2, 2, 8]
for i in range(len(data)):
    print(data[i]-line[i], end = ' ')