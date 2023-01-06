class Visualization:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def home(self):
        print(self.name , self.age)


viz = Visualization('ram' , 20)

viz.home()

