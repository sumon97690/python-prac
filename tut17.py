# sets 
a={10,2,54,12,8,7}
print(type(a))
print(a)
# suppose
a={10,25,25,41,78}
print(a) #it cannot print the repeative nos

# an empty set can be created using
b= set()  #first create a set and then add the values by b.add(values)
print(type(b))
b.add(4)
b.add(5)
b.add(54)
# we can also add a tuples in the sets but we cannot add a list and dictionary
b.add((9,65,69))
print(b)


