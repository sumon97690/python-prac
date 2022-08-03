# practice set
# practice1

a = int(input("Enter the no1: "))
b = int(input("Enter the no2: "))
c = int(input("Enter the no3: "))

def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3 and num2>num1:
        return num2
    else:
        return num3
print("The maximum no is:",+maximum(a,b,c))