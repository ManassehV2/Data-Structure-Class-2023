def QS(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst.pop()
    leftHalf = []
    rightHalf = []
    for e in lst:
        if e <= pivot:
            leftHalf.append(e)
        else:
            rightHalf.append(e)
    return QS(leftHalf) + [pivot] + QS(rightHalf)


def main():
    print(QS([8, 2, 4, 1, 3]))


main()
