#write a program to find the gcd of the given two numbers using recursion

import math
print(math.gcd(5,12))
print(math.lcm(5,12))
print()

#Non-recursive program
a,b=map(int,input().split())
while a!=b:
    print(a,b)
    if a>b:
        a=a-b
    else:
        b=b-a
print(f"GCD of the two numbers is:{a}")

#RECURSIVE PROGRAM

def rgcd(a, b):
    if a == b:
        return a
    if a < b:
        return rgcd(a, b - a)  # recursive call when a < b
    else:
        return rgcd(a - b, b)  # recursive call when a > b

a, b = map(int, input().split())
ans = rgcd(a, b)
print(ans)