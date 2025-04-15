# multilevel inheritance

class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotoCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotoCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()