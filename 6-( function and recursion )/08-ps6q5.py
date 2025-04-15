# write a program to check entered number is ever or odd

def checker(num):
    if(num % 2 == 0):
        print(num, "is even number")
    else:
        print(num, "is odd number")

checker(int(input("enter the num you want to is it even or odd :")))