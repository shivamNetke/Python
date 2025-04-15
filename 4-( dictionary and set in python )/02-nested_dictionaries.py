# nested dictionaries

student = {
    "name" : "shivam netke",
    "subjects" : {
        "physics" : 97,
        "chemestry" : 98,
        "mathematics" : 95,
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["mathematics"])