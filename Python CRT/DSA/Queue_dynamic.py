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
 
#
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
            print("Queue is empty")
        elif self.front == self.rear:
            x = self.front.data
            self.front = None
            self.rear = None
            print(f"Deleted: {x}")
        else:
            x = self.front.data
            self.front = self.front.next
            print(f"Deleted: {x}")

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Queue elements:", end=' ')
            while temp:
                print(temp.data, end=' ')
                temp = temp.next
            print()

# --------- Menu-driven interface ---------

q1 = lq()

while True:
    print("\nQueue Menu:")
    print("1. Enqueue (Add)")
    print("2. Dequeue (Delete)")
    print("3. Display")
    print("4. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        val = int(input("Enter value to add: "))
        q1.add(val)
    elif ch == 2:
        q1.delete()
    elif ch == 3:
        q1.display()
    elif ch == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
