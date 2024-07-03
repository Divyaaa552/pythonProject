A=[[1,2]
   [2,3]]
B=[[1,2]
   [3,4]]
c=[[0,0]
   [0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            c[i][j]=c[i][j]+A[i][k]*B[k][j]
for i in c:
    print(i)