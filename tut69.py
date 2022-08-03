# practice8
with open('this.txt','r') as f:
    t=f.read()
    
with open('copy.txt','w') as f:
    f.write(t)
    