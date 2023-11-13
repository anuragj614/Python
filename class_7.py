mytuple = (1,1,1,1,2,3,"hello","byebye")
for i in mytuple:
    print(i)
# tuple ma pop, insert, delete ,append, modify ni hudaina
mylist = list(mytuple)                    #tuple lai modify garna mildaina so yeslai pahila list ma convert garne
mylist.append("wowo")              
a = mylist
print(a)
tup = tuple(mylist)                       #list bata feri tuple convert and print gareko
print(tup)
print(tup.count(1))
for j in tup:
    print(j)
