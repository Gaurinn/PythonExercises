class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")


def palindrome(head):
    
    node = head
    string = ""
    counter = 0
    while node != None:
        string += str(node.data)
        node = node.next
        counter += 1

    return recursiveIsPalindrome(string, 0, counter)

def recursiveIsPalindrome(string, first, last):
    
    if last == 1:
        return True

    if first == last:
        return True

    if string[first] != string[last - 1]:
        return False

    return recursiveIsPalindrome(string, first + 1, last - 1)
    


if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")