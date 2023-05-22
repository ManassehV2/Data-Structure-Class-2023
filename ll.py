class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printNodes(self):
        if self.head == None:
            return None
        curr = self.head
        while curr != None:
            print(curr.value, end=' -> ')
            curr = curr.next
        print("null")

    def addFirst(self, e):
        newNode = Node(e)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    def addLast(self, e):
        newNode = Node(e)
        if self.tail == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def removeLast(self):
        if self.head == None:
            return None
        elif self.size == 1:
            self.head = self.tail = None
            self.size -= 1
        else:
            curr = self.head
            for i in range(self.size - 2):
                curr = curr.next
            curr.next = None
            self.tail = curr
            self.size -= 1

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


ll = LinkedList()
ll.addFirst('e')
ll.addFirst('d')
ll.addFirst('c')
ll.addFirst('b')
ll.printNodes()
ll.addFirst('a')
ll.printNodes()
ll.addLast('f')
ll.printNodes()
ll.removeLast()
ll.printNodes()
