class ArrayDeque():
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.arr = [0] * self.capacity

    def push_back(self, value):
        #resize if deque is full
        if(self.size >= self.capacity):
            resizeArray(self)

        self.arr[self.size] = value
        self.size += 1
        return self.arr

    def push_front(self, value):
        #resize if deque is full
        if(self.size >= self.capacity):
            resizeArray(self)

        counter = self.size
        while counter > 0:
            self.arr[counter] = self.arr[counter - 1]
            counter -= 1

        self.arr[0] = value
        self.size += 1

    def pop_back(self):
        #if deque is empty return None
        if(self.size <= 0):
            return None
        
        returnValue = self.arr[self.size - 1]
        self.size -= 1

        return returnValue

    def pop_front(self):
        #if deque is empty return None
        if(self.size <= 0):
            return None

        returnValue = self.arr[0]

        counter = 0
        while counter < self.size:
            self.arr[counter] = self.arr[counter + 1]
            counter += 1

        self.size -= 1
        return returnValue

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        counter = 0
        while counter < self.size:
            ret_str += str(self.arr[counter]) + " "
            counter += 1
        return ret_str
