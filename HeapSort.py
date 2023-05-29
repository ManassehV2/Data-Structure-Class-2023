from Heap import Heap


def HeapSort(lst):
    h = Heap()
    for i in range(len(lst)):
        h.add(lst[i])
    for i in range(len(lst)):
        lst[len(lst) - 1 - i] = h.remove()

    return lst


print(HeapSort([4, 1, 3, 2, 0, -1, 7, 10, 9, 20]))
