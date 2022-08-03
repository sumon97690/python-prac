# practice2

# multiply by 1.8 or  9/5 and add 32
a= int(input("Enter the temperature in celsius: "))

def temperature(celsius):
    faranheit = celsius * float(1.8)+32
    return faranheit

f = temperature(a)
print("The temperature in faranheit is:",+f)
