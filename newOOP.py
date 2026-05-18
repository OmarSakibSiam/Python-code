"""class car():
    #method
    def start(self):
        print("Car is starting....")
    def stop(self):
        print("Car is stopping....")


car1=car() #objects
car2=car()

car1.start()  #object calling the methods
car2.stop()"""


class Car:
    def set_details(self,brand,color):
        self.brand=brand  #for setting inputs
        self.color=color

    def show_details(self):
        print(f"This car is a {self.color},{self.brand}")


car1=Car()
car1.set_details("BMW","Blue")

car1.show_details()