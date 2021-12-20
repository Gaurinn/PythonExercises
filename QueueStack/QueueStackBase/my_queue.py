from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self, type):
        self.container = None
        self.type = type

        if self.type == "array":
            self.container = ArrayDeque()
        if self.type == "linked":
            self.container = LinkedList()

    def add(self, data):

        if self.type == "array":
            self.container.push_back(data)
        else:
            self.container.push_back(data)

    def remove(self):
        if self.type == "array":
            return self.container.pop_front()
        else:
            return self.container.pop_front()

    def get_size(self):
        if self.type == "array":
            return self.container.get_size()
        else:
            return self.container.get_size()
