import sys
from itertools import permutations

input = sys.stdin.readline
diction = {}

n = int(input())
for _ in range(n):
    line = input().rstrip()
    diction[line] = 1

m = int(input())
#from copy import deepcopy
for _ in range(m):
    line = input().rstrip().split()
    result = 0

    for i in line:

        if len(i) < 3:
            if i in diction:
                if result == 0:
                    result += 1
                else:
                    result *= 1
        else:
            ni = i[1:-1]
            permute = set(list(permutations(ni, len(ni))))

            count = 0

            for k in permute:
                l = list(k)
                new_word = i[0] + ''.join(l) + i[-1]
                if new_word in diction:
                    count += 1

            if result == 0:
                result += count
            else:
                result *= count
    print(result)