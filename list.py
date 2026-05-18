#List

#squarbracets
my_list=[1,2,3,4,"hello",True]
print(my_list)

#list constructor
my_list_2=list((1,2,3,4,"hello",True))
print(my_list_2)

#Accessing list values

lst=[1,2,3,4,5,]
print(lst[0])

lst[1]="hello" #updating
print(lst)

lst_2=[1,2,3,4,5]
lst_2[0:3]=10,20,30
print(lst_2)

#concating lists
result=lst+lst_2
print(result)

#repeting
print(lst*2)

#aliasing
list_1=[1,8,6,4]
list_2=list_1
print(list_2)

list_2[0]=100
print(list_1,list_2)

#copy method #list_2=list_1.copy()




