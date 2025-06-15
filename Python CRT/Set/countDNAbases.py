# input="ATGCGATAAGCTTTAA"
# output={'A':5,'T':4,'G':2,'C':2}
set=input("Enter the Bases :").upper()
a=0
t=0
c=0
g=0
for  i in range(len(set)):
    if set[i] == 'A':
        a+= 1
    elif set[i] == 'T':
        t+= 1
    elif set[i] == 'C':
        c+= 1
    elif set[i] == 'G':
        g+=1 
o={'A':a,'T':t,'C':c,'G':g}
print(o)