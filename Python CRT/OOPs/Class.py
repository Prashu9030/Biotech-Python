#Static method
class person:
    age=36
p1=person()
print(p1.age)
p2=person()
print(p2.age)
print(person.age)

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


