# with syntax
# with automatically close the file

with open("demo.txt", "r") as n:
    data = n.read()
    print(data)

with open("demo.txt", "w") as n:
    n.write("new data")