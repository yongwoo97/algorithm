import sys
from collections import defaultdict
input = sys.stdin.readline
dic = defaultdict(dict)
for _ in range(int(input())):
    line = input().strip()
    i = line[0]+line[-1] if len(line)>1 else line[0]
    k = ''.join(sorted(line[1:-1]))
    dic[i][k] = dic[i].get(k,0)+1
for _ in range(int(input())):
    ans = 1
    for line in input().strip().split():
        i = line[0]+line[-1] if len(line)>1 else line[0]
        k = ''.join(sorted(line[1:-1]))
        ans *= dic[i].get(k,0)
    print(ans)