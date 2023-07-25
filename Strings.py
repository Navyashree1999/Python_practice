name_1 = 'Aarun'
name_2 = 'T' + name_1[1:]
print( name_1,name_2)
a = '''
tfdbdjfuejgcfvcsnmc\
vtdfyukdnkwndhsufhb\
gdytgenfdmyjnfmlkf
'''
print(a)
# assessing elements
a = 'Hello, world'
print(a[0],a[8])

print(a[0:4])

#Concatination can be done using + symbol
#we can add two String easily using + symbol but we can't add integer and String simply by using + symbol
#we should use str() for concatination

my_string1 = 'navya'
my_string2 = 'shree'
print(my_string1 + my_string2)
print(my_string1,my_string2)

#Indexing, positive indexing
my_string1 = 'navyashree'
print(my_string1[0],my_string1[5],my_string1[8])

my_string2 = 'navya shree' #even space should be numbered and consider for indexing
print(my_string2[5],my_string2[-6])

#Indexing, negative indexing
print(my_string1[-1],my_string1[-6])

#Slicing  positive Slicing (syntax variable_name[start_index:end_index])

my_string1 = 'The Council of Water Sheep'
print(my_string1[0:11])

my_string2 = 'There were walking very slowly'
print(my_string2[0:])
print(my_string2[5:])
print(my_string2[:10])

#Slicing  negative Slicing (syntax variable_name[start_index:end_index])

my_string2 = 'There were walking very slowly'
print(my_string2[-6:])
print(my_string2[-10:0]) # we can't increment it to zero
print(my_string2[-10:])
print(my_string2[-15:-5])
print(my_string2[:])

#step index --> which is to skip the characters (syntax-> variable_name[start_index:stop_index:step_index])
my_string2 = 'There were walking very slowly'
print(my_string2[0:5:1])
print(my_string2[0::2])
print(my_string2[0:15:3])
print(my_string2[::2])
print(my_string2[::1])

#Reversing of String
my_string2 = 'There were walking very slowly'
print(my_string2[::-1])
print(my_string2[-10::-1])


# String methods, no arrguments
# upper()
my_string2 = 'navya'
print(my_string2.upper())

#lower(), (also have another method called casefold() which convert string to lowercase)
my_string2 = 'NAVYA'
print(my_string2.lower())

#title()
my_string1 = 'The Council of Water Sheep'
print(my_string1.title())

#capitalise()
my_string1 = 'The Council of Water Sheep'
print(my_string1.capitalize())

# String methods, with arguments
# split()--> it converts the string into list, it takes two arguments one is 'seperator' another is 'maxsplit'
my_string1 = 'The Council of Water Sheep'
print(my_string1.split())
print(my_string1.split('e'))
print(my_string1.split('e',2))
print(my_string1.split('e',3))
print(my_string1.split('a'))
print(my_string1.split('a',1))
print(my_string1.split('a',2))

#partition() --> it converts the string into tuple (syntax--> variable_name.partition('value')

my_string1 = 'The Council of Water Sheep'
print(my_string1.partition('Council'))
print(my_string1.partition('of'))

#join()
my_string1 =' '.join(['The', 'council', 'of', 'water', 'sheep'])
print(my_string1)
my_string1 ='x'.join(['The', 'council', 'of', 'water', 'sheep'])
print(my_string1)

# replace()--> it is to replace a string by another string
my_string1 = 'The Council of Water Sheep'.replace('Sheep','Goat')
print(my_string1)
print('The Council of Water Sheep'.replace('Sheep','Goat'))

#strip()--> it removes leading and trailing whitespaces
my_string1 = 'The Council of Water Sheep' .strip('The')
print(my_string1)
print('The Council of Water Sheep' .strip('The'))

#startswith()/endswith() --> returs boolen
print('The Council of Water Sheep' .startswith('The Council'))
print('The Council of Water Sheep'.endswith('Water'))

#count()--> it refers to how many times a specified value appers in a string
#syntax--> .count(value, starting position, ending position)

print('The Council Council of Water Sheep'.count("Council",4))

#find(),index()--> they return the first occurance of a specified value
#find() returns -1 if there is no value, index() gives error if thereis no value

#format()
my_string1 = "My name is {},I'm {}"
print(my_string1.format('navya',24))

my_string1 = "My name is {fname},I'm {age}"
print(my_string1.format(fname='divya',age=22))

my_string1 = "My name is {0},I'm {1}"
print(my_string1.format('John',20))

#center()--> syntax center(length,character) character is optional
my_string1 = 'navya'
print(my_string1.center(10))
print(my_string1.center(10,'G'))

#isalnum()--> returns true if all the characters in string are alphanumeric
my_string1 = 'navya12'
print(my_string1.isalnum())

#isalpha()--> returns true if all the character is alphabets
my_string1 = 'navya'
print(my_string1.isalpha())

my_string1 = 'navya12'
print(my_string1.isalpha())

#isascii()--> returns true if all the character is ascii

my_string1 = 'navya12'
print(my_string1.isascii())

#isdigit()--> returns true if all the character is digit

my_string1 = 'navya12'
print(my_string1.isdigit())

my_string1 = '1244578'
print(my_string1.isdigit())

#isdecimal()--> returns true if all the character is decimal
my_string1 = '1244578'
print(my_string1.isdecimal())

#islower()
my_string1 = 'navya'
print(my_string1.islower())

#isnumeric()
my_string1 = 'navya'
print(my_string1.isnumeric())

#isprintable()
my_string1 = 'Hello!\n Are you #1?'
print(my_string1.isprintable())

my_string1 = 'Hello! world'
print(my_string1.isprintable())

#isspace()
my_string1 = 'Hello'
print(my_string1.isspace())

my_string1 = ' '
print(my_string1.isspace())

#isupper()
my_string1 = 'NAVYA'
print(my_string1.isupper())

#ljust()--> returns left align string, rjust()--> returns right align string
my_string1 = 'navya'
print(my_string1.ljust(10))

my_string1 = 'navya'
print(my_string1.ljust(10,'G'))










































