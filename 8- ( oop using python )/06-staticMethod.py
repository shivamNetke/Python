# static method
# methods that dont use the self parameter ( work at class level )

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")


s1 = Student("karan", 97)
print(s1.name, s1.marks)
s1.hello()