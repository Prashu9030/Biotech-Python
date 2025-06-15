str=input("Enter the String")
Digit_Count=0
vowel_count=0
SpecialChar=0
for ch in str:
    if ch.isdigit():
        Digit_Count+=1
    elif ch.isalpha():
        if ch in['a','e','i','o','u']:
            vowel_count+=1
    else:
        SpecialChar+=1
print(f"Digit count:{Digit_Count}")
print(f"vowel count:{vowel_count}")
print(f"SpecialChar count:{SpecialChar}")
#String3
str=input("enter the string")
Vowel_lCount=0
Vowel_uCount=0
Consonents_Count=0
for ch in str:
    if ch.isalpha():
        if ch in['a','e','i','o','u']:
            Vowel_lCount+=1
        elif ch in['A','E','I','O','U']:
            Vowel_uCount+=1
        else:
            Consonents_Count+=1
print(f"Vowel lower Count:{Vowel_lCount}")
print(f"Vowel upper Count:{Vowel_uCount}")
print(f"Consonents Count:{Consonents_Count}")
            

    



