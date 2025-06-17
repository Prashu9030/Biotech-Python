# Multilevel
class grandfather():
    def show(self):
        print("This is Grandfather Class")
class father(grandfather):
    def show1(self):
        print("This is Father class")
class son(father):
    def show2(self):
        print("This is son class")
s1=son()
s1.show()
s1.show1()
s1.show2()
print()
# Multiple Inheritence
class dance:
    def dancing(self):
        print("I can Dance")
class fly:
    def flying(self):
        print("I can also fly ")
class peacock(dance,fly):
    def sound(self):
        print("I had a good sound too")
p1=peacock()
p1.dancing()
p1.flying()
p1.sound()
print()

#Hirarchial Inheritance
class shape:
    def area(self):
        print("Calculate area :")
class circle(shape):
    def circlearea(self,radius):
        print("Area of Circle",3.14*radius*radius)
class square(shape):
    def squarearea(self,side):
        print("Area of Square=",side*side)
c1=circle()
c1.area()
c1.circlearea(5)
s1=square()
s1.area()
s1.squarearea(5)