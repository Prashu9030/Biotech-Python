Str=input("Enter the String :")
upperv=0
lowerv=0
upperc=0
lowerc=0
for ch in Str:
    if(ch.isalpha() and ch.islower()):
            if ch in 'aeiou':
                lowerv+=1
            else:
                lowerc+=1
    elif(ch.isalpha() and ch.isupper()):
            if ch in 'AEIOU':
                upperv+=1
            else:
                upperc+=1
print(f"Uppercase vowels count: {upperv}")
print(f"Lowercase vowels count: {lowerv}")
print(f"Uppercase consonants count: {upperc}")
print(f"Lowercase consonants count: {lowerc}")