n = int(input())
n1 = list(map(int, input().rstrip().split()))
m = int(input())
m1 = list(map(int, input().rstrip().split()))

s = {i: 1 for i in n1}

result = []
for i in m1:
    try:
        result.append(s[i])
    except:
        result.append(0)
print(*result)

