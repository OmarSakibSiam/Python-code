"""
one name,many forms
"""
#len here could be polymorphism.Same name but working in different things
print(len("python"))
print(len((1,2,3)))

#method overrinding:child will replace the parent

class Bird():
    def sound(self):
        print("Birds  make sound")
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