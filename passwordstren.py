#check password strength

def check_password(password):
    if len(password)<8:
        raise Exception("Error:Password has to be  8 character")   #custom exception
    print("password is strong")

try:
    password=input("Enter password: ")
    check_password(password)
except Exception as e:              
    print(e)