class Employee:
    company = "google"
    
    def getsalary(self , signature):
        print(f"The salary is {self.salary} for company {self.company}! {signature} to join with us.")
        
    @staticmethod     #to def a function without taking any arguments use @staticmethod 
    def greet():
        print("Welcome to accenture!")
        
        
sumon = Employee()   #sumon is a object
sumon.salary = 60000
sumon.getsalary("Thanks")
sumon.greet()  #Employee.getsalary("Thanks")