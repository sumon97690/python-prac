# default parameter value 

def greet(name="stranger"):
    print("good day," + name)

a=input("Enter you name: ")
greet(a)
greet()    #it will print the default name "stranger"