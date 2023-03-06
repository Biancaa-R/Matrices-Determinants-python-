mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
r=len(mat)
c=len(mat[0])
k=mat[0][0]

for i in range(0,r-1):
    mat[i][0]=mat[i+1][0]
for j in range(0,c-1):
    mat[r-1][j]=mat[r-1][j+1]
for i in range(r-1,0,-1):
    mat[i][c-1]=mat[i-1][c-1]
for i in range(c-1,0,-1):
    mat[0][i]=mat[0][i-1]
mat[0][1]=k
for i in mat:
    print(i)
