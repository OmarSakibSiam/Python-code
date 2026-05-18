"""radius=float(input("Enter radius:"))
area_of_circle=3.14*radius**2
print(f"Area=",area_of_circle)"""""

#conditional statement

"""age=int(input("Enter your age:"))
if age>=18:
    print("You can vote")
elif age<=0:
    print("Invalied")
else:
    print("You are under aged.")"""

num1=float(input("Give 1st number:"))
num2=float(input("Give 2nd number:"))

choice=input("What would you like to do (+,-):")

if choice=='+':
    print(f"addition:{num1+num2}")
elif choice=='-':
    print(f"subtraction:{num1-num2}")
else:
    print("Invalid")