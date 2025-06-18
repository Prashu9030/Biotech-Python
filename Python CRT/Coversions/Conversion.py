#Binary
n=int(input("Enter the integer to Convert :"))
x=bin(n)
print(x)
print(type(x))
print(x)
dec=int(x,2)
print(dec)
print()

#Octadecimal 
x=oct(n)
print(x)
print(type(x))
print(x)
dec=int(x,8)
print(dec)
print()

#Hexadecimal
x=hex(n)
print(x)
print(type(x))
print(x)
dec=int(x,16)
print(dec)