def MergeSort(lst):
    size = len(lst)
    if size == 1:
        return lst
    mid = size // 2
    leftHalf = MergeSort(lst[:mid])
    rightHalf = MergeSort(lst[mid:])

    return Merge(leftHalf, rightHalf)


def Merge(lst1, lst2):
    result = []
    inx1 = 0
    inx2 = 0
    while inx1 < len(lst1) and inx2 < len(lst2):
        if lst1[inx1] < lst2[inx2]:
            result.append(lst1[inx1])
            inx1 += 1
        else:
            result.append(lst2[inx2])
            inx2 += 1

    while inx1 < len(lst1):
        result.append(lst1[inx1])
        inx1 += 1
    while inx2 < len(lst2):
        result.append(lst2[inx2])
        inx2 += 1

    return result


def main():
    print(MergeSort([4, 1, 3, 2, 0, -1, 7, 10, 9, 20]))


main()
