# set methods
# set is mutable
# but sets elements are immutable

# .add() # add an element
coll1 = set()
coll1.add(1)
coll1.add(2)
coll1.add(3)
coll1.add(3)
print(coll1)
print()

# .remove() # remove an element
coll2 = set()
coll2.add(4)
coll2.add(5)
print(coll2)
coll2.remove(4)
print(coll2)
print()

# .clear() # empty the set
coll3 = set()
coll3.add(6)
coll3.add(7)
print(coll3)
coll3.clear()
print(coll3)
print(len(coll3))
print()

# .pop() # removes a random value
coll4 = {"hello", "shivam", "world", "coding", "python"}
print(coll4)
coll4.pop()
print(coll4)
coll4.pop()
print(coll4)
print(coll4.pop())
print()

# .union() # combines both set values and returns new
coll5 = {1, 2, 3}
coll6 = {2, 3, 4}
print(coll5.union(coll6))
print(coll5)
print(coll6)
print()

# .intersection() # combines common values and returns new
coll7 = {5, 6, 7}
coll8 = {6, 7, 8}
print(coll7.intersection(coll8))
print(coll7)
print(coll8)
print()