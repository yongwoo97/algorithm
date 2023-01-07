n = int(input())

import math
def judge(x):

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True:
    check = False
    if n == 1:
        n += 1
    if judge(n):
        string = str(n)
      #  mid = (len(string) - 1) // 2

        r_string = string[::-1]
        if string == r_string:
            print(string)
            break
        else:
            n+=1
    else:
        n += 1

