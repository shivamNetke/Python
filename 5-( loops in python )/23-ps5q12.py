# wap to find the factorial of first n numbers ( using while )

n = int(input("enter the number :"))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print("total sum :",factorial)