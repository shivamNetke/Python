# dictionary methods
student = {
    "name" : "shivam netke",
    "subjects" : {
        "physics" : 97,
        "chemestry" : 98,
        "mathematics" : 95,
    }
}

#01- .keys() # returns all keys
print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))
print()


#02 - .values() # returns all values
print(student.values())
print(list(student.values()))
print()



#03 - .items() # returns all (key, val) pairs as tuples
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
print()


#04 - .get() # returns the key according to value
#print(student["name2"])   #it gives error #stops the code
print(student.get("name2")) #no error #it gives none #didnt stops the code
print()

#05 - .update() # inserts the specified items to dictionary
student.update({"city" : "delhi"})
student.update({"name" : "ravish kumar"})
print(student)

