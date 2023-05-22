from Heap import Heap


def HeapSort(lst):
    h = Heap()
    for i in range(len(lst)):
        h.add(lst[i])
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = h.remove()

    return lst


print(HeapSort([8, 2, 4, 1, 3]))
