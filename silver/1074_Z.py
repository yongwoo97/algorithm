import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())

#분할정복 문제네
count = -1

def search(x, y, leng):
    global count, result
    if leng <= 2:
        for i in range(2):
            for j in range(2):
                count += 1
                if x+i == r and y+j == c:
                    print(count)
                    exit()
        return
    nn = leng//2

    for i in range(2):
        for j in range(2):
            if x + (i*nn) <= r < x + (i*nn) + nn and y + (j*nn) <= c < y + (j*nn) + nn:
                search(x + (i*nn),y + (j*nn), nn)
            else:
                count += nn ** 2

search(0, 0, 2 ** N)