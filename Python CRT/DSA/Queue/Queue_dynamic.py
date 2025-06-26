class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class lq:
    def __init__(self):
        self.front = None
        self.rear = None  

    def add(self, newdata):
        newnode = node(newdata)
        if self.front is None:
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def delete(self):
        if self.front is None:
            print("empty")
        elif self.front == self.rear:
            x = self.front.data
            self.front = None
            self.rear = None
            return x
        else:
            x = self.front.data
            self.front = self.front.next
            return x  

    def display(self):
        if self.front is None:
            print("empty")
        else:  # Move the display logic into the proper else block
            temp = self.front
            while temp:
                print(temp.data, end=' ')
                temp = temp.next
            print()

# Testing
q1 = lq()
q1.add(10)
q1.add(20)
q1.display()    # Output: 10 20
q1.delete()     # Deletes 10
q1.display()    # Output: 20
 
