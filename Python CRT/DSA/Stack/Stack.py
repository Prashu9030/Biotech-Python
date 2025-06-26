class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """
    A Stack implementation using a singly linked list.
    Attributes:
        top (Node): The top node of the stack.
    Methods:
        push(newdata):
            Pushes a new element with the given data onto the top of the stack.
        pop():
            Removes and returns the data from the top element of the stack.
            Prints "empty" and returns None if the stack is empty.
        display():
            Prints all elements in the stack from top to bottom.
            Prints "empty" if the stack is empty.
    """
    def __init__(self):
        self.top = None

    def push(self, newdata):
        newnode = Node(newdata)  # Capital N
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if self.top is None:
            print("empty")
            return None
        else:
            x = self.top.data
            self.top = self.top.next
            return x

    def display(self):
        if self.top is None:
            print("empty")
        else:
            temp = self.top
            while temp:
                print(temp.data, end=' ')
                temp = temp.next
            print()  

# Usage
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)

s1.display()  
s1.pop()
s1.display()  
s1.pop()
s1.display()  
s1.pop()
s1.display()

