import sys
input = sys.stdin.readline

def travel(cnt, cur):

    result = 0
    for i in cur:
        if i == 0:
            semi = cnt
        elif len(cur) > 1:
            semi = travel(cnt + 1, cur[i])
        elif len(cur) < 2 and cnt == 0:
            semi = travel(cnt + 1, cur[i])
        else:
            semi = travel(cnt, cur[i])
        result += semi

    return result


while True:
    n = input()
    if n:
        n = int(n)
    else:
        break

    trie = {}
    for i in range(n):
        line = input().rstrip()
        cur = trie
        for j in range(len(line)):
            if line[j] not in cur:
                cur[line[j]] = {}
            cur = cur[line[j]]
        cur[0] = True
    print(f'{travel(0, trie)/ n:.2f}')
