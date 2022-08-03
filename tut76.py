class Employee:
    company = "google"
    
    def getsalary(self):
        print(f"The salary is {self.salary} for company {self.company}")
        
        
sumon = Employee()   #sumon is a object
sumon.salary = 60000
sumon.getsalary()