# practice7
# this = "             sumon is a good boy        "
# print(this.strip())      strip method is usedto remove the space

# now using func

def remove_and_strip(string,word):
    str = string.replace(word," ")
    return str.strip()

this = "         sumon is a good boy           "
n= remove_and_strip(this,"sumon")
print(n)

