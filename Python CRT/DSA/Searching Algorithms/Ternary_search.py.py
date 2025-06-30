# Ternary Search
#terinary search

n = int(input("Enter number of elements: "))
x = list(map(int, input("Enter elements: ").split()))
x.sort()
print("Sorted list:", x)
key = int(input("Enter key to search: "))
l = 0
r = n - 1
flag = 0
while l <= r:
    print("Searching in:", l, "to", r)    
    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3  
    print("Midpoints:", mid1, mid2)
    if x[mid1] == key:
        flag = 1
        print("Found at index", mid1)
        break
    elif x[mid2] == key:
        flag = 1
        print("Found at index", mid2)
        break
    elif key < x[mid1]:
        r = mid1 - 1
    elif key > x[mid2]:
        l = mid2 + 1
    else:
        l = mid1 + 1
        r = mid2 - 1

if flag == 0:
    print("Data not found")