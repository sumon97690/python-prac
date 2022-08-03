# n! = 1x2x3x4x5.......n
# we can also say that  
# n! = 1x2x3x4x5........n = (n-1)!*n

# n=5
# product=1
# for i in range(n):
#     product = product*(i+1)
# print(product)

# by using function


def factorial_iter(n):
    product=1
    for i in range(n):
        product = product*(i+1)
    return product

print(factorial_iter(5))

# using recuursive function
n=5
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n* factorial_recursive(n-1)
print(factorial_recursive(5))