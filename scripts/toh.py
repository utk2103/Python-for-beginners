def move(a, b):
    print("Move ", a, "to", b)  # Why: Shows each move

def TowerOfHanoi(n, A, B, C):
    # Why: Recursively solve for n disks
    if n == 1:
        move(A, C)  # Why: Base case, move directly
    else:
        TowerOfHanoi(n-1, A, C, B)  # Why: Move n-1 to spare
        move(A, C)  # Why: Move largest disk
        TowerOfHanoi(n-1, B, A, C)  # Why: Move n-1 on top

n = int(input("Enter the number of disks"))  # Why: User input for problem size
TowerOfHanoi(n, "A", "B", "C")