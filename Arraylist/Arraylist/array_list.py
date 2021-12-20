import random

class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = self.capacity * [None] #["A","B","C","D"]
        self.largest = 0
        self.testlist = list()
        self.sorted = True

    #Time complexity: O(n) - linear time in size of list
    def print(self):
        print_str = ""
        for i in range(0,self.size):
            if i < self.size-1:
                newstr = str(self.arr[i]) + ", "
                print_str = print_str + newstr
                newstr = ""
            else:
                newstr = str(self.arr[i])
                print_str= print_str + newstr
                newstr = ""
                
        print(print_str)

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        if isinstance(value, int) and value > self.largest:
            self.largest = value
            self.checkifsorted()

        counter = 0
        newsize = self.size +1
        if self.size+1 < self.capacity:
            while self.size >= counter:
                target = self.arr[self.size]
                self.arr[self.size+1] = target
                self.size += -1              
        else:
            self.resize()
            return self.prepend(value)
        self.size = newsize
        self.arr[0] = value
        
    
    def checkifsorted(self):
        if self.size > 1:
            self.sorted = False
            

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if isinstance(value, int) and value > self.largest:
            self.largest = value
            self.checkifsorted()

        if self.size+1 < self.capacity:
            save = self.size+1
            counter = 0
            if  index > self.size:
                return  
                
            else:
                while self.size-counter != index:
                    self.arr[self.size-counter] = self.arr[self.size-counter-1] 
                    counter += 1   
        else:
            self.resize()
            return self.insert(value,index)
        
        self.arr[index] = value
        self.size = save
        

    #Time complexity: O(1) - constant time
    def append(self, value):
        if isinstance(value, int) and value > self.largest:
            self.largest = value

        if self.size < self.capacity:
            self.arr[self.size] = value
            self.size += 1
        else:
            self.resize()
            return self.append(value)
        self.checkifsorted()

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        new_capacity = self.capacity * 2
        new_arr = new_capacity * [None]
        for i in range(0,self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

        return

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if isinstance(value, int) and value > self.largest:
            self.largest = value
            self.checkifsorted()

        if index > self.capacity-1:
            return
        else:
            if self.arr[index] == None:
                self.arr[index] = value
                self.size += 1
            else:
                self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):  
        if self.size > 0:
            return self.arr[0]
        else:
            raise Empty()
          
    def test_list(self):
        counter = 0
        while counter <= 4:
            number = self.randomint()
            self.append(number)
            self.testlist.append(number)
            counter += 1


    def randomint(self): 
        number = random.randint(0,100) 
        return number     

    #Time complexity: O(1) - constant time
    def get_at(self, index):
 
        if index > self.size-1:
                raise IndexOutOfBounds
        else:
            return self.arr[index]
       
         

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size > 0:
            return self.arr[self.size-1]
        else:
            raise Empty

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index < self.size:
            while self.size-index+1 != 0:
                self.arr[index] = self.arr[index+1]
                index += 1
            self.size += -1
    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def insert_ordered(self, value):
        if not self.sorted:
            self.append(value)
            self.sort()
        else:
            if self.size == 0:
                self.append(value)
                self.sorted = True
            elif value >= self.arr[self.size-1] :
                self.append(value)
            elif value < self.arr[self.size//2]:
                self.insert_ordered_rec(value,0,self.size//2)
            elif value > self.arr[self.size//2]:
                self.insert_ordered_rec(value,self.size//2,self.size-1)



    
    def insert_ordered_rec(self,value,left,right):
        middle = left+(right-left)//2

        if value == self.arr[middle] or middle == left:
            self.insert(value,middle)
        elif value < self.arr[middle]:
            self.insert_ordered_rec(value,left,middle-1)
        elif value > self.arr[middle]:
            self.insert_ordered_rec(value,middle+1,right)
            



    #Time complexity: O(n^2) - quadratic time in size of list
    #Time complexity: O(n log n) - linear times logarythmic time in size of list
    def sort(self):
        self.merge_sort(0,self.size-1)
        self.sorted = True
        
    def merge(self,left,middle,right):
        n1 = middle - left + 1
        n2 = right - middle 

        L = [None] * (n1) 
        R = [None] * (n2) 

        for i in range(0 , n1): 
            L[i] = self.arr[left + i] 
  
        for j in range(0 , n2): 
            R[j] = self.arr[middle + 1 + j] 

        i = 0     # Initial index of first subarray 
        j = 0     # Initial index of second subarray 
        k = left     # Initial index of merged subarray 
    
        while i < n1 and j < n2 : 
            if L[i] <= R[j]: 
                self.arr[k] = L[i] 
                i += 1
            else: 
                self.arr[k] = R[j] 
                j += 1
            k += 1

        while i < n1: 
            self.arr[k] = L[i] 
            i += 1
            k += 1
  
        while j < n2: 
            self.arr[k] = R[j] 
            j += 1
            k += 1


    def merge_sort(self,left,right):
        if left < right:
            middle = (left+right-1)//2
            self.merge_sort(left,middle)
            self.merge_sort(middle+1,right)
            self.merge(left,middle,right)




    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def find(self, value):
        if self.sorted:
            return self.binarysearch(value,0,self.size-1)
        else:
            return self.linearsearch(value)

    def linearsearch(self,value):
        for i in range(0,self.size):
            if value == self.arr[i]:
                return i
        raise NotFound()

    def binarysearch(self,value,left,right):
        if right < left:
            raise NotFound

        middle = left+(right-left)//2

        if self.arr[middle] == value:
            return middle

        if self.arr[middle] < value:
            return self.binarysearch(value,middle+1,right)
        elif self.arr[middle] > value:
            return self.binarysearch(value,left,middle-1)




    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def remove_value(self, value):
        try:
            index = self.find(value)

            for i in range(index + 1, self.size):
                self.arr[i] = self.arr[i + 1]

            self.size -= 1
        except NotFound:
            pass
        

if __name__ == "__main__":

    pass