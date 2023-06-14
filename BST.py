from Queue import Queue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def getsize(self):
        return self.__size

    def idempty(self):
        return self.__size == 0

    def getroot(self):
        return self.__root

    def add(self, val):
        if self.__root == None:
            self.__root = TreeNode(val)
            self.__size += 1
            return True

        curr = self.__root
        parent = None
        while curr != None:
            parent = curr
            if curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
            else:
                return False

        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        self.__size += 1
        return True

    def preorder(self, node):
        if node == None:
            return None
        print(node.val, end=", ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node == None:
            return None
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end=", ")

    def inorder(self, node):
        if node == None:
            return None
        self.inorder(node.left)
        print(node.val, end=", ")
        self.inorder(node.right)

    def levelorder(self, node):
        q = Queue()
        q.enqueue(node)
        while not q.isEmpty():
            n = q.dequeue()
            print(n.val, end=", ")
            if n.left:
                q.enqueue(n.left)
            if n.right:
                q.enqueue(n.right)


def main():
    tree = BST()
    tree.add(7)
    tree.add(20)
    tree.add(5)
    tree.add(15)
    tree.add(10)
    tree.add(4)
    tree.add(4)
    tree.add(33)
    tree.add(2)
    tree.add(25)
    tree.add(6)

    tree.levelorder(tree.getroot())


main()
