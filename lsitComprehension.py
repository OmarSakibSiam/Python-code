#list comprehension
"""
Mainly used for creating list for a specific condition
expression like x*2
for in range(1,11)
condition-if 

"""
squares=[]
for i in range(1,11):
    squares.append(i**2)    #Without list comprehension. Used append method to add value in a existing list
print(squares)


squares_1=[i**2 for i in range(1,11)]  #with list comprehension
print(squares_1)

squares_2=[i**2 for i in range(1,11) if i%2==0]
print(squares_2)