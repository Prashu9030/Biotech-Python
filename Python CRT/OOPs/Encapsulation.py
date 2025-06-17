class base:
    def __init__(self):
        self.__a=32
        print(self.__a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a+2)
b1=base()
#static Method
class mathematics:
    def addnumbers(x,y):
        return x+y
    
m=staticmethod(mathematics.addnumbers)
print(m(4,55))
print()
# 
class mathematics:
    @staticmethod
    def addnumbers(x,y):
        return x+y
    
print(mathematics.addnumbers(4,55))