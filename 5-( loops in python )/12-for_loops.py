# for loops

# for - in

nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)


allveggies = ["potato", "brinjal", "ladyfinger", "cucumber", "chilli"]
for veggies in allveggies:
    print(veggies) 


# for loop on tuple
tup = (1, 2, 3, 4, 5, 6)

for num in tup:
    print(num)

# for loop on string

str = "ShivamNetke"
for char in str:
    print(char)


str1 = "apnacollege"
for char1 in str1:
    if(char1 == 'o'):
        print("o found")
        break
    print(char1)
else:
    print("end")