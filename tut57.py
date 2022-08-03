# practice8

# a= int(input("Enter the number:  "))

# for i in range(1,11):
#     p=a*i
#     print(p)



a= int(input("Enter the number:  "))

def pattern(val):
    for i in range(1,11):
        p= val*i
    return p

b=pattern(a)
print(b)