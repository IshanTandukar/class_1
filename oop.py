# # class Animal:
# #     def __init__(self , name ) :
# #         self.name = name

# #     def make_sound(self) :
# #         print("some animal sound")
# #         bark = f'{self.name} + barks'
# #         return bark


# # class Dog(Animal) : 
# #     def make_sound(self):
# #         super().__init__()
# #         super().make_sound()
# #         print("Woof")

# # dog = Dog("Max")
# # print(dog.name)
# # dog.make_sound()        
# # #  ann = Animal{"Jack"}            


# class Animal:
#     def make_sound(self) :
#         None

# class Cat(Animal) :
#     def make_sound(self):
#         print("meow")
    
# class Horse(Animal) :
#     def make_sound(self):
#         print ("Neigh")

# def make_sound(animal) :
#     animal.make_sound()

# cat = Cat("Seto Biraalo")
# horse = Horse()


#Data Hiding
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self._year = year
        
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        #protected
        return self._year
    
    def set_make(self, make):
        self.__make = make
        
    def set_model(self, model):
        self.__model = model
        
    def set_year(self, year):
        self._year = year
        
car = Car("Toyota", "Camry", 2022)
print("Make:", car.get_make())
print("Model:", car.get_model())
car.set_year(2021)
print("Year:", car.get_year())
