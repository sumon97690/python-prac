# practice7
t=True
i=1

with open('log.txt') as f:
    while t:
        t=f.readline()
        if "python" in t:
            print(t)
            print(f"Python is present in {i}")
        i=i+1
            