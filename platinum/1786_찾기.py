#kmp 알고리즘을 활용한 문자열 탐색
#패턴에서 앞뒤가 같은 경우를 계산해서 틀린지점 부터 시작하는게 핵심 그런데 구현은 어떻게 하면 될까?
# 그것이 문제로다
#시간초과 풀이

t = input()
p = input()

def match(text, pat, start):
    check = True
    for i in range(start, start + len(pat)):
        j = i - start

        if text[i] == pat[j]:
            continue
        else:
            check = False
            if j <= 1:
                return False, start + 1
            for k in range(j-1, 1, -1):
                if pat[:k] == pat[j - k:j]:
                    return False, start + j - k

                else:
                    continue

    if not check:
        return False, start + 1

    if check:
        j = len(pat)
        if j <= 1:
            return True, start + 1
        for k in range(j-1, 1, -1):
            if pat[:k] == pat[j - k:j]:
                return True, start + j - k

            else:
                continue
        return True, start + j

init = 0
count = 0
pos = []
while init <= len(t) - len(p):
    a, b = match(t, p, init)
    #print(a, b)
    if a:
        count += 1
        pos.append(init + 1)
    init = b

print(count)
print(' '.join(list(map(str, pos))))