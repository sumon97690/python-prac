# syntax of function
# def func1():
#     print("hello")


# functions

def average(marks):
    p=(marks[0]+marks[1]+marks[2])/3
    return p

marks1 = [10,50,25]
ans1 = average(marks1)

marks2 = [10,50,14]
ans2 = average(marks2)

print(ans1,ans2)