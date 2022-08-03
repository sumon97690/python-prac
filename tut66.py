# practice5
words=["kutte","harami","saale"]

with open("sample3.txt") as f:
    t=f.read()
    
for i in words:
    t=t.replace(i,"####")
    
    with open("sample3.txt",'w') as f:
        f.write(t)
    