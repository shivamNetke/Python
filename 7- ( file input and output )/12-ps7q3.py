# search if the word "learning" exist in the file or not
def checkword():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")

checkword()