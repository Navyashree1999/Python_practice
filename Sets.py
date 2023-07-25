# Sets is used to store multiple items in single variable
# It is defined using curly phrases
# sets are unordered, unchangeable, unindexed and duplicates are not allowed
# sets declaration
this_set = {1, 2, 3, 4, 5}
print(this_set)

this_set = set((1, 2, 3, 4))
print(this_set)

this_set = set()
this_set = {1, 2, 3, 4, 5, 6}
print(this_set)

# unordered --> Items in the sets do not have a defined order
colours = {'red', 'green', 'yellow', 'black'}
print(colours)

#unchangeable--> we can not change the item once the set is defined

# Duplicates are not allowed
fruits = {'apple', 'orange', 'mango', 'grapes', 'apple'}
print(fruits)

this_set = {'apple', 42, 1, True} # Here true and 1 are same and treated as duplicates
print(this_set)

this_set = {'apple', 42, True, 1}
print(this_set)
print(len(this_set))
print(type(this_set))

# Accessing items
# accessing of Items is only possible using for loop

fruits = {'apple', 'orange', 'mango', 'grapes', 'apple'}
for i in fruits:
    print(i)
print("\n")
print('banana' in fruits)

# Adding items into set
# 1. add()
fruits = {'apple', 'orange', 'mango', 'grapes'}
fruits.add("banana")
print(fruits)

'''fruits = {'apple', 'orange', 'mango', 'grapes'}
fruits.add("banana", 'kiwi')
print(fruits)''' # TypeError: set.add() takes exactly one argument (2 given)


numbers = {45, 100, 2, 5, 9}
numbers.add(10.5)
print(numbers)

this_set = { 2, "apple"}
this_set.add(True)
print(this_set)

# 2. update() --> It adds one list to another list
fruits = {'apple', 'orange', 'mango', 'grapes'}
vegetables = {'tomato', 'carrot'}
fruits.update(vegetables)
print(fruits)

fruits = {'apple', 'orange', 'mango', 'grapes'}
new_fruits = ['banana', 'kiwi']
fruits.update(new_fruits)
print(fruits)

fruits = {'apple', 'orange', 'mango', 'grapes'}
numbers = (1, 2, 3,4)
fruits.update(numbers)
print(fruits)

# Remove set items
# 1. remove() --> it remove the item from set by taking element as argument
fruits = {'apple', 'orange', 'mango', 'grapes'}
fruits.remove("orange")
print(fruits)

"""fruits = {'apple', 'orange', 'mango', 'grapes'}
fruits.remove('banana')
print(fruits) # item which we wat remove from does not contain in list it will an error, KeyError: 'banana'"""

# discard()--> if the item to remove does not exit discard() will not raise an error
fruits = {'apple', 'orange', 'mango', 'grapes'}
fruits.discard('banana')
print(fruits)

fruits = {'apple', 'orange', 'mango', 'grapes'}
fruits.discard('apple')
print(fruits)

# pop() --> It can used but there is not sure about which item is removed
fruits = {'apple', 'orange', 'mango', 'grapes'}
fruits.pop()
print(fruits)

# clear()
fruits = {'apple', 'orange', 'mango', 'grapes'}
fruits.clear()
print(fruits)

# del statement it will remove the variable from memory
fruits = {'apple', 'orange', 'mango', 'grapes'}
del fruits
#print(fruits)

# join()--> It as many methods to join two sets
# union()
set1 = {'a', 'b', 'c', 'd'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# intersection_update()--> It keeps the item which present in the both sets
x = {"apple", 'banana', 'cherry'}
y = {'red', 'blue', 'apple'}
x.intersection_update(y)
print(x)

# intersection() --> it returns new set
x = {"apple", 'banana', 'cherry'}
y = {'red', 'blue', 'apple'}
z = x.intersection(y)
print(z)

# symmetric_difference update() --> It keeps all the items which present in bot the sets
x = {"apple", 'banana', 'cherry'}
y = {'red', 'blue', 'apple'}
x.symmetric_difference_update(y)
print(x)

# symmetric_difference()
x = {"apple", 'banana', 'cherry'}
y = {'red', 'blue', 'apple'}
z = x.symmetric_difference(y)
print(z)

# copy()
x = {"apple", 'banana', 'cherry'}
y = x.copy()
print(y)

# difference() --> It it removes the set that contain only in one set
x = {"apple", 'banana', 'cherry'}
y = {'red', 'blue', 'apple'}
z = x.difference(y)

print(z)

# difference_update()
x = {"apple", 'banana', 'cherry'}
y = {'red', 'blue'}
x.difference_update(y)
y.difference_update(x)
print(x)
print(y)

# isdisjoint() --> It returns true if no item x is present in y
x = {"apple", 'banana', 'cherry'}
y = {'red', 'blue', 'apple'}
z = x.isdisjoint(y)
print(z)

x = {"apple", 'banana', 'cherry'}
y = {'red', 'blue'}
z = x.isdisjoint(y)
print(z)

# issubset()
x = {'a', 'b', 'c', 'd'}
y = {'a', 'b'}
print(y.issubset(x))

# issuperset()
print(x.issuperset(y))












































