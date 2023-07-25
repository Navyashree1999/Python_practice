# Tuple isa data type which store multiple data at once
# Characteristics of Tuple are ordered, unchangeable and duplicate is allowed
#syntax tuple_name = (elememt1, element2,....)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# other ways of deceleration---> tuple constructor
my_tuple = tuple(('red', 'blue', 'green', 'yellow'))
print(my_tuple)

my_tuple = tuple()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# we can create tuple with one item but at end you add comma(,) otherwise python will not recognise it as tuple
new_tuple = (1)
print(type(new_tuple)) # it is considered as int not tuple to make it tuple at the end we have to give ,

new_tuple = (1,)
print(type(new_tuple))

new_tuple = ('apple')
print(type(new_tuple))

new_tuple = ('apple',)
print(type(new_tuple))

# tuple is heterogeneous --> means we can store any datatype inside single tuple

my_tuple = (1, 2, "red", True)
print(my_tuple)
print(type(my_tuple[0]))

# Access Tuple items --> it can through indexing, slicing and looping statement
my_tuple =(1, 2, 3, 4)
print(my_tuple[1])
print(my_tuple[1:4])
print(my_tuple[:4])
print(my_tuple[:])
print(my_tuple[-3:-1])
print(my_tuple[::-1])

for i in my_tuple:
    print(i)
print(('\n'))

for i in range(len(my_tuple)):
    print(my_tuple[i])
print(('\n'))

for i in range(0,4): # it takes index value
    print(my_tuple[i])
print(("\n"))

my_tuple = ('red','green', 'orange', 'yellow')
i=0
while i<len(my_tuple):
    print(my_tuple[i])
    i+=1
print(("\n"))

my_tuple = (1, 2, 3, 4, 5)
i=0
while i<len(my_tuple):
    print(my_tuple[i])
    i+=1

# add or remove items from Tuple directly is not possible because Tuple is unchangeable
# we do it my converting into list

my_tuple = ('apple', 'mango', 'orange', 'grapes')
new_tuple = list(my_tuple)
new_tuple.append('kiwi')
my_tuple = tuple(new_tuple)
print(my_tuple)
print(("\n"))


my_tuple = ('apple', 'mango', 'orange', 'grapes')
new_tuple = list(my_tuple)
new_tuple.pop()
my_tuple = tuple(new_tuple)
print(my_tuple)
print(("\n"))

my_tuple = ('apple', 'mango', 'orange', 'grapes')
new_tuple = list(my_tuple)
new_tuple.pop(2)
my_tuple = tuple(new_tuple)
print(my_tuple)
print(("\n"))

my_tuple = ('apple', 'mango', 'orange', 'grapes')
new_tuple = list(my_tuple)
new_tuple.remove("mango")
my_tuple = tuple(new_tuple)
print(my_tuple)

print(("\n"))

my_tuple = ('apple', 'mango', 'orange', 'grapes')
new_tuple = list(my_tuple)
new_tuple.clear()
my_tuple = tuple(new_tuple)
print(my_tuple)
print(("\n"))

my_tuple = ('apple', 'mango', 'orange', 'grapes')
del new_tuple
print(my_tuple)
print(("\n"))

# Adding Tuple to a tuple this can be done by relational operator (+=)
thistuple = ('apple','banana', 'cherry')
y = ('orange',)
thistuple+=y
print(thistuple)

# unpack Tuple --> extracting value in tuple back to variables is known as unpacking
fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

'''fruits = ('apple', 'banana', 'cherry')
(green, yellow) = fruits
print(green,yellow) # ValueError: too many values to unpack (expected 2)'''

'''fruits = ('apple', 'banana')
(green, yellow,red) = fruits
print(green,yellow,red) # not enough values to unpack (expected 3, got 2)'''

# above errors can be avoided using asterisk (*)
fruits = ('apple', 'banana', 'cherry')
(green, *yellow) = fruits
print(green,yellow)

fruits = ('apple', 'banana', 'cherry')
(*green, yellow) = fruits
print(green,yellow)

# Join two tuples
my_tuple1 = ('apple', 'mango', 'orange', 'grapes')
my_tuple2 = (1, 2, 3)
new_tuple =my_tuple1 + my_tuple2
print(new_tuple)

# if we want to multiply the content of tuple
my_tuple = (1, 2, 3)
my_tuple1 = my_tuple * 2
print(my_tuple1)

# tuple methods
# 1. count() --> returns the number of times the specified value returns
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))

# 2. index() --> it returns index of specified value
my_tuple1 = ('apple', 'mango', 'orange', 'grapes')
print(my_tuple1.index('mango'))






























