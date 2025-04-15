# define a circle class to create a circle with radius r using the constructor. define an Area() method of the class which calculates the area 
# of the circle. define a perimeter() method of the class which allows you to calculate the perimeter of the circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())