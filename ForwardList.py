class Node:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

class ForwardList:
    def __init__(self):
        self.__head = Node()
        self.__size = 0

    def is_empty(self):
        return self.__head == None

    def get_element_count(self):
        return f"Count: {self.__size}" 

    def front(self):
        return self.__head.value

    def clear(self):
        while self.__head.next != None:
            self.__head = self.__head.next
            del self.__head
        self.__size = 0

    def push_front(self,value):
        if self.is_empty():
            self.__head = Node(value)
        else:
            self.__head = Node(value,self.__head)
        
        self.__size += 1

    def pop_front(self):
        if self.__head.next != None:
            tmp = self.__head.next
            del self.__head
            self.__head = tmp

    def insert(self,pos,value):
        #pos.next = Node(value,pos.next)
        if pos == 0:
            self.push_front(value)
        else:
            tmp = self.__head
            for val in range(pos-1):
                tmp = tmp.next
            newNode = Node(value,tmp.next)
            tmp.next = newNode
            self.__size += 1
    
    def show_all(self):
        while self.__head.next != None:
            print(self.__head.value)
            self.__head = self.__head.next
    

    #Private Member
    __head = Node()
    __size = 0


forward = ForwardList()

forward.push_front(99)
forward.push_front(123)
forward.push_front(77)
forward.insert(2,55)

print(forward.is_empty())
print(forward.get_element_count())
forward.show_all()
