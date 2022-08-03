# practice set 2
# a = int(input("Enter a number: "))
class calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        print(f"the square of the number {self.num} is {self.num **2}")
    def cube(self):
        print(f"the cube of the number {self.num} is {self.num **3}")
    def squareroot(self):
        print(f"the square root  of the number {self.num} is {self.num **0.5}")
sumon = calculator(36)
sumon.square()
sumon.cube()
sumon.squareroot()
