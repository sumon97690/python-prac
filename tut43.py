# practice6

# write a program to calculate the factorial of a given number using FOR loop
factorial=1
a=int(input("Enter a number: "))
for i in range(1,a+1):
    factorial= factorial * i
print(factorial)