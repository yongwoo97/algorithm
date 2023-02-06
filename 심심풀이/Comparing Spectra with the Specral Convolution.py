a = list(map(float, input().split()))
b = list(map(float, input().split()))

dic= {}
for i in a:
    for j in b:
        if i >= j:
            r = round(i-j, 5)
            if r in dic:
                dic[r] += 1
            else:
                dic[r] = 1
print(dic)