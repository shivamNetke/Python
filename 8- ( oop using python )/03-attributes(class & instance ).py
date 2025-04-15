# attributes ( class and instance )

class Student:
    clgName = "ahmednagar college"
    name = "unknown" # class attr
    def __init__(self, name, marks):
        self.name = name  # obj sttr > class attr
        self.marks = marks
        print("adding new student in database..")

s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)

print(s2.clgName)
print(Student.clgName)
