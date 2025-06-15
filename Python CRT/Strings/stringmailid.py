st=input("enter mail Id :")
name=''
organization=''
l=len(st)
lenn=l-4
for i in range(0,len(st)):
    if st[i]=='@':
        name=st[0:i]
        organization=st[i+1:lenn]
print(f'name is',name)
print(f'organisation is',organization)
