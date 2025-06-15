st=input('name@oraganisation.com :  ')
print(st)
name=''
organisation=''
l=len(st)
lenn=l-4
for i in range(0,len(st)):
    if st[i]=='@':
        name=st[0:i]
        organisation=st[i+1:lenn]
print(f'name is  :', name)
print(f'organisation is :', organisation)
