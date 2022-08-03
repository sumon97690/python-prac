# practice set dictionaries  and tupless
# practice 1
mydict={
    "pankha":"fan",
    "mandir":"temple",
    "ganit":"maths",
    "kutta":"dog",
    "sher":"lion"
}
print("The options are:",mydict.keys())
a=input("Enter the hindi word:\n")
print("the meaning of you hindi word is: ", mydict.get(a))  #this will print the values for the given key in input


