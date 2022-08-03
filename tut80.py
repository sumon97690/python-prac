# practice set 1
class programmer:
    company = "microsoft"
    
    def __init__(self,name,product):
        self.name= name
        self.product = product
        
    def getinfo(self):
        print(f"welcome {self.name} to our company {self.company} you product is {self.product}")
        
sumon = programmer("sumon","apple")
sachin = programmer("sachin","micro")
sachin.company = "micro"
supriyo = programmer("supriyo","google")
supriyo.company = "google"


sumon.getinfo()
sachin.getinfo()
supriyo.getinfo()
        