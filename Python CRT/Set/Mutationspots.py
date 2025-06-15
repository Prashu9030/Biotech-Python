#input:
#seq1="AAGCTCGA"
#seq2="AACCTAGA"
#output:[2, 6]
n=int(input('enter the length of DNA strings:'))
str1=input('enter first sequencs:').upper()
str2=input('enter second sequence:').upper()

mutation=[]
if (len(str1)==len(str2)):
    for i in range (n):
        if (str1[i]!=str2[i]):
            mutation.append(i)
    print(mutation)
else:
    print("DNA strategies should be same size")