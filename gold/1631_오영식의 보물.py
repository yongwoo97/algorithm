n, m = map(int, input().split())
target = list(input().rstrip())
start = ['A'] * n
#print(target)
#print(start)
idx = n-1
dp = [1]
for i in range(30):
    dp.append(sum(dp) + 1)

mem = target[idx]

check = False
check1 = False
while idx >= -1:
    #if not check:
    #    while idx >= 0 and target[idx] == start[idx]:
    #        idx -= 1
    #    check = True
    #    mem = target[idx]
    #    continue
    #print(m, idx, start)
    if m <= 0:
        print(''.join(start))
        exit()
        break
    if not check1:
        mem = target[idx]
        #만약에 계속 같으면 mem이 업데이트 되는건 확실하잖아?
        #음...

    if dp[idx] <= m and start[idx] != mem:
        #print(m)
        t = mem
        for i in ['A', 'B', 'C']:
            if i != mem and i != start[idx]:
                t = i
                break
        start[idx] = mem
        for i in range(idx-1, -1, -1):
            start[i] = t

        m -= dp[idx]

    elif dp[idx] > m and start[idx] != mem:
        for i in ['A', 'B', 'C']:
            if i != mem and i != start[idx]:
                mem = i
                break
        check1 = True
    else:
        pass
    idx -= 1
print(start)

