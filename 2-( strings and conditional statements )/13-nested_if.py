#nested if

age = int(input("enter your age : "))

if( age > 1):
    print("please enter valid age")

elif( age >= 18):

    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")


else:
    print("cannot drive")