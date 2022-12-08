l = int(input())
m = int(input())
k = int(input())


import math

if k % 2 == 1:
    if l / k > ((k + 1) / 2):
        result = int(m/k) - math.ceil(l / k) + 1
    else:
        result = int(m/k) - ((k + 1) / 2) + 1
else:
    if math.ceil(l / (k/2)) >= k + 1:
        result = int(m/(k/2)) - math.ceil(l/(k/2)) + 1
        if k == 4 and math.ceil(l/(k/2)) <= 6 and int(m/(k/2)) >= 6:
            result -= 1
    else:
        result = int(m/(k/2)) - (k+1) + 1
        if k == 4 and int(m / (k/2)) >= 6:
            result -= 1
if result < 0:
    print(0)
else:
    print(int(result))