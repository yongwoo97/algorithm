k = int(input())
a = [int(input()) for _ in range(k)]

re = []
for i in a:
    if i == 0:
        re.pop()
    else:
        re.append(i)
print(sum(re))