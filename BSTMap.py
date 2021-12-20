#BSTMap
#andri saemundsson andri09@ru.is
class ItemExistsException():
    pass
class NotFoundException():
    pass

class BSTNode:
    def __init__(self, key = None, data = None, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BSTMap:
    def __init__(self, root = None, size = 0):
        self.root = root
        self.size = 0

    def contains(self, key):
        if(self.root == None):
            return False
        node = self.root
        return self._containsRecursive_(key, node)

    def _containsRecursive_(self, key, node):
        if(node == None):
            return False
        if(key == node.key):
            return True
        if(key < node.key):
            return self._containsRecursive_(key, node.left)
        if(key > node.key):
            return self._containsRecursive_(key, node.right)

    def insert(self, key, data):
        if(self.contains(key)):
            return ItemExistsException()
        self.root = self._insert_recursive_(key, data, self.root)

    def _insert_recursive_(self, key, data, node):
        if(node == None):
            self.size = self.size + 1
            return BSTNode(key, data)
        elif(key < node.key):
            node.left = self._insert_recursive_(key, data, node.left)
        elif(node.key < key):
            node.right = self._insert_recursive_(key, data, node.right)
        return node     

    def __str__(self):
        ret_str = ""
        return self._print_in_order_recursive_(self.root, ret_str)

    def _print_in_order_recursive_(self, node, ret_str):  
        if(node == None):
            return ret_str
        ret_str = self._print_in_order_recursive_(node.left, ret_str)
        ret_str = ret_str + "{" + str(node.key) + ":" + str(node.data) + "} "
        ret_str = self._print_in_order_recursive_(node.right, ret_str)
        return ret_str
    
    def update(self, key, data):
        if(self.contains(key) == False):
            return NotFoundException()
        self.root = self._update_recursive_(key, data, self.root)

    def _update_recursive_(self, key, data, node):
        if(node == None):
            return None
        elif(key < node.key):
            node.left = self._update_recursive_(key, data, node.left)
        elif(node.key < key):
            node.right = self._update_recursive_(key, data, node.right)
        else:
            node.data = data
        return node

    def find(self, key):
        if(self.contains(key) == False):
            return NotFoundException()
        return self._find_recursive_(key, self.root)

    def _find_recursive_(self, key, node):
        if(node == None):
            return None
        elif(key < node.key):
            node.left = self._find_recursive_(key, node.left)
        elif(node.key < key):
            node.right = self._find_recursive_(key, node.right)
        else:
            return node.data   

    def remove(self, key):  
        if(self.contains(key) == False):
            return NotFoundException()
        self.size -= 1
        self.root = self._remove_recursive_(key, self.root)

    def _remove_recursive_(self, key, node):
        if(node == None):
            return None
        elif(key < node.key):
            node.left = self._remove_recursive_(key, node.left)
        elif(node.key < key):
            node.right = self._remove_recursive_(key, node.right)
        else:#if key == node.key
            return self._remove_node_(node)
        return node

    def _remove_node_(self, node):
        if(node.left == None and node.right == None):   #if node has no children
            return node
        elif(node.right == None):                       #if node has no right child, but at least one left child
            return node.left
        elif(node.left == None):                        #if node has no left child, but at least one right child
            return node.right
        else:                                           #if node has a left and a right childe
            node = self._swap_and_remove_leftMost_(node)
        return node
    
    def _swap_and_remove_leftMost_(self, node):
        originalNode = node
        if(node.right.left == None):                    
            node.right.left = originalNode.left
            return node.right      
        parent = node.right
        delNode = node.right
        while(delNode.left != None):
            parent = delNode
            delNode = delNode.left
        originalNode.data = delNode.data
        if(delNode.right != None):
            parent.left = delNode.right
        else:
            parent.left = None
        return originalNode

    def __len__(self):
        return self.size

    def __setitem__(self, key, data):
        if(self.contains(key)):
            self.update(key, data)
        else:
            self.insert(key, data)

d = {}
d[1] = 'asdf'
print(d[1])
b = BSTMap()
b[5] = "fimma"
b[3] = "thir"
print(b.root.left.data)