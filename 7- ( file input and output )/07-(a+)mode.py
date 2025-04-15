# a+ mode
# didnt print anything in terminal because pointer is on the end. but it can write in the open file at start

f = open("demo.txt", "a+")
print(f.read())
f.write("abc")
f.close()