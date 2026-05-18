#one child class one parent class

class Animal:
    def sound(self):
        print("Animals make sound")
class Dog(Animal):
    def bark(self):
        print("Dog say baw baw")

dog=Dog()


dog.sound()
dog.bark()