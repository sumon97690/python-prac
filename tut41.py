# Practice4
a=int(input("Enter the number: "))
t=0
for i in range(2,a):
    if(a%i==0):
        t=t+1
if(t>0):
    print("not Prime")
else:
    print("prime")

