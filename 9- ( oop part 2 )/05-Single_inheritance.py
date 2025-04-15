# inheritance type

# single inheritance
#eg of single inheritance :-

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar('forturner')
car2 = Toyotacar("prius")
print(car1.name)
print(car1.color)

