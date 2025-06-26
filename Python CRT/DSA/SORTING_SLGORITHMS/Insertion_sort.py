'''
INSERTION SORT
1.Every iteration moves an element from unsorted to sortedd portion until all the elements are sorted in list
2.It is similar to cards in order
'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted
        j = i - 1     # Index of the last element in sorted portion
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place key in its correct position
    return arr


input_str = input("Enter the numbers That to be Sorted : ")
arr = list(map(int, input_str.strip().split()))
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)