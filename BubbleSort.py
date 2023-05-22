def BubbleSort(lst):
    for j in range(len(lst)):
        for i in range(len(lst) - 1 - j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def main():
    print(BubbleSort([8, 2, 4, 1, 3]))


main()
