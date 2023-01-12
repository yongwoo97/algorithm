import math

a = int(input()) / 100
b = int(input()) / 100

#소수 확인하는 함수
def check(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


team1 = 0
team2 = 0
for i in range(19):
    if not check(i):
        team1 += math.factorial(18) / (math.factorial(i) * math.factorial(18 - i)) * (a ** i) * ((1- a) ** (18 - i))
        team2 += math.factorial(18) / (math.factorial(i) * math.factorial(18 - i)) * (b ** i) * ((1- b) ** (18 - i))

print(1 - (team1 * team2))