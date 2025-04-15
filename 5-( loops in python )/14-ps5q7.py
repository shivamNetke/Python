# search for a number x in this tuple using loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter the number you want to find :"))
idx = 0
for n in tup:
    if(n == x):
        print(x,"found at index", idx)
        break
    idx += 1
else:
    print("the no you entered is not exist in the tuple")
