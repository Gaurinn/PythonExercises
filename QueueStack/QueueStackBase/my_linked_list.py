class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop_front(self):
        if self.head == None:
            return None
        ret_val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return ret_val

    def get_size(self):
        return self.size
            
    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str