# dictionary in python
# dictionary is mutable (changeable)
                  

info = {
    "name" : "shivam",
    "subject" : ["python", "c", "java"],
    "topics" : ("dictionary", "set"),
    "learning" : "python",
    "age" : 20,
    "is adult" : True,
    "sgpa" : 9.4,

}
print(type(info))
print(info)
print(info["name"])
print(info["topics"])
print(info["subject"])
print(info["age"])
print()

info["name"] = "shiv"
info["surname"] = "netke"
print(info)

nulldict = {}
print(nulldict)

nulldict["name"] = "apnacollege"
print(nulldict)
