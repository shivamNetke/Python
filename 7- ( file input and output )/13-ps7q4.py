# waf to find in which line of the file does the word "learning" occur first.
# print -1 if word not found

def checklineno():
    word = "learning"
    data = True
    lineno = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(lineno)
                return
            lineno += 1
    return -1

print(checklineno())