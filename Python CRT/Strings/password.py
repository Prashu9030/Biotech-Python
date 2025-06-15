Str=input("Enter the String :")
special =0
letter=0
number=0
for ch in Str:
    if ch.isalpha():
        letter+=1
    elif ch.isdigit():
        number+=1
    else:
        special+=1
if letter!=0 and number!=0 and special!=0:
    print("Valid password!")
else:
    print("Invalid password! Please include letters, numbers, and special characters like !@#$%^&*")
    
