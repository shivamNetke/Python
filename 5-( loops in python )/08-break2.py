# break

# search for a number x in this tuple using loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter the no you want to find :"))
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at index", i)
        break
    i += 1
else:
    print("no not found in the data")