sample_prefix=int(input("Enter the sample prefix:"))
sample_format=""
n=int(input("enter th number of samples ypu want to generate::"))
list=[]
for i in range(0,n):
    sample_format=(f"LAB2025-0{sample_prefix+1}")
    list.append(sample_format)
    sample_prefix+=1
print(list)

