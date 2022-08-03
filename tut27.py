# practice set 

# practice1

a=int(input("Enter the first number a: "))
b=int(input("Enter the second number b: "))
c=int(input("Enter the third number c: "))
d=int(input("Enter the fourth number d: "))

if(a>b and a>c and a>d):
    print("the greatest number is a")
elif(b>a and b>c and b>d):
    print("b is greater")
elif(c>a and c>b and c>d):
    print("The greatest number is c")
else:
    print("the greatest number is d")