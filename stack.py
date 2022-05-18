class Stack:
    def __init__(self):
        pass

    def push(self,value):
        self.__array.append(value)

    def pop(self):
        self.__array.pop()

    def top(self):
        return self.__array[-1]

    def front(self):
        return self.__array[0]

    def clear(self):
        self.__array.clear()

    def is_empty(self):
        return not self.get_length()

    def get_length(self):
        return len(self.__array)-1


    #private member
    __array = []


stack = Stack()
stack.push(99)
stack.push(66)
stack.push(77)

while not stack.is_empty():
    print(stack.top())
    stack.pop()

