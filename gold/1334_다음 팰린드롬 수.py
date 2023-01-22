n = int(input())
n += 1
#print(n)
ns = str(n)
#print(len(ns))
if len(ns) < 2:
    print(ns)


elif len(ns) % 2 == 1:
    mid = len(ns) // 2
    left = int(ns[:mid][::-1])
    right = int(ns[mid+1:])

    if left >= right:
        print(ns[:mid] + ns[mid] + ns[:mid][::-1])
    else:
        new_ns = str(int(ns[:mid+1]) + 1)
        tail = new_ns[:-1][::-1]
        print(new_ns + tail)

elif len(ns) % 2 == 0:
    mid = len(ns) // 2
    left = int(ns[:mid][::-1])
    right = int(ns[mid:])

    if left >= right:
        print(ns[:mid] + ns[:mid][::-1])
    else:
        new_left = str(int(ns[:mid]) + 1)
        print(new_left + new_left[::-1])