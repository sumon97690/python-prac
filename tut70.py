# pratice9
file1="copy.txt"
file2="this.txt"
with open(file2) as f:
    t=f.read()
    
with open(file1) as f:
    r= f.read()
    
    
if t==r:
    print("Files are identical")
else:
    print("Files are not identical")


