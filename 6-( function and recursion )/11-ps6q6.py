# write a recursive function to calculate the sum of first n natural numbers

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n

print(sum(int(input("enter the number who's recursive sum you want to find : "))))