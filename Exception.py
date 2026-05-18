# Special type of error.
"""
1-start running
2-gives detail msg
3-catch and handle. so programe wont crash
"""
"""
Exception handling
try except

try
except
finally- it will always run
"""
try:
    num=int(input("Enter a number:"))
    result=10/num
    print((f"result:{result}"))
                                        #prbuild exception
except ZeroDivisionError:
    print("you cannot divide with 0")
except ValueError:
    print("Cant devide with string")

finally:
    print("Operation completed")


try:
    password=input("Enter pass: ")
    if len(password)<8:
        raise Exception("Pass word is short")   #Self made exception
except Exception as e:
    print(e)


