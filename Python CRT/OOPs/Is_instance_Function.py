class Calculation1:
    def Summation(self,a,b):
        return a+b
class Calculation2:
    def Multiplication(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b
d=Derived()
print(isinstance(Derived,Calculation1))
print(isinstance(Derived,Calculation2))
print(isinstance(Calculation1,Calculation2)) 
