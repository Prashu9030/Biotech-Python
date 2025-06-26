#Example = 30 50 10 40 20 
''' 
30 50 10 40 20 
0   1  2  3  4
Stage-1
min1=0
x[min1]>x([j]
30>50(0,1)False
30>10(0,2)True
min1=2
x[min1]>x[j]
10>40(2,3)False
10>20(2,4)False
10 50 30 40 20
..........................
stage-2
min1=1
x[min1]<>x[j]
50>30(1,2)True
min1=2
x[min1]<>x[j]
30>40(2,3) False
30>20(2,4)True
min1=4
10 20 30 40 50
......................
'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n): 
        min1 = i # Find the minimum element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min1]:
                min1 = j  # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min1] = arr[min1], arr[i]
    return arr

input_str = input("Enter the numbers That to be Sorted : ")
arr = list(map(int, input_str.strip().split()))
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)