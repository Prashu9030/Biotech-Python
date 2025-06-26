'''
Quick Sort is an efficient, in-place, comparison-based sorting algorithm that uses the divide-and-conquer approach.
 It selects a pivot element,partitions the array around the pivot (elements smaller than the pivot go to its left, 
 larger to its right), and recursively sorts the sub-arrays.
 Quick Sort is widely used due to its average-case efficiency, 
 though its worst-case performance depends on pivot selection.
'''
def qs(arr):
    global a
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print(pivot, a)
    a += 1
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return qs(left) + middle + qs(right)

a = 1
n = int(input("Enter number of elements: "))
x = list(map(int, input("Enter elements separated by space: ").split()))
print("Input list:", x)
ans = qs(x)
print("Sorted list:", ans)