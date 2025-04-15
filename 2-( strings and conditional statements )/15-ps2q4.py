# wap to find the greatest of 3 numbers entered by the user


num1 = int(input("enter the num 1 : "))
num2 = int(input("enter the num 2 : "))
num3 = int(input("enter the num 3 : "))



if(num1 > num2):                            # second method:
                                            #if( num1 >= num2 and num1 >= num3):
    gnum = "num 1 is greater"               #   print("first num is largest",num1)
                                            #elif( num2 >= num3):
    gnum = "num 1 is greater"               #   print("second num is largest",num2)
elif(num2 > num3):                          #else:
    gnum = "num 2 is greater"               #   print("third is largest",num3)
                                            
elif(num3 > num1):
    gnum = "num 3 is greater"

else:
    gnum = "dont enter same number"

print(gnum)