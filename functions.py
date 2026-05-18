def greet(name): #parameter
    '''displaying a hi massage''' #docstrings
    print(f"hi!{name}")

greet("siam") #argument

"""
positional argument
keyword argument
default argument
"""
#key word
def greet(name,city): 
   print(f"hi!{name} to {city}")

greet(name="siam",city="Dhaka") 


#default argument
def greet(name="siam",city="Dhaka"): 
   print(f"hi!{name} to {city}")

greet()

def circle(r):
  print(f"Area:{3.14*r**2}")

circle(r=8)


#Return

def get_full_name(first_name,last_name):
   full_name=f"{first_name}{last_name}"         #store the argument or vlaues in a variable
   return full_name

name=get_full_name("omar","Siam")
print(name)

def circle_1(r):
   area=3.1416*r**2
   return area

a=circle_1(8)
print(a)