#Single Level Inheritence Method 1
class Father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class son(Father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)
x=Father('nagarjuna')
x.show()
y=son('akhil')
y.show1()
y.show()
##Single Level Inheritence Method 2
class base:
    def __init__(self):
        self._a=32
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a+2)
x=base()
y=derived()
print(x._a)
print(y._a)

#Multilevel Inheritence
class base:
    def __init__(self):
        self._a=42
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a+2)
class derived1(derived):
    def __init__(self):
        derived.__init__(self)
        print(self._a*2)
x=derived1()

#Multiple Iheritence
class Father:
    fathername=''
    def Father(self):
        print(self.fathername)
class Mother:
    mothername=''
    def Mother(self):
        print(self.mothername)
class Son1(Father,Mother):
    son1name=''
    def Son1(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)
s1=Son1()
s1.son1name="Ram"
s1.fathername="Shiva"
s1.mothername="Pavani"
s1.Son1()

#Hirarchial Inheritance
class Son1(Father,Mother):
    son1name=''
    def Son1(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)
class Son2(Father):
    son2name=''
    def Son2(self):
        print(self.fathername)
        print(self.son2name)
s1=Son1()
s1.son1name="Ram"
s1.fathername="Shiva"
s1.mothername="Pavani"
#s1.Son1()
s2=Son2()
s2.son2name="Lava"
s2.fathername="Shiva"
#s2.Son2()
s1.Father()
s1.Mother()
s2.Father()
