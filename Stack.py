class Stack:
    def __init__(self):
        self.__elements = []

    def pop(self):
        if len(self.__elements) == 0:
            return None
        return self.__elements.pop()

    def push(self, e):
        self.__elements.append(e)

    def isEmpty(self):
        return len(self.__elements) == 0


def isValid(s):
    myStack = Stack()
    dic = {'{': '}', '[': ']', '(': ')'}
    if len(s) % 2 != 0:
        return False
    for i in s:
        if i in dic.keys():
            myStack.push(i)
        else:
            if myStack.isEmpty():
                return False
            temp = myStack.pop()
            if i != dic[temp]:
                return False

    return myStack.isEmpty()


print(isValid("[]{}({})"))
