# dictionaries

mydict= {
    "keys": "values",
    "que": "ans",
    "list" : [10,25,85],
    "peoples": "good",
    "anotherdict": {'sumon':'engineer'}
    }
print(mydict)
print(mydict['que'])
print(mydict['list'])
print(mydict['peoples'])
print(mydict['anotherdict'])

mydict['list']= [20,35]
print(mydict['list'])
print(mydict)

# dict methods
print(mydict.keys()) #it will print the keys
print(mydict.values()) #it will print the values
print(mydict.items()) # it will print in form ('keys','values')
updatedict={
    "study":"knowledge"
}
mydict.update(updatedict) #to update keys and values in the dict
print(mydict)

print(mydict.get("que"))
print(mydict["que"]) #the value should be present in the dict

print(mydict.get("que1")) #it will throw an error as que1 is not present in the dict
print(mydict["que2"])



