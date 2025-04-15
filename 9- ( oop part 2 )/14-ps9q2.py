# define a employee class with attributes role, department and salary. this class also has a showDetails() method
# create an enginner class that inherits properties from employee and has additional attributes : name and age


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role = ", self.role)
        print("department = ", self.dept)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Enginner", "IT", "75000")


# e1 = Employee("account", "finance", "80000")
# e1.showDetails()


eng1 = Engineer("shivam netke", 40)
eng1.showDetails()