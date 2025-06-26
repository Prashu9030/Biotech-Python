'''
Merge Sort is a stable, comparison-based sorting algorithm that uses the divide-and-conquer approach.
It divides the input array into two halves, recursively sorts each half, and then merges the sorted halves to produce a fully sorted array.
Unlike Bubble, Selection, or Insertion Sort, Merge Sort is efficient for large datasets but is not in-place.
'''

def mergesort(nlist):
    print("Splitting", nlist)
    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k] = lefthalf[i]
                i += 1
            else:
                nlist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j += 1
            k += 1

        print("Merging", nlist)

nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
mergesort(nlist)
print("Sorted list:", nlist)