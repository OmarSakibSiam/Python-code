#pairs-> key:value
#key should be unique.Other wise it will be overwritten


my_dict={
    "Name":"Siam","Age":24, "Marks":1185    #we can also store list and touple
}
print(my_dict)

my_dict["class"]=10     #adding a vlaue
print(my_dict)

my_dict["Age"]=25
print(my_dict)          #updating


my_language={
    "name":"Python","version":3.9
}
del my_language["version"]              #deleting
print(my_language)


#METHODS

profile={
    "name":"siam",
    "age":25,
    "Salary":25000
}

#get()

age=profile.get("age")
#age=profile.get("age_2","not found") #normally None ,here not found
print(age)

#keys()
keys=profile.keys()
print(list(keys))

#values()
value=profile.values()
print(list(value))

#items
all_item=profile.items()
print(list(all_item))

#pop()
popped=profile.pop("age")
print(profile)

#popitem()
popped_i=profile.popitem()
print(profile)             #deleting last item

#clear()
clear=profile.clear()
print(profile)