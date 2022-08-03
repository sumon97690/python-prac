import os
oldname="sample5.txt"
newname="newname.txt"

with open(oldname) as f:
    t=f.read()
    
with open(newname,'w') as f:
    f.write(t)
    
os.remove(oldname)