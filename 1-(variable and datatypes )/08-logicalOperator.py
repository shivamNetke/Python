#logical operator   (not, and, or)

# not operator
print(not False)
print(not True)

a = 2
b = 1
print(not (a > b))


# and operator
val1 = True
val2 = True
print("and operator : ", val1 and val2)


val3 = True
val4 = False
print("and operator : ", val3 and val4)


# or operator

val5 = True
val6 = True
print("or operator : ", val5 or val6)


val7 = True
val8 = False
print("or operator : ", val7 or val8)


val9 = False
val10 = False
print("or operator : ", val9 or val10)


c = 20
d = 10
print((c == d) and (c > d))  # and needs both values true
print((c == d) or (c > d))  # or needs any value to be true


