from Student import Student
from ll import LinkedList


class Queue:
    def __init__(self):
        self.__elements = LinkedList()

    def getSize(self):
        return self.__elements.getSize()

    def enqueue(self, e):
        self.__elements.addLast(e)

    def dequeue(self):
        return self.__elements.removeFirst()

    def isEmpty(self):
        return self.getSize() == 0

    def peek(self):
        return self.__elements.head.value


def main():
    q = Queue()
    q.enqueue(Student("Abebe", 97, 3))
    q.enqueue(Student("Challa", 98, 2))
    q.enqueue(Student("Abebech", 100, 1))

    while q.getSize() > 0:
        print(q.dequeue())
    print([1, 2])


main()
