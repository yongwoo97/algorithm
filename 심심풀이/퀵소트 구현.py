
def quicksort(data):

    def _quicksort(data, i, j):
        if i >= j:
            return
        part = partition(data, i, j)
        _quicksort(data, i, part)
        _quicksort(data, part+1, j)


    def partition(data, i, j):
        pivot = j
        while i <= j:
            while data[i] < data[pivot]:
                i += 1
            while data[pivot] < data[j]:
                j -= 1

            if i >= j:
                return j

            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
        return j

    _quicksort(data, 0, len(data)-1)
    return data
a = [1, 1, 3, 2, 3]
print(quicksort(a))
print(a)

