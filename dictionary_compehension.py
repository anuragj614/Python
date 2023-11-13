price_of_iterm = {
            'apple': 120,
            'banana': 330,
            'orange': 210,
            'pear': 210,
            'grape': 410,
            'pineapple': 560,
            'strawberry': 770,
            'watermelon': 660
}
# item__dict = {} #initial dictionary
# for key, value in price_of_iterm.items():
#     print("Old price", key, value)
#     value = value + value*0.13
#     print("New Price",key, value)
# #updating keys

#     item__dict [key] = value
# print(item__dict)


for key, value in price_of_iterm.items():
     print("Old price", key, value)
     value = value + value*0.13
     print("New Price",key, value)
     #updating keys
     price_of_iterm.update({key : value}) #update yesari garda kam memory lincha
    
print(price_of_iterm)

#arko easy way also most used
iterm_dict = {f"{key}'s" : value+value*0.13 for key,value in price_of_iterm.items()} #f halechi format garera curly
# print(iterm_dict)                                                                    # bracket ma sida update garna milcha
#ramro dekhna
for key,value in price_of_iterm.items():
    print(key,value)
    
 #function
def get_price_of_iterm(price_of_iterm, tax_rate = 0.13):
    return {key : value+value*tax_rate for key,value in price_of_iterm.items()} 

print(get_price_of_iterm(price_of_iterm))   
#argument pass garyo bhane override garera naya result aauxa
print(get_price_of_iterm(price_of_iterm, 0.15)) #0.15 le badaucha price 15%

#f(x) = x^2+ 5x+ 1
#f(1) = 1^2+ 5*1 +1 =7

def calculate_f(x):
    return x**2 + 5*x + 1
print(calculate_f(1)) 
#lamda fun ekchoti call bhayechi afai del huncha memory ko astitwa(identity) sakkinxa

f = lambda x : x**2 + 5*x + 1
print(f(1))
#string ko concatenation
f = lambda name,naam : name + naam + "1"
print(f("asa","cutie"))

f = lambda x,y : x**2 +5*x*y +1
print(f(4,5))



