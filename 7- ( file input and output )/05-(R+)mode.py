# r+ mode
# pointer at start

f = open("demo.txt", "r+")
f.write("override ")
print(f.read())
f.close()