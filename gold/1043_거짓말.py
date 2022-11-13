import sys
input = sys.stdin.readline
n, m  = map(int, input().split())
truth = list(map(int, input().split()))

real = [-1] * 51

quest = []
for x in range(1, truth[0]+1):
    num = truth[x]
    real[num] = 1

for _ in range(m):
    line = list(map(int, input().split()))
    quest.append(line)


i = 0
count = 0
while i < m:
    line = quest[i]
    num = line[0]
    check = False
    d_check = False
    for j in range(1, num+1):
        if real[line[j]] == -1:
            continue

        elif real[line[j]] == 1:
            for x in range(1, num+1):
                if real[line[x]] == 0:
                    i = 0
                    count = 0
                    check = True
            for y in range(1, num + 1):
                real[line[y]] = 1
            if not check:
                d_check = True
        elif real[line[j]] == 0:
            for x in range(1, num+1):
                if real[line[x]] == 1:
                    i = 0
                    count = 0
                    for y in range(1, num+1):
                        real[line[y]] = 1
                    check = True

    if check:
        continue
    else:
        if d_check:
            i += 1
            continue
        count += 1
        i += 1
        for y in range(1, num + 1):
            real[line[y]] = 0

print(count)
