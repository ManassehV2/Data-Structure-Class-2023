from Heap import Heap
from Student import Student


class PQueue:
    def __init__(self):
        self.__elements = Heap()

    def poll(self):
        return self.__elements.remove()

    def add(self, e):
        self.__elements.add(e)

    def getSize(self):
        return self.__elements.getSize()


def main():
    pq = PQueue()
    pq.add(Student("Tom", 50, 117))
    pq.add(Student("Joe", 100, 1))
    pq.add(Student("Jonny", 90, 5))
    pq.add(Student("Jerry", 85, 10))

    while pq.getSize() > 0:
        print(pq.poll())


main()
