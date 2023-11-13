mystring="Hello world from new python script"
# for i in mystring:
#     # print(i)      loop in string
#     if i=="l":
#         i= i.upper()
#     print(i)
    
print(mystring.strip())    

a = "You are heisenberg"
b = f"say my name {a}"
print(b)
c = "mero nam {0} ho {1}, {2}, {3}".format(a,mystring,"helllo", "world")
print(c)

d = f"my name {a} {mystring}"
print(d)

mystring2 = mystring.replace("w","B")           #every w in mystring is replaced by B
print(mystring)
mystring3 = mystring.replace("Hello","Bye-bye")           
print(mystring)

print(mystring.count("o"))

mystring1 = "aaabcdefaaaabababababaababaabaabbba"
print(mystring1.count("a"))
print(mystring1.count("ab"))
print(mystring1.count("ba"))    

mylist = mystring.split(" ")
# print(mylist)
for index, item in enumerate(mylist):
    if index % 2 == 0:
        mylist[index] = item.upper()
print(mylist)
# print(index,item)
# for item in mylist:
#     print(item)

b=[item.upper() for item in mylist if mylist.index(item) % 2 == 0]        #advanced python decorator haru pani advanced python
print(b)

