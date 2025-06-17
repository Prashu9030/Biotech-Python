#Example
class student:
    def __init__(self,name,rno,mat,phy,che):
        self.name=name
        self.rno=rno
        self.mat=mat
        self.phy=phy
        self.che=che
    def calculation(self):
        if(self.mat>=40 and self.phy>=40 and self.che>=40):
            tot=self.mat+self.phy+self.che
            avg=tot/3
            print(tot)
            print("%.2f"%avg)
            if(self.mat>=40 and self.phy>=75) or (self.che>=75 and self.phy>=75) or (self.che>=75 and self.mat>=75):
                print("Admission is Confirmed")
            else:
                print("Admission is not Confirmed")
        else:
            print("Fail")
s1=student("Kiran",501,74,85,85)
s1.calculation()
print()

#Example 2
class Customer:
    def __init__(self,name,item1,item2,item3):
        self.name=name
        self.item1=item1
        self.item2=item2
        self.item3=item3
    def calculation(self):
        print(self.name)
        tot=(self.item1+self.item2+self.item3)
        print(tot)
        if(tot>200):
            total=tot-tot*(20/100)
            print(total)
        else:
            print(tot)
c1=Customer("Prashu",80,26,800)
c1.calculation()
print()

#Method 2
class store:
    def __init__(self,name,noofitems):
        self.name=name
        self.noofitems=noofitems
    def calculation(self):
        x=self.noofitems
        tp=0
        for i in range(x):
            p=int(input())
            tp+=p
        return tp
name=input("Enter the Name:")
noofitems=int(input("Enter the No of Items:"))
c1=store(name,noofitems)
tp=c1.calculation()
print("Total:",tp)
if(tp>=200):
    print("After Discount",tp-tp*0.2)
else:
    print(tp)