# write a recursive function to print all elements in a list 
# HINT : use list and index as parameters

def printList(list, index=0):
    if(index == len(list)):
        return
    print(list[index])
    printList(list, index+1)



    
fruits = [str(input("first fruit : ")),str(input("second fruit : ")),str(input("third fruit : ")),str(input("forth fruit : "))]
printList(fruits)