"""
Adding a funciton inside main function without changing the main function
A decorator is a function that takes another function as an argument, adds some behavior, and returns a new function.
"""
def my_decorator(func):   #Function as a paremeter
    def wrapper():
        print("Something is happening before the function is called")
        func()  #here we decorated the function by adding sentences before and after
        print("Somthing is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("hello")   #This is passed into my_decorator as argument
    
say_hello()


def uppercase_decorator(func):
    def wrpper():
        result=func()   #Ekta function argument hishebe nitesi(func) oita arekta function dhkay decorate kortesi the returning the other function
        return result.upper()
    return wrpper()



@uppercase_decorator
def greet():                        # greet = uppercase_decorator(greet)
    return "good morning"

print(greet())  