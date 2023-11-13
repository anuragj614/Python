mylist = [1,2,3,4,5,6,7,8,9,10]      #tuple lai ni milxa
print(mylist)

nextlist = mylist[::-1]               #if tuple xa bhane nextlist= list(mylist[::-1]) hunxa

print("Ulto list is:")
print(nextlist)

def sum_of_num(a,b):
    return a+b

print(sum_of_num(1,2))
sum = map(sum_of_num, mylist, nextlist)         #map ma function pathaune ani add garnu parne variables pathaune 

print("Sum of ulto ra sulto list is:")
print(list(sum))

# newlist = []
# for index in range(len(mylist)):
#     newlist.append()
#     print(index)


my_list = (1,2,3,4,5,6,7,8,9,10)
next_list = list(my_list[::-1])
jpt_list = tuple(zip(my_list, next_list))       #zip le 2ota list lai euta ma rakhxa
lis = [11, 11, 11, 11, 11, 11, 11, 11, 11]
jpt_list = list(zip(my_list, next_list, lis))
print(jpt_list)
print(next_list)

def sum_of_num(a,b,c):
    return a+b+c

print(sum_of_num(1,2,3))
sum = map(sum_of_num, my_list, lis ,next_list)         #map ma function pathaune ani add garnu parne variables pathaune 

print(list(sum))

NEW_LIST = list(map(lambda x,y : x+y, my_list, next_list))
print(NEW_LIST)

#filter function
def check( a ):
    if a%2 == 0:
        return True
    else:
        return False 

#lambda x: x%2 == 0    
#sum = map(check, new_list)
    
new_list = list(filter(check, my_list))    #new_list = list(filter(lambda x :x%2 == 0, my_list))
print(new_list)

   

        