class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None
        
    def __str__(self) -> str:
        return str(self.value)
    
class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, node):
        if not isinstance(node, Node):
            _node = Node(node)
            
        if self.root is None:
            self.root = _node
        else:
            self._insert(self.root, _node)
            
    def _insert(self, current, node):
        if node.value['salary'] < current.value['salary']:
            # left
            if current.left is None:
                current.left = node
            else:
                self._insert(current.left, node)
        else:
            # rigth
            if current.rigth is None:
                current.rigth = node
            else:
                self._insert(current.rigth, node)
                
    def pre_order(self):
        self._pre_order(self.root)
        
    def _pre_order(self, current):
        """root, left, rigth"""
        if current:
            print(current.value)
            self._pre_order(current.left)
            self._pre_order(current.rigth)
            
    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, current):
        """left, root, rigth"""
        if current:
            self._in_order(current.left)
            print(current.value)
            self._in_order(current.rigth)
            
    def post_order(self):
        return self._post_order(self.root)
    
    def _post_order(self, current):
        """left, rigth, root"""
        if current:
            self._post_order(current.left)
            self._post_order(current.rigth)
            print(current.value)
    
    def search(self, salary):
        return self._search(self.root, salary)
    
    def _search(self, current, salary):
        if current:
            if current.value["salary"] == salary:
                return current.value
            elif salary < current.value["salary"]:
                return self._search(current.left, salary)
            elif salary > current.value["salary"]:
                return self._search(current.rigth, salary)
        return "Value not found in the BST"
    
    def delete(self, salary):
        self._delete(self.root, salary, None, None)
        
    def _delete(self, current, salary, previous, is_left):
        if current:
            if current.value["salary"] == salary:
                if current.left is None and current.rigth is None:
                    if previous:
                        if is_left:
                            previous.left = None
                        else:
                            previous.rigth = None
                    else:
                        self.root = None
                elif current.left is None:
                    if previous:
                        if is_left:
                            previous.left = current.rigth
                        else:
                            previous.rigth = current.rigth
                    else:
                        self.root = current.rigth
                elif current.rigth is None: #One child None (Rigth is None)
                    if previous:
                        if is_left:
                            previous.left = current.left
                        else:
                            previous.rigth = current.left
                    else:
                        self.root = current.left
                else:# Both left and child nodes are not None
                    min_rigth = self.get_min_rigth(current.rigth)
                    current.value = min_rigth.value
                    self._delete(current.rigth, min_rigth.value["salary"], current, False)
                    
            elif salary < current.value["salary"]:
                return self._delete(current.left, salary, current, True)
            elif salary > current.value["salary"]:
                return self.delete(current.rigth, salary, current, False)
    
    def get_min_rigth(self, current):
        if current.left is None:
            return current
        else:
            return self.get_min_rigth(current.left)            
    
myBST = BST()
myBST.insert({
    "name": "Knyaz",
    "salary": 500
})
myBST.insert({
    "name": "Davo",
    "salary": 800
})
myBST.insert({
    "name": "Armen",
    "salary": 550
})
myBST.insert({
    "name": "Varo",
    "salary": 350
})

#myBST.pre_order()
#myBST.in_order()
#myBST.post_order()

myBST.delete(350)
myBST.pre_order()