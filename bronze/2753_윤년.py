year = int(input())
if year % 4 == 0:
    if year % 400 == 0 or year % 100 != 0:
        print(1)
        exit()
    else:
        print(0)
else:
    print(0)