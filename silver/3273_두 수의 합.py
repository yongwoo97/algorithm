n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

checker = [0] * 2000001
count = 0

for number in numbers:
    if x - number > 0:
        if checker[x-number] == 1:
            count += 1
    checker[number] = 1

print(count)