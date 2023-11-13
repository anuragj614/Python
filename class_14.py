# class Sagarmatha:
#     def __init__(self):                   #self halnu parxa syntax ho  double underscore hunxa init ko agadi paxadi
#         print("constructor created")
#     def home(self):                        #yeta self nadida pani program chalxa
#         print("method home")
#     def __del__(self):
#         print("destructor")    
        
#sg = Sagarmatha()                     # yo garne bhaye home func ko argument ma self chainxa
#sg.home()

#Sagarmatha.home()                       #class batai fnctn bolayo bhane home func ko argument ma self chaidaina

# class Sagarmatha:
#     def __init__(self, name, age, roll, address):   
#         self.name = name                
#         self.age = age
#         self.roll = roll
#         self.address = address
        
#     def home(self): 
#         print("Name:", self.name)                       
#         print("Age:", self.age)
#         print("Roll number:", self.roll)
#         print("Address ", self.address)    
        
#     def __del__(self):
#         print("destructor")    
        
# sg1 = Sagarmatha("Anurag", 20, 8, "Sanepa")
# sg2 = Sagarmatha("Ishan lwaath", 20, 19, "Lalitpur")
# sg3 = Sagarmatha("Milan chor", 20, 24, "Lalitpur")
# sg1.home() 
# sg2.home()      
# sg3.home()            

class Sagarmatha:
     def __init__(self, age):                 
         self.age = age
        
     def home(self, name): 
         print(self.age)                       
         print(f"Name {name} age is {self.age}")      #f=filtering
           
        
     def __del__(self):
         print("destructor") 
         
sg = Sagarmatha(20)
sg.home("Anurag")