#Example : 30 50 10 40 20
'''
s-1
30>50(0,1)False
30>10(0,2)True
10 50 30 40 20
10>40(0,3)False
10>20(0,4)False
n-1 comparision=4
........................
step-2
10 50 30 40 20
50>30(1,2)True
10 30 50 40 20
30>40(1,3)False
30>20(1,4)True
10 20  50 40 30
n-2 comparision=3
.......................
stage-3
10 20  50 40 30
50>40(2,3)True
10 20 40 50 30
40>30(2,4)True
10 20 30 50 40
n-3 Comparision=2
...........................
satge-4
10 20 30 50 40
50>40(3,4)True
10 20 30 40 50
n-4 Comparision=1
........................
Total Comparision=10
'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

input_str = input("Enter the numbers That to be Sorted : ")
arr = list(map(int, input_str.strip().split()))
bubble_sort(arr)
print("Sorted array:", arr)

 