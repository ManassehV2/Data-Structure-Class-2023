class Heap:
    def __init__(self):
        self.__lst = []

    def add(self, e):
        self.__lst.append(e)
        curr = len(self.__lst) - 1
        while curr > 0:
            parent = (curr - 1) // 2
            if self.__lst[curr] > self.__lst[parent]:
                self.__lst[curr], self.__lst[parent] = self.__lst[parent], self.__lst[curr]
                curr = parent
            else:
                break

    def remove(self):
        removed = self.__lst[0]
        self.__lst[0] = self.__lst[len(self.__lst) - 1]
        self.__lst.pop()
        current = 0
        while current < len(self.__lst):
            leftChild = (2 * current) + 1
            if leftChild >= len(self.__lst):
                break
            maxChild = leftChild
            rightChild = (2 * current) + 2
            if rightChild < len(self.__lst):
                if self.__lst[leftChild] < self.__lst[rightChild]:
                    maxChild = rightChild

            if self.__lst[current] < self.__lst[maxChild]:
                self.__lst[current], self.__lst[maxChild] = self.__lst[maxChild], self.__lst[current]
                current = maxChild
            else:
                break

        return removed

    def print(self):
        print(self.__lst)

    def getSize(self):
        return len(self.__lst)
