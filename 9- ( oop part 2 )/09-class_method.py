#  class method
# a class method is bound to the class and receives the class as an implicit first agrument
# note - static method cant access or modify class state and generally for utility

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("shivam netke")
print(p1.name)
print(Person.name)
