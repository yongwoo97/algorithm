num = int(input())
data = [input() for _ in range(num)]


result =0
for j in data:
    checker = {e: 0 for e in range(26)}
    memo = ''
    counter = True
    for i in j:
        if memo == i:
            continue
        elif checker[ord(i) - 97] == 0:
            checker[ord(i) - 97] = 1
            memo = i
        else:
            counter = False
            break
    if counter:
        result += 1
print(result)

