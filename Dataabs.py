from abc import ABC,abstractmethod

class Bird(ABC):
    @abstractmethod
    def sound(self):    #you are forced to use the method
        pass #no implementation
class crow(Bird):   
    def sound(self):
       print("crow say kaka")

class chicken(Bird):
    def sound(self):
     print("Chicken calls quack")

bird1=crow()
bird2=chicken()

bird1.sound()
bird2.sound()