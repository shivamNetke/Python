# waf to find the factorial of n. ( n is the parameter )

def funfactorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i

    print(factorial)

funfactorial(int(input("enter the number you want to find his factorial : ")))