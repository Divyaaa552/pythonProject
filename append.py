r = int(input("Enter no of rows"))
c = int(input("Enter no of columns"))
A = []
for i in range(r):
    x = []
    for j in range(c):
        x.append(int(input()))
    A.append(x)
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()
