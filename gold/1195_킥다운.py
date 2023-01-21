a = input().rstrip()
b = input().rstrip()

if len(a) < len(b):
    a, b = b, a
small = len(a)
#탬플릿은 a가 되겠지
a = '0' *(len(b)) + a + '0' *(len(b))

minn = float('inf')

#print(a)
for i in range(len(a)-len(b)+1):
    check = True
    count = 0
    #print(i)
    for j in range(i, i + len(b)):
        if a[j] == '0':
            count += 1
            continue
        elif int(a[j]) + int(b[j-i]) == 4:
            check = False

    if check:
      #  print(small, count)
        minn = min(minn, small + count)
print(minn)