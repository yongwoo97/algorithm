minn, maxx = map(int, input().split())
x, y = map(int, input().split())

if minn > maxx:
    minn, maxx = maxx, minn

if y < 0 or y >= abs(x):
    print("Unknwon Number")
    exit()

start = minn // x
if x < 0:
    start += 1

count = 0
result = 0
while True:
    if minn <= start * x + y <= maxx:
        count += 1
        if count == 1:
            result = start * x + y

        if count >= 2:
            break

    if maxx < start * x + y:
        break

    if x < 0:
        start -= 1
    else:
        start += 1


if count == 1:
    print(result)
else:
    print("Unknwon Number")