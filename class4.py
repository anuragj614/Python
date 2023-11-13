# matrix addition
# A=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# B=[[1,0,2],
#    [4,7,1],
#    [9,8,2]]
# result=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]
# for i in range(len(A)):
#     for j in range(len(B)):
#         result[i][j]=A[i][j]+B[i][j]
# print(result)


c = [[1,2,3],
   [4,5,6],
   [7,8,9]]
d = [[1,0,2],
   [4,7,1],
   [9,8,2]]
r = [[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(c)):
    for j in range(len(d[0])):
        for k in range(len(d)):
            r[i][j] = r[i][j] + c[i][k]*d[k][j]
for s in r:
    print(s)
