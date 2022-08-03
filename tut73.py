# oops 
class Employee:
    company = "google"
    salary = 50000
    
sumon = Employee()
rahul = Employee()
sumon.salary = 40000  #instance variable takeover the values defined in the classes
rahul.salary = 40000
print(sumon.company)
print(rahul.company)
print(sumon.salary)
print(rahul.salary)
Employee.company = "microsoft"
print(sumon.company)
print(rahul.company)
