#단순 구현 문제인데.
#31%에서 터지네

import sys
input = sys.stdin.readline

n = int(input())
data = [list(input().rstrip()) for _ in range(5)]
'''
s = [[] for _ in range(n)]

ss = ###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###
ss = ss.split()
num = [[] for _ in range(10)]
for e in ss:
    line = list(e)
   # print(line)
    for x in range(0, 39, 4):
        num[x // 4].append(line[x:x+3])
'''
num = [[['#', '#', '#'], ['#', '.', '#'], ['#', '.', '#'], ['#', '.', '#'], ['#', '#', '#']], [['.', '.', '#'], ['.', '.', '#'], ['.', '.', '#'], ['.', '.', '#'], ['.', '.', '#']], [['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#'], ['#', '.', '.'], ['#', '#', '#']], [['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#']], [['#', '.', '#'], ['#', '.', '#'], ['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#']], [['#', '#', '#'], ['#', '.', '.'], ['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#']], [['#', '#', '#'], ['#', '.', '.'], ['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#']], [['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#'], ['.', '.', '#'], ['.', '.', '#']], [['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#']], [['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#'], ['.', '.', '#'], ['#', '#', '#']]]
#위의 코드는 문제가 아니야
#어디 부분에서 시간을 이렇게 잡아먹는거지:?


def num1(e):
    for i in range(10):
        if e == num[i]:
            return i
    else:
        return -1

from itertools import combinations
from copy import deepcopy

def check(k):
    global data
    start = 0 + (k * 4)
    end = 2 + (k * 4)
    result = []
    com = []
    #아래 코드는 꺼져 있는 전구의 위치값을 알기 위해서 하는 코드
    for i in range(5):
        for j in range(start, end + 1):
            if data[i][j] == '.':
                com.append([i, j])


    for i in range(0, len(com) + 1):

        comb = list(combinations(com, i))
        if i != 0:

            for t in comb:
                temp = deepcopy(data)
                for tt in t:
                    temp[tt[0]][tt[1]] = '#'
                temp1 = []
                for e in range(5):
                    temp1.append(temp[e][start:end + 1])

                nn = num1(temp1)

                if nn != -1:
                    result.append(nn)

        else:
            temp1 = []
            temp = deepcopy(data)
            for e in range(5):
                temp1.append(temp[e][start:end+1])
            nn = num1(temp1)
            if nn != -1:
                result.append(nn)

    return result

r= []
for i in range(n):
    semi = check(i)
    if data[1][4 * i + 1] == '#' or data[3][4 * i +1] == '#':
        print(-1)
        exit()
    elif semi:
        r.append(check(i))
    else:
        print(-1)
        exit()

def recur(cycle, pre):
    global n, summ, count, r
    if cycle == n:
        summ += int(pre)
        count += 1
        return

    for i in range(len(r[cycle])):
        recur(cycle + 1, pre + str(r[cycle][i]))

#recur(0, '')
#print(float(summ / count))

c = n
summ = 0
count = 1

co = 1
for e in range(len(r)):
    co *= len(r[e])

for i in range(len(r)):
    for j in range(len(r[i])):
        summ += r[i][j] * (10 ** (c-1)) * co / len(r[i])
    count *= len(r[i])
    c -= 1

#print(summ, count)
print(float(summ / count))
