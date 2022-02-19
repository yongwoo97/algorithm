n = int(input())

re = [input().rstrip() for _ in range(n)]

for i in re:
    count = 0
    total = 0
    for j in i:
        if j == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)