# methods ( methods are functions that belongs to objects )

class Student:
    def __init__(self, name, marks):
        self.name = name  # obj sttr > class attr
        self.marks = marks


    def welcome(self):
        print("welcome student,", self.name)

    def getmarks(self):
        return self.marks

s1 = Student("karan", 97)
s1.welcome()

print(s1.getmarks())