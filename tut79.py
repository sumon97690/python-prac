class Employee:
    company = "google"
    
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary = salary
        print("Hello")

    def getdetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The age of the employee is {self.age}")
        print(f"The salary of the employee is {self.salary}")
        
    
    def getsalary(self , signature):
        print(f"The salary is {self.salary} for company {self.company}! {signature} to join with us.")
        
    @staticmethod     #to def a function without taking any arguments use @staticmethod 
    def greet():
        print("Welcome to accenture!")
        
        
sumon = Employee("Rahul",20,30000)#sumon is a object
sumon.getdetails()