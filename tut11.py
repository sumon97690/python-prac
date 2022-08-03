# string practice set
# write a python program of user entered a name with a message good afternoon

a=input("Enter your name: \n")
print("good afternoon",a)

# to detect double spaces in the string
b="my name is s  umon ghosh"
print(b.find("  "))

# q2

letter= '''Dear <|name|> ,
            you are selected!
            congratulation you can join us soon at any moment!
            <|date|> '''
            

name=input("Enter your name: \n")
date =input("enter the date: \n")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)

print(letter)

###############################

f="my name is s  umon ghosh"
print(f.replace("  "," "))