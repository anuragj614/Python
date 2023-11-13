mystring="Hello World from our first Python script"

next_string='''"hello world"'''
print(next_string)

my_string = "Hello world"
print(my_string[5])

next_string = '''"hello" world'''
print(next_string)

##"our" in my_string
# a = "Hello world"
# a in my_string
# mystring = "aaabcdefaaaabababababaababaabaabbba"
    
my_string[1:10]

my_string[:-1] #0 dekhi last samma

my_string[::-1] #mirror huncha

my_string[::3] #first dekhi 3 ko gap hudai

my_string.index("H") #jun paila bhetyo tesko index

my_string.index("Hello") #jun paila bhetyo tesko index

my_string.index(" ") #jun paila bhetyo tesko index
 
name = "anurag jaiswal"
name.upper()                        #capital banauna sab lai
uppername = "ANURAG JAISWAL"
uppername.lower()                   #lowercase banauna
name.capitalize()                   #first ko lai capital banaune
name.title()                        #sab word ko first letter lai capital banaune
name +" "+ uppername                #concatinate 2 string

my_string.index("our")              #our ko o ko index dincha
my_string.index("o")                # first o ko index dincha
my_string.split(" ")                #every space ma wordharu lai split garyo
#answer ['Hello', 'world']

my_string.split("o")                #every o ma word split garcha
#answer ['Hell', 'w', 'rld']
o_binako = my_string.split("o")
"o".join(o_binako)                  #o lagera join garcha word lai
"+".join(['Hell', 'w', 'rld'])      #sab lai + le join garcha
str(['Hell', 'w', 'rld'])           #list lai string banaucha
"+".join(str(['Hell', 'w', 'rld', 123]))            #every letter pachi + thapcha
"+".join(['Hell', 'w', 'rld', str(123)])

