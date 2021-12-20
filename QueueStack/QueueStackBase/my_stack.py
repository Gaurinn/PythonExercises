from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self, type):
        self.container = None
        self.type = type

        if self.type == "array":
            self.container = ArrayDeque()
        if self.type == "linked":
            self.container = LinkedList()

    def push(self, data):

        if self.type == "array":
            self.container.push_back(data)
        else:
            self.container.push_front(data)

    def pop(self):
        if self.type == "array":
            return self.container.pop_back()
        else:
            return self.container.pop_front()

    def get_size(self):
        if self.type == "array":
            return self.container.get_size()
        else:
            return self.container.get_size()