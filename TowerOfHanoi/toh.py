def move(a,b):
    print("Move ",a, "to", b)
def TowerOfHanoi(n,A,B,C):
    if n==1:
        move(A,C)
    else:
        TowerOfHanoi(n-1,A,C,B)
        move(A,C)
        TowerOfHanoi(n-1,B,A,C)
        #input for number of disks you want 
n = int(input("Enter the number of disks"))
TowerOfHanoi(n,"A","B","C")
        