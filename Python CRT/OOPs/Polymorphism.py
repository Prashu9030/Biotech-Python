class A:
    def __init__(self,a):
        self.a=a

    #adding two objects
    def __add__(self,o):
        return self.a+o.a
ob1=A(1)
ob2=A(2)
ob3=A("GEEKS")
ob4=A("For")
print(ob3+ob4)