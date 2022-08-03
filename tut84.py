# practice set 5
a= input("Enter your name: ")
class train:
    def __init__(self,name,fare,seat,a):
        self.name = name
        self.fare = fare
        self.seat = seat
        self.a = a
        
    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The fare of the seat is {self.fare}")
        print(f"The seats available are {self.seat}")
    def book(self):
        print(f"congratulation {self.a} your ticket for {self.name} is booked")
    
ticket = train("doronto",2800,300,a)
ticket.getstatus()
ticket.book()    
    
    