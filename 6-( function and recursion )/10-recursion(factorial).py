# recursion by factorial

def fact(n):
    if(n == 1 or n == 0 ):
        return 1
    return fact(n - 1) * n

print(fact(int(input("enter the number who's factorial you want to find : "))))