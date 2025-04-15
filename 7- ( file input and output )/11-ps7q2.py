# waf that replace all occurrence of "java" with "python" in above file.

with open("practice.txt", "r") as f:
    data = f.read()
    
newData = data.replace("java", "python")
print(newData)

with open("practice.txt", "w") as f:
    f.write(newData)