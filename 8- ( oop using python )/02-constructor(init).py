# constructor init function
# the self parameter is a reference to the current instance of the class,
#  and is used to access variables that belongs to the class

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)