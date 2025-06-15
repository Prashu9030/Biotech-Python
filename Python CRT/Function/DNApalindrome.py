def Palindrome(s):
    s=s.replace("A","T")
    s=s.replace("C","G")
    s=s.replace("T","A")
    s=s.replace("G","C")
    return "Given DNA sequence is a palindrome" if s == s[::-1] else "Given DNA sequence is not a palindrome"
res=Palindrome(s=input("ENter the DNA sequence: ").upper())
print(res)