# # print formatting

# name = "john"
# age = "39"

# print(f'{name} is {age} years old')

# # list

# my_list = [1,2,3,4]
# mylist = ['hello', 'hi', 'bye']

# my_list + mylist

# print(mylist + my_list)

# new_list = ['a','s','e','x']
# newlist = [1, 9, 8,4]

# new_list.sort()
# listt = new_list
# print(listt)

# newlist.reverse()
# listtt = newlist
# print(listtt)

# dictionary

my_dict = {'key1':199, 'key2': 200, 'k3': 300}
print(my_dict)

mydict = {'k1': 2.30, 'k2': [1,2,3,4], 'k3': {'k4':'hello'}}
print(mydict)

print(mydict['k1'])
print(mydict['k2'][2])

mydict['k4'] = 'new_value'
print(mydict)

mydict['k5'] = ['a', 'b', 'c', 'd']

print(mydict['k5'][3].upper())

# tuple

t = (1,2,3)

print(len(t))

t = ('a', 'a', 'b')

print(t.count('a'))

# set

myset = set()

myset.add(1)
print(myset)

myset.add(3)
print(myset)

mylisttt = [1,1,1,1,2,3,4,4,5,3,4,3,4,2,1,9]
mysett = set(mylisttt)
print(mysett)

# comparators and logical comparators

print('h' == 'h' and 2 == 2)

print(2 != 2 or 3 == 4)

print(not(1 == 1))