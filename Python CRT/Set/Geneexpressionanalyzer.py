size=int(input("Enter the data:"))
underexpressed=0
normal=0
overexpressed=0
list=[]
output = []
for i in range(size):
    gene=float(input("Enter the value:"))
    list.append(gene)       
    if(gene<5):
        output.append("Underexpressed")
    elif(gene>=5 and gene<=15):
        output.append("Normal")
    else:
        output.append("Overexpressed")
print("Gene values:",list)
print(output)