#list methods

# APPEND    ( add one element at the end )
list = [2, 1, 3]
list.append(4)
print(list)
list.append(6-3)
print(list)
print("")

#sort  [ascending order]  (list.sort() ==> sort in ascending order)
list1 = [4, 6, 5]
list1.sort()
print(list1)
#second method
list11 = ["banana", "cherry", "apple"]
list11.sort()
print(list11)
print("")


#sort [decending order]     (list.sort(reverse = True)  ==> sort in decending order)
list2 = [1,3,2,6,4,5]
list2.sort(reverse=True)
print(list2)
#second method
list22 = ["banana", "cherry", "apple"]
list22.sort(reverse=True)
print(list22)
print("")


#reverse        (reverses the list)
list3 = ['a', 'd', 'e', 'c','b']
list3.reverse()
print(list3)
print("")


#insert         (insert element at index)
list4 = [2, 1, 3]
list4.insert(1, 5)
print(list4)        #result = [2, 5, 1, 3]
print("")


#remove       (removes first occurrence of element)
list5 = [5, 6, 7, 4]
list5.remove(6)
print(list5)
list5.remove(4)
print(list5)
print("")



#pop         (removes element at idx)
list6 = [2, 1, 3, 1]
list6.pop(2)
print(list6)
list6.pop(0)
print(list6)
print("")