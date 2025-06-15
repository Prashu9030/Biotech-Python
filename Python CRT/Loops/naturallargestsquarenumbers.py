#Natural numbers
n=int(input("Enter the input:"))
i=1
while(i<=n):
    print(i)
    i+=1
#Squares of the number
n=int(input("Enter the input:"))
i=1
while(i<=n):
    print(i**2)
    i+=1
#Largest number
n=int(input("Enter the input:"))
list=[]
for i in range(n):
    num=int(input("Enter the number:"))
    list.append(num)
large_num=list[0]
for j in list:
    if j>large_num:
        large_num=j
print("The largest number in the list is:",large_num )
