n, m = map(int, input().split())
s = [input().rstrip() for _ in range(n)]
d = [input().rstrip() for _ in range(m)]


s = set(s)

count = 0
for i in d:
    if i in s:
        count += 1

print(count)