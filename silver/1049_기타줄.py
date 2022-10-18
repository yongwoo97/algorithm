import sys
input = sys.stdin.readline

n, m = map(int, input().split())

min_set = float('inf')
min_nat = float('inf')
for _ in range(m):
    a, b = map(int, input().split())
    min_set = min(min_set, a)
    min_nat = min(min_nat, b)

moc = n // 6
nam = n - (moc * 6)

if nam * min_nat >= min_set:
    print((moc + 1) * min_set)
elif min_set >= 6 * min_nat:
    print(n * min_nat)
else:
    print((moc * min_set) + (nam * min_nat))