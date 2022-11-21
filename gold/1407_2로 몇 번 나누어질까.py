a, b = map(int, input().split())

#1000000000000000

def func(k):
    count = 0
    while True:
        if k % 2 == 0:
            count += 1
            k = k // 2
        else:
            break
    return 2 ** count

result = 0
for i in range(a, b+1):
    result += func(i)
print(result)

a,b = map(int, input().split())

def calc(number) :
  if number == 0 :
    return 0
  elif number == 1 :
    return 1
  elif number % 2 == 0 :
    return number // 2 + 2 * calc(number // 2)
  elif number % 2 == 1 :
    return number // 2 + 2 * calc(number // 2) + 1

print(calc(b) - calc(a-1))