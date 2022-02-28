n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    s = c // a
    s1 = c % a
    if s1 == 0:
        s1 = a
        print(f'{s1}{s:02d}')

    else:
        print(f'{s1}{s+1:02d}')


