# practice4

with open('donkey.txt','r') as f:
    t=f.read()
t=t.replace("donkey","######")

with open('donkey.txt','w') as f:
    f.write(t)
