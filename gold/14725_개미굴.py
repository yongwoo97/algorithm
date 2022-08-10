import sys
input = sys.stdin.readline

n = int(input())
trie = {}

def travel(t, l):
    if 0 in t:
        return
    #sorted(t)
    for i in range(len(t)):
        temp = sorted(t)
        print('--' * l, temp[i], sep='')
        travel(t[temp[i]], l + 1)

for _ in range(n):
    line = input().rstrip().split()
    k = int(line[0])
    line = line[1:]

    cur = trie
    for i in range(k):
        if line[i] not in cur:
            cur[line[i]] = {}
        cur = cur[line[i]]
    cur[0] = 1

travel(trie, 0)



