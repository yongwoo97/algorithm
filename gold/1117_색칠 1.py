w, h, f, c, x1, y1, x2, y2 = map(int, input().split())

def result():
    global w, h, f, c, x1, y1, x2, y2

    if min(w-f, f)-x1 >= 0:
        if min(w-f, f)-x2 > 0:
            return w * h - (2 * (x2-x1) * (y2-y1) * (c + 1))
        else:
            left = 2 * (min(w-f, f)-x1) * (y2-y1) * (c + 1)
            right = (x2-min(w-f, f)) * (y2-y1) * (c+1)
            return w * h - left - right
    else:
        return w * h - ((x2-x1) * (y2-y1) * (c+1))
print(result())
