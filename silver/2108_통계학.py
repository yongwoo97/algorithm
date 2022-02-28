from collections import Counter
n = int(input())
data = [int(input()) for _ in range(n)]

data.sort()
c = Counter(data).most_common()
max1 = c[0][1]
semi = []
for i in c:
    if i[1] == max1:
        semi.append(i[0])



print(int(round(sum(data) / n, 0)))
print(data[n//2])
if len(semi) > 1:
    print(semi[1])
else:
    print(semi[0])
print(data[-1] - data[0])