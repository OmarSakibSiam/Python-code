# on demand vlaue generation
#yield keyword
#generate sequence of values over time
#We use generators in Python when we want to produce a sequence of values one at a time
#Used for utilization of memory

def count_down(num):
    while num>0:
        yield num  #it somewhat works like return.generator
        num-=1
        
#for printing all the number together one after another 
for number in count_down(5):
    print(number)

#for printing or accessing one value at a time
x=count_down(5)
print(next(x))
print(next(x))


#problem

def generate_squares(n):
    i=1
    while i<=n:
        yield i**2
        i+=1

for number in generate_squares(4):
    print(number)