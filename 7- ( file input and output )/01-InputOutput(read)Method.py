#input output method

# r = open for reading 
# w = open for writing, truncating the file first (overide in file clear first text and write other)
# x = create a new file and open it for writing
# a = open for writing, appending to the end of the file if it exist 
# b = binary Mode 
# t = text mode 
# + = open a disk file for updating 


f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()