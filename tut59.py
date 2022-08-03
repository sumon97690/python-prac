f=open('sample1.txt','rt') 
data=f.readline()  #it will print only first line 
print(data)
data=f.readline()  #it will print second line 
print(data)
f.close()