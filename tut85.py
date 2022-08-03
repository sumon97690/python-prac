# inheritance example

class manager:
    company= "google"

    def mandetails(self):
        print("The manager of the company is",self.company)

class Employee(manager):
    position = "software engineer"

    def empdetails(self):
        print("The employee worked in the company name", self.company) #here it will print the company name which is given in the class manager
        print("The position is " +self.position +" for the employee in " +self.company +" company")
comp = manager()
comp.mandetails()
emp = Employee()
emp.empdetails()