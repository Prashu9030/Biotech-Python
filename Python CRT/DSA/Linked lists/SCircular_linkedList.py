class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class SCLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        if self.headval is None:
            print("List is empty")
            return

        printval = self.headval
        while True:
            print(printval.dataval, end=" ")
            printval = printval.nextval
            if printval == self.headval:
                break
        print()

    def atbeginning(self, newdata):
        newnode = Node(newdata)
        if self.headval is None:
            newnode.nextval = newnode
            self.headval = newnode
        else:
            temp = self.headval
            while temp.nextval != self.headval:
                temp = temp.nextval
            newnode.nextval = self.headval
            temp.nextval = newnode
            self.headval = newnode

    def atend(self, newdata):
        newnode = Node(newdata)
        if self.headval is None:
            newnode.nextval = newnode
            self.headval = newnode
        else:
            temp = self.headval
            while temp.nextval != self.headval:
                temp = temp.nextval
            temp.nextval = newnode
            newnode.nextval = self.headval

    def inbetween(self, middle, newdata):
        newnode = Node(newdata)
        temp = self.headval
        if temp is None:
            print("List is empty")
            return
        while temp.dataval != middle and temp.nextval != self.headval:
            temp = temp.nextval
        if temp.dataval == middle:
            newnode.nextval = temp.nextval
            temp.nextval = newnode
        else:
            print("Middle node not found")

    def removenode(self, removekey):
        if self.headval is None:
            print("List is empty")
            return

        temp = self.headval
        prev = None

        while True:
            if temp.dataval == removekey:
                if prev is None:  # deleting head
                    if temp.nextval == self.headval:
                        self.headval = None  # only one node
                    else:
                        last = self.headval
                        while last.nextval != self.headval:
                            last = last.nextval
                        self.headval = temp.nextval
                        last.nextval = self.headval
                else:
                    prev.nextval = temp.nextval
                return
            prev = temp
            temp = temp.nextval
            if temp == self.headval:
                break
        print("Data not found")

# Testing
list1 = SCLinkedList()
list1.atbeginning("mon")
list1.atbeginning("sun")
list1.listprint()
list1.atend("thu")
list1.listprint()
list1.inbetween("mon", "tue")
list1.listprint()
list1.removenode("fri")  # Not present
list1.listprint()