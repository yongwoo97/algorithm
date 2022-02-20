n = int(input())


de = n
for i in range(1, n+1):
    if de - i > 0:
        de -= i
        continue
    else:
        if i % 2 == 0:
            print(f'{de}/{i-de+1}')
            break
        else:
            print(f'{i-de+1}/{de}')
            break
