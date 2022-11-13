import sys
input = sys.stdin.readline
n, m  = map(int, input().split())
truth = list(map(int, input().split()))



real = [[-1, -1] for _ in range(51)]
quest = []
for x in range(1, truth[0]+1):
    num = truth[x]
    real[num][0] = 1

for _ in range(m):
    line = list(map(int, input().split()))
    quest.append(line)

#print(real)
i = 0
count = 0
while i < m:
    line = quest[i]
    num = line[0]
    #print(i, count, 'hello')
    check = False
    True_check = False
    d_check = False
    dd_check = False
    for j in range(1, num+1):
        numm = line[j]
        if real[numm][0] == 1:
            #check의 용도는 해당 파티에 진실을 알고 있는 사람이 존재하는 경우
            check = True
            for e in range(1, num + 1):
                num2 = line[e]
                if real[num2][0] == 0:
                    dd_check = True

            break
        elif real[numm][0] == -1:
            continue
        #거짓말 하는 사람 발견시
        elif real[numm][0] == 0:
            for k in range(1, num+1):
                numf = line[k]
                if real[numf][0] == 1:
                    True_check = True
            #예외 케이스지
            if True_check:
                for e in range(1, num + 1):
                    num2 = line[e]
                    real[num2][0] = 1
                i = 0
                count = 0
                d_check = True
                break
    if d_check:

        continue
   #print(check, dd_check)
    if check:

        if dd_check:
            i = 0
            count = 0
            for e in range(1, num + 1):
                num2 = line[e]
                real[num2][0] = 1

        else:
            i += 1
            for e in range(1, num + 1):
                num2 = line[e]
                real[num2][0] = 1

    else:

        count += 1
        for e in range(1, num + 1):
            num2 = line[e]
            real[num2][0] = 0
        i += 1
#print(real)
print(count)
