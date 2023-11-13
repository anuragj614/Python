# loops in list
mylist = ["hello",2,3,4,"hi",6,7,8,9,"byebye"]
sum = 0
for element in mylist:
    if type(element)==int:
        sum += element
        print(sum)
mylist = ["hello",2,3,4,"hi",6,7,8,9,"byebye"]
mylist1 = mylist[2:5:2]
print(mylist1)
print(mylist[1:8:3],mylist[2:6:2])
        
print(mylist[::-1])
print(mylist[-2:7:1])
print(mylist[-1:0:-1])
print(mylist[-1:-5:-2])

# list in list 
mat_A = [[1,2,3],[4,5,6],[7,8,9]]
print(mat_A[1])
print(mat_A[1][-2])





    