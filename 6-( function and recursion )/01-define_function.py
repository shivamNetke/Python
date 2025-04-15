# define function

def calcAdd(a, b):
    Add = a + b
    print("the addition of",a ,"and", b, "is", Add)


def calcSub(a, b):
    sub = a - b
    print("the substraction of",a ,"and", b, "is", sub)

def calcMul(a, b):
    mul = a * b
    print("the multiplication of",a ,"and", b, "is", mul)

def calcDiv(a, b):
    div = a / b
    print("the division of",a ,"and", b, "is", div)

def print_hello(name):
    print("hello", name)


print_hello(str(input("whats your name :")))
print("lets do additon...")
calcAdd(int(input("enter value of a :")), int(input("enter value of b :")))
print()
print("now substraction...")
calcSub(int(input("enter value of a :")), int(input("enter value of b :")))
print()
print("now multiplication...")
calcMul(int(input("enter value of a :")), int(input("enter value of b :")))
print()
print("finally division")
calcDiv(int(input("enter value of a :")), int(input("enter value of b :")))
