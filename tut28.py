# practice2
sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
elif(sub1+sub2+sub3)/3 <40:
    print("you are fail due to less percentage")
else:
    print("congratulation! you are passed")
    
