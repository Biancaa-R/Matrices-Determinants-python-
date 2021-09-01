#project to add 2 matrices

A=[[1,2,3],
[4,5,6],                  
[7,8,9]]

B=[[5,4,3],
[3,4,5],
[6,7,8]]

result=[[0,0,0],
[0,0,0],
[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]

for i in result:
    print(i)

'''
 output:
 [6, 6, 6]
[7, 9, 11]
[13, 15, 17]

'''
