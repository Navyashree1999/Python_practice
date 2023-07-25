# Dictionary saves the data in the for of key_value pair
# it is ordered, changeable, not allowed duplicates
# syntax
car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015
}
print(car)

car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015,
    "year"  : 2016
}
print(car) # Dictionary does not allow duplicate it consider latest value of specified key

car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015
}
car["model"] = "Safari"
print(car) # item inside dictionary can be changeable

# accessing of elements inside dictionary
# 1. using key inside square brackets
car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015
}
print(car["brand"])
print(car["model"])
#print(car["colour"])--> if the specified key is not present in the dictionary it throw "key error"

# 2. using get() we can also access elements
fruits = {
    "name" : "apple",
    "colour" : "red",
    "cost" : 100
}
print(fruits.get("name")) # get() takes key as an argument and if specified key not present in dictionary it will not throw error insted returs none

# 3. if we want only keys we will use key()
print(car.keys())
print(fruits.keys())

#4. if want only values we can use values() it will return values list
print(car.values())
print(fruits.values())

# 5. if we want both key and value simultaneously we can use item()
print(car.items())
print(fruits.items())

# adding element or updating can be done in dictionary
# 1. using key[]
fruits = {
    "name" : "apple",
    "colour" : "red",
    "cost" : 100
}
fruits["cost"] = 200 # updating cost
print(fruits)
car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015
}
car["cost"] = 500000
print(car)

# we can also use update()
car.update({"cost" : 700000})
print(car)

# we can use in keyword to check key is present or not
if "cost" in car:
    print("cost key is present")

# we can remove item from dictionary
# 1. pop() -> takes key as argument
car.pop("cost")
print(car)

# 2. pop item() -> by default this item going to remove last item
car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015,
    "cost" : 500000
}
car.popitem()
print(car)

# 3 using delete statement
del car["model"]
print(car)

del car
#print(car)

# 4 using clear()
car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015,
    "cost" : 500000
}
car.clear()
print(car)

# python looping dictionaries
car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015,
    "cost" : 500000
}
for x in car:
    print(x)
print('\n')
for x in car:
    print(car[x])
print('\n')
for y in car.keys():
    print(y)
print('\n')
for x in car.values():
    print(x)
print('\n')
for x, y in car.items():
    print(x,y)
print('\n')

# we can copy elements from one dictionary to other
# 1. copy()

vehicle = car.copy()
print(vehicle)

# 2. dict()
vehicle1 = dict(car)
print(vehicle1)

# nested loop
car = {
    "car1" : {
        "brand" : "Tata",
        "name" : "nexon",
        "year" : 2015
    },
    "car2" : {
        "brand" : "Honda",
        "name" : "civic",
        "year" : 1999
    },
    "car3" : {
        "brand" : "Toyota",
        "name" : "camry",
        "year" : 2000
    }

}
# accessing items in Nested Dictionaries
print(car["car1"]["brand"])

# setdefault()
car = {
    "brand" : "Tata",
    "model" : "Nexon",
    "year"  : 2015
}
car.setdefault("cost",500000)
print(car)

# fromkeys() --> this methods will create a dictionary from the given sequence of keys and values
x = {"a", "b", "c"}
y = 1

z = dict.fromkeys(x,y)
print(z)

keys = {"a","e","i","o","u",}
values = 'vowel'
vowels = dict.fromkeys(keys,values)
print(vowels)

# fromkeys() without value

keys = [1, 2, 3]
numbers = dict.fromkeys(keys)
print(numbers)












