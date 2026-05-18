def uppercase_decorator(func):
    def wrapper():
        result = func().upper()       # Call the original function, e.g., greet()
        return result # Return the uppercase version and returing the to wrapper funtion
    return wrapper      # Return the wrapper function

@uppercase_decorator
def greet():
    return "good morning"

print(greet())  # Calls the wrapper function


def add_exclamation(func):   #It is a decorator of sayhello() function
    def wrapper():
       result=func()+"!"
       return result
    return wrapper

def say_hello():
    return "Hello"
print(say_hello())

@add_exclamation
def say_hello():   #orginal function
    return "Hello"       
print(say_hello())






