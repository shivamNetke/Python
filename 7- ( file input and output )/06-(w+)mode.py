# w+ mode
# didnt print anything in terminal because pointer is on the end. but it can write in the open file

f = open("demo.txt", "w+")
print(f.read())
f.write("abc")
f.close()