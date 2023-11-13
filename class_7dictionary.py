# >>> dictionary={'a': 1, 2: 2, 'c': None}
# >>> dictionary[2]
# 2   
# >>> len(dictionary)
# 3   
# >>> dictionary.values()
# dict_values([1, 2, None])
# >>> dictionary[a]    
# >>> dictionary["a"]
# 1    
# >>> dictionary.items()
# dict_items([('a', 1), (2, 2), ('c', None)])
# >>> dictionary.keys()
# dict_keys(['a', 2, 'c'])


dictionary = {'a': 1, 2: 2, 'c': None}
len(dictionary)
dictionary.keys()                                               
print(dictionary)
dictionary.values()
print(dictionary)
for key, value in dictionary.items():
    print(key,value)
    
dictionary = {'Milan': "Chor", 'Ishan': "Good"}
for k, v in dictionary.items():
    print(k,v)    
    
    

# >>> mydict = {1:"one", "two":2}
# >>> mydict
# {1: 'one', 'two': 2}
# >>> mydict["three"] = 3    
# >>> mydict
# {1: 'one', 'two': 2, 'three': 3}
# >>> mydict.items()
# dict_items([(1, 'one'), ('two', 2), ('three', 3)])
# >>> mydict["two"] == 25
# False
# >>> mydict["two"] = 25
# >>> mydict["two"] == 25
# True
# >>> mydict.pop("two")
# 25
# >>> mydict
# {1: 'one', 'three': 3}
# >>> len(mydict)
# 2
# >>> mydict["name"] = "Ram"
# >>> mydict
# {1: 'one', 'three': 3, 'name': 'Ram'}
# >>> mydict.popitem()      last ma j thyo tyo nikalxa
# ('name', 'Ram')
# >>> mydict
# {1: 'one', 'three': 3}


mydict = {1:"one", "two":2}
mydict.update({"maya:Boa"})
print(mydict) 
