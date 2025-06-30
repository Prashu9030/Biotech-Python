'''
Binary Search works on sorted arrays by repeatedly dividing the search space in half. 
It compares the target with the middle element and eliminates half of the remaining elements.
'''
n=int(input())
x=list(map(int,input().split(' ',n-1)))
print(x)
x.sort()
print(x)
key=int(input())
low=0
high=n-1
while low<=high:
  mid=(low+high)//2
  if x[mid]==key:
    print(mid)
    flag=1
    break
  elif x[mid]<key:
    low=mid+1
  else:
    high=mid-1
else:
  print("data not present")