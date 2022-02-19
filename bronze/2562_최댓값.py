a = [int(input()) for _ in range(9)]

max1 = -1
index = -1
for i, j in enumerate(a):
    if j > max1:
        max1 = j
        index = i
print(max1)
print(index+1)


