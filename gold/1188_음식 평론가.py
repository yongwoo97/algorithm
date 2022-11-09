#좀재밌어 보이는 문제네.
a ,b = map(int, input().split())

ans = 1
for i in range(min(a, b), 0, -1):
    if  a % i == 0 and b % i == 0:
        ans = i
        break

if ans == 1:
    print(b-1)
else:
    print(b-ans)