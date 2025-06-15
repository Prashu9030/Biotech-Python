def Hello():
    print("Hello world")
Hello()
print(Hello())

def display(a):
    print("a:",a())
def demo():
    print("Hey.....!I'm a demo function...!")
display(demo)

def disp():
            def show():
                  return "show function"
            print("disp funtion")
            return show
r_s=disp()
print(r_s())

def Print(a,b):
      print(f"a :",a)
      print(f"b :",b)
Print(10,20)