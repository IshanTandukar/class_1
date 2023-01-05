#Jan5,2023
class Sagarmatha:
    # def __init__(self , age , name , roll , address):       #init = Constructor
    #     self.name = name
    #     self.age = age
    #     self.roll = roll
    #     self.address = address
        
    
    # def home(self):    #Yeta self na didaa pani program chalxa
    #     print("Name:" , self.name)
    #     print("Age:", self.age) 
    #     print("Roll:" , self.roll)
    #     print("Address:" , self.address)

    def __init__(self,age):
        self.age = age
    
    def home(self,name):
        print(self.age)
        print(f"My name s {name} age is {self.age}")      # f = filtering
        
    def __del__(self):
        print("destructor")

# sg1 = Sagarmatha( "Ishan" ,20 ,  19 , "Lalitpur")      #yesma home function vitra self didaa chalaune ho object call
# sg2 = Sagarmatha("Milanchcor" , 21 ,  24 , "sanepa")

# sg1.home()
# sg2.home()

# Sagarmatha.home()

sg = Sagarmatha(20)
sg.home("Ishan")
