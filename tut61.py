# automatically open and close the file without using close() _Statement


with open('sample.txt','r') as  f:
    a=f.read()
    
print(a)