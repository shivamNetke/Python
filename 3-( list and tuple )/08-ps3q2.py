# wap to check if  a list contains a palindrome of elements. (   hind: use copy() method 
list1 = []
l1 = input("enter he contain 1 : ")
l2 = input("enter he contain 2 : ")
l3 = input("enter he contain 3 : ")
print("")

list1.append(l1)
list1.append(l2)
list1.append(l3)


copylist1 = list1.copy()
copylist1.reverse()
if(copylist1 == list1):
    print("it is palindrome")
    print("")
          

else:
    print("it is not palindrome")
    print("")
