import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

maxx = 0

for i in range(n):
    count = 0
    for j in range(n):
        #print(j, 'h')
        if i == j:
            continue
        elif i > j:
            check = False
            for k in range(j+1, i):
                result = (data[j] - data[i]) / (j - i) * (k - i) + data[i]
                if result <= data[k]:
                    check = True
                    break
            #print(check, '여기')
            if check:
                continue
            else:
                count += 1


        elif j > i:
            check = False
            #print('wer', j)
            for k in range(i+1, j):
                result = (data[j] - data[i]) / (j - i) * (k - i) + data[i]

                if result <= data[k]:
                    check = True
                    break
            if check:
                continue
            else:
                count += 1
    #print(count)
    maxx = max(maxx, count)
print(maxx)


