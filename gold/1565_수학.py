n, m = map(int, input().split())
D = list(map(int, input().split()))
M = list(map(int, input().split()))

def fff(a, b):
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b

    return fff(b, a % b)

start = D[0]
for i in D[1:]:
    start = start * i // fff(start, i)

#인수분해
def div(nn):

    result = []
    for i in range(1, int(nn ** 0.5) + 1):
        if nn % i == 0:
            result.append(i)
            result.append(nn // i)
    return list(set(result))

r = []
for i in M:
    if not r:
        r = div(i)
    else:
        r = list(set(r).intersection(div(i)))
count = 0
for i in r:
    if i % start == 0:
        count += 1
print(count)