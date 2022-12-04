import sys
input = sys.stdin.readline

n = int(input())
data = [input().rstrip() for _ in range(n)]


table = [0] * 54
for i in range(n):
    word_list = data[i].split()

    rx = -1
    ry = -1


    for j in range(len(word_list)):
        if table[ord(word_list[j][0].upper()) - 65] == 0:
            rx = j
            ry = 0
            table[ord(word_list[j][0].upper()) - 65] = 1
            break
    #print(word_list, rx, ry)
    if rx == -1:
        for j in range(len(word_list)):
            check = False
            for e in range(1, len(word_list[j])):
                if table[ord(word_list[j][e].upper()) - 65] == 0:
                    rx = j
                    ry = e
                    table[ord(word_list[j][e].upper()) - 65] = 1
                    check = True
                    break
            if check:
                break
    if rx == -1 and ry == -1:
        print(' '.join(word_list))
    else:
        new_word = word_list[rx][:ry] + '[' + word_list[rx][ry] + ']' + word_list[rx][ry + 1:]
        word_list[rx] = new_word
        print(' '.join(word_list))




