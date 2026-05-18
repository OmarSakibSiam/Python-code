list=[1,2,3]
list.append(4)# adding at the end
print(list)

list_1=[1,2,3]
list_2=[4,5,6]
list_1.extend(list_2) #concate creats a new list but this doesnt
print(list_1)

a=[1,2,3]
a.insert(0,"hello") #inserting at specific position
print(a)

print(a.remove(3))#removing a vlaue

b=[1,2,3]
popped= b.pop(0)#removing a value from a specific position
print(popped)
print(b)

c=[1,2,3]
c.clear()#remoing all values
print(c)

d=[4,5,6,4]
print(d.index(6)) #for finding index

counter=d.count(4)
print(counter)

#sort .sort()
#reverse .reverse()
#min/max   min(lisname),max(listname)

f=[1,2,3]
g=[3,4,5]

s1=set(f)#converting list to set
s2=set(g)

s3=s1.intersection(s2)
print(s3) #again converting set to list

#nested list
h=[100,200,300,f,g]
print(h)
