def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found
arr = list(map(int,input("Enter the Numbers :").split()))
target = int(input("Enter the target Number :"))
result = linear_search(arr, target)
print(f"Element {target} found at index: {result}")