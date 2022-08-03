# practice set 4
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
    @staticmethod
    def user():  #to greet a user ... static isliye banate h taaki uske andar self nhi chahiye rhta h...
        print(f"hello sumon welcome to our group")
sumon = calculator(36)
sumon.square()
sumon.cube()
sumon.squareroot()
sumon.user()
