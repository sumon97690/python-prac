# file i/o 
# use the open function to print the content of the file 
f=open('sample.txt','r')
# f=open('sample.txt')  #by default the mode is r which is read
data = f.read()
print(data)
# data=f.read(5)  #it is used to read the first 5 characters in sample.txt
# print(data)
f.close()
