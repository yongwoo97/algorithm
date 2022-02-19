a = [int(input()) for _ in range(3)]
r = 1

for k in a:
    r *= k

r = str(r)
dic = {str(j): 0 for j in range(10)}
for i in r:
    dic[i] += 1

for i in dic:
    print(dic[i])

