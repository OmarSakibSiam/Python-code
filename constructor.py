"""
its a special method
_inti_()

3 types of constructor 
1/default
2/parameterized 
3/constructor with default values

"""
#without constructor
class Car:
    def set_details(self,brand,color):
        self.brand=brand  #for setting inputs
        self.color=color

   
car1=Car() #object
car1.set_details("BMW","Blue")

print(car1.brand)
print(car1.color)


#with constructor

class Car:
    def __init__(self,brand,color):
        self.brand=brand #For setting values
        self.color=color
    
    def show_details(self):
        print(self.brand,self.color) # we didnt use object. we use self.brand ,self.color


car1=Car("tesla","Red") #no need to call the method

car1.show_details()
#print(car1.brand,car1.color)  #outsid printing the details