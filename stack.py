class Stack:
    def __init__(self, start=[]):
        self.__array = []
        for x in start:
            self.push(x)

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
        return not self.__array

    def get_length(self):
        return len(self.__array)-1


    # overloads
    def __repr__(self):
        return f"Stack: {self.__array}"

    def __eq__(self, other):
        return self.__array == other.__array
    
    def __len__(self):
        return len(self.__array)
    
    def __add__(self, other):
        return Stack(self.__array + other.__array)
    
    def __mul__(self, other):
        return Stack(self.__array * other.__array)
    
    def __getitem__(self, offset):
        return self.__array[offset]
    
    def __getattr__(self, name):
        return getattr(self.__array, name)
    
    #private member
    __array = []


stack = Stack(start=[12, 34, 5, 6, 7])
stack2 = Stack(start=[99, 88, 44])
#stack.push(99)
#stack.push(66)
#stack.push(77)

while not stack.is_empty():
    print(stack.top())
    stack.pop()


print(stack2)

