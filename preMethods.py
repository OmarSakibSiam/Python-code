
#All predifined method in STRING

#Lowering upper letters
str="THIS IS DOG"
print(str.lower())  #just add .lower() with varaible

str="THIS IS DOG".lower()
print(str)

#Upper case
str="this is a dog"
print(str.upper())  #just add .upper() with varaible

str="this is a dog".upper()
print(str)

#Capitizing the fast letter
str="this is a dog"
print(str.capitalize())  #just add .capitalize() with varaible

str="this is a dog".capitalize()
print(str)

#Title 
str="this is a dog"
print(str.title())  #just add .title() with varaible

str="this is a dog".title()
print(str)

#swapcase
str="This Is A Dog"
print(str.swapcase())  #just add .swapcase() with varaible

#find(finding the index number of the charecter's first occurance)
text="My name is siam"
print(text.find("s"))

#Replace method
text="Python programme"
print(text.replace("Python","Jave"))

#Split method
str="a,b,c"
print(str.split(","))

text="My name is siam"
s=text.split(" ")
print(s)

#join method
print(" ".join(s)) #first write the way you wanna join then write the vriable in .join()

#cheaking method
str="python"
print(str.startswith("p"))

print(str.endswith("n"))

#isdigit() method
str="123a"
print(str.isdigit())#false
str="1234"
print(str.isdigit())#True

#.isalnum() for cheaking number in string