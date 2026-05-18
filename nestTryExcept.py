try:
    num1=int(input("Enter number_1"))
    num2=int(input("Enter a number_2"))
    try:
        result=num1/num2
        print(result)
    except ZeroDivisionError:
        print("You cant devide with zero")
except ValueError:
    print("provide a valid input")