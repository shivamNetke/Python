# create student class that takes name and marks of 3 subject as arguments in constructor
# then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getavg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hii", self.name, "your avg score is ", sum/3)

s1 = Student("shivam netke", [99, 98, 97])
s1.getavg()
s1.name = "ironman"
s1.getavg()
    