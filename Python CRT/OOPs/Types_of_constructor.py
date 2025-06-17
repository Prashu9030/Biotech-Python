#Instance Method Using Parameterized Constructor
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person('kiran',40)
p2=person('Sandeep',42)
print(p1.name,p1.age)
print(p2.name,p2.age)

#Instance Method Without Using Consructor
class person:
    name=''
    age=''
p1=person()
p1.name='kiran'
p1.age='20'
p2=person()
p2.name='Sandeep'
p2.age='22'
print(p1.name,p1.age)
print(p2.name,p2.age)

#Instance Method Using Parameterized Constructor and normal function
class person:
    def __init__(se,name,age):
        se.name=name
        se.age=age
    def printing(self):
        print(self.name,self.age)
    def decide(self): # Checking wheather a person is Major Or Minor
        if self.age>18:
            print("Major")
        else:
            print("Minor")
    def convert(self):  #Uppercase Conversion
        print(self.name.upper())
    def length(self):#Length of Name
        print(len(self.name))

p1=person('kiran',40)
p2=person('Sandeep',18)
print(p1.name,p1.age)
print(p2.name,p2.age)
p1.printing() #calling Function
p2.printing()
p1.decide()
p2.decide()
p1.convert()
p2.convert()
p1.length()
p2.length()
#Non parameterized Constructor
class person:
    c=0
    def __init__(self):
        person.c+=1
p1=person()
print(p1.c)
p2=person()
print(p2.c)
p3=person()
print(p3.c)

#Default Constructor
class student:
    name="Prashu"
    age=20
st=student()
print(st.name,st.age)

#Multiple Constructor
class person:
    def __init__(self):
        print("Iam First Constructor")
    def __init__(self):
        print("Iam Second Constructor")
    def __init__(self):
        print("Iam Third Constructor")
p1=person()
#Functions
class Person:  
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person('Prashu',20)
print(getattr(p1,'name')) #prints(p1.name)
print(getattr(p1,'age')) #prints(p1.age)
setattr(p1,'age',40)
print(getattr(p1,'age'))
print(hasattr(p1,'age'))
print(hasattr(p1,'id'))

