# waf to print the elements of a list in single line. ( list is the parameter)

cities = ["delhi", "gurgoan", "noida", "pune"]
# print(cities[0], end=" ")
# print(cities[1], end=" ")
# print(cities[2], end=" ")
# print(cities[3], end=" ")

def plist(list):
    for item in list:
        print(item, end=" ")

plist(cities)