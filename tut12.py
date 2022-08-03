# create a list using []
a= [1,2,3,4,56,7,8]

# print the list using print function
print(a)
# print the seperate values in the list using indexing
print(a[2])

# change the value in the list
a[0]= 45
print(a)

# list indexing
friends= ["sumon","sachin","raju","raja","mali",45]
print(friends[1:4])
print(friends[-5:])

# types of list methods
l1= [1,8,7,9,6,4,22,3]
# l1.sort()  #to sort the list
# l1.reverse() #to reverse the list
# l1.append(45)  # to add the values at the end of the list
# l1.append(46)
l1.insert(4,99)
l1.pop(2)  #it will delete the value for which the index is given
l1.remove(9) #it will remove the value for which the value is given
print(l1)
