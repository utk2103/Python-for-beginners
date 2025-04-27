def mergeSort(array):
    # Why: Recursively splits and sorts, then merges
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]  # Why: Left half
        M = array[r:]  # Why: Right half
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        # Why: Merge sorted halves
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]  # Why: Example unsorted list
    mergeSort(array)
    print("Sorted array is: ")
    printList(array)
