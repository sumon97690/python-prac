# practice6
with open('log.txt') as f:
    t=f.read()
    
if "python" in t:
    print("Python is present")
else:
    print("python is not present")