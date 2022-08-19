h, m = map(int,input().split())
s = int(input())
h1 = s // 60
m1 = s - (h1 * 60)

fh = h + h1


fm = m + m1
if fm > 59:
    fm = fm - 60
    fh += 1
if fh > 23:
    fh = fh - 24
print(fh, fm)