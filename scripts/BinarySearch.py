def binarySearch(array, x, low, high):
    # Why: Efficiently search sorted array by dividing in half each time
    while low <= high:
        mid = low + (high - low)//2  # Why: Avoids overflow, finds middle
        if array[mid] == x:
            return mid  # Why: Found target, return index
        elif array[mid] < x:
            low = mid + 1  # Why: Ignore left half
        else:
            high = mid - 1  # Why: Ignore right half
    return -1  # Why: Not found

array = [3, 4, 5, 6, 7, 8, 9]  # Why: Example sorted input
x = 4  # Why: Target to search for
result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
