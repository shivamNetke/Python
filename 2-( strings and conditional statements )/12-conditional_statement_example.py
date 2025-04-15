marks = input("ENTER YOUR MARKS : ")
marks = int(marks)
if(marks > 100):
    print("enter valid marks")
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student -> ",grade)
