# wap to enter marks of 3 subjects from the user and store them in a dictionary. 
# start with an empty dictionary and add one by one. use subject as key and marks as value

subject = {}
subject.update({"physics" : int(input("enter physics marks : "))})
subject.update({"chemestry" : int(input("enter chemestry marks : "))})
subject.update({"math" : int(input("enter math marks : "))})

print(subject)