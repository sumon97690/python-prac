# multiple inheritance means 2 parent and 1 child ==> 2 base class and 1 derrived class.........

class company:
    compcode = 555

class manager:
    name = "sumon ghosh"
    level = 0
    def mandetails(self):
        print("HELLO GUYZZZ")
    
class Employee(company,manager):
    product = "Medical item"

c = company()
print(c.compcode)
m = manager()
e = Employee()
print(e.level)
print(e.product)
print(e.name)
print(e.compcode)
e.mandetails()
