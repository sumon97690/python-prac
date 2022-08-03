# practice2
def game():
    return 150


score = game()
print(score)

with open('hiscore.txt','r') as f:
    hiscore=(f.read())

if hiscore==" ":
    with open('hiscore.txt','w') as f:
        f.write(str(score))
elif int(hiscore)<score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))
        
    

