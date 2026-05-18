
"""file_2 = open("E:/CODE/files2.txt", "w")
content_2 = input("Write something on file: ")
file_2.write(content_2)
print("Data saved successfully")
file_2.close()  # This is the correct way to close the file"""

#with statement
#with open("file_name",mode) as file


with open("E:/CODE/files2.txt","w") as file:
    content=input("enter :")
    file.write(content)
    print("saved!")    #no need to write close state here

