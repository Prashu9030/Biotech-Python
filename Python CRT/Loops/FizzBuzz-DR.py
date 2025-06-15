z=int(input())
if(z%3==0 and z%5==0):
    print("FizzBuzz")
if(z%3==0 and z%5!=0):
    print("Fizz")
if(z%3!=0 and z%5==0):
    print("Buzz")
if(z%3!=0 and z%5!=0):
    print("BuzzFizz")
