def linearSearch(array, n, x):
    # Why: Simple, works on any list (not just sorted)
    for i in range(0, n):
        if (array[i] == x):
            return i  # Why: Return first match
    return -1  # Why: Not found

array = [2, 4, 0, 1, 9]  # Why: Example input
x = 1  # Why: Target to search for
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
