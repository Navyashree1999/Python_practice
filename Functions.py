# functions --> set of instructions or block of which is to perform some task
'''
syntax --> def function_name(arguments):
            statement
            return(optional)
'''

def demo():
    pass

# function calling
demo()

# function can be with arguments and without arguments
# functions without arguments
def greet():
    print('Hi, good morning')

greet()

# function with arguments
'''
types of arguments 
1. Positional arguments
2. Keyword arguments
3. Arbitrary arguments(*args)
4. keyword arguments(**kwargs)
'''
# positional arguments
def sum(n1,n2):
    sum = n1+n2
    return sum

result = sum(10,20)
print(result)

def sum_sub(n1,n2):
    sum=n1+n2
    sub=n1-n2
    return sum,sub

result = sum_sub(10,20)
print(result)
print('\n')

num=[4,5,6,7,8,3]
def max_num(num):
    max = num[0]
    for i in range(1,len(num)):
        if num[i] > max:
            max = num[i]
    print('maximum value is',max)
max_num(num)

# with return type
def max_num(num):
    max = num[0]
    for i in range(1,len(num)):
        if num[i] > max:
            max = num[i]
    return max
print(max_num(num))

# function with keyword arguments
def person_name(fname, mname, lname):
    name=fname+mname+" "+lname
    return name

result = person_name(mname='shree', fname='Navya', lname='GM')
print('The name of Person:',result)

'''def person_name(fname,lname):
    name=fname+lname
    return name

result = person_name(fname='Navya')
print('The name of Person:',result)'''

# function with Arbitrary arguments

'''def name_per(*name):
    print('name of person is:',name[5])
name_per('navya','divya','appu')---> when we run this we will get tuple index out of range'''

def name_per(*name):
    print('name of person is:',name[2])
name_per('navya','divya','appu')

# To over come arbitrary arguments disadvantages we kwargs
def name_per(**name):
    print('name of person is:', name['lname'])
name_per(fname='navya', lname='shree')

# default argument
def my_functon(name='navya'):
    print('name of the person:',name)
my_functon(name='Divya')

print('\n')
# sum of all numbers in a list
num=[8, 2, 3, 0, 7]
def sum_num(num):
    sum=0
    for i in range(0, len(num)):
        sum+=num[i]
    return sum
print(sum_num(num))

# multiply all numbers in a list
num = [8, 2, 3, -1, 7]
def mul_num(num):
    mult=1
    for i in num:
        mult*=i
    return mult
print(mul_num(num))

# reverse a string
my_string = "1234abcd"
def reverse_str(my_string):
    print(my_string[::-1])
reverse_str(my_string)
print('\n')

# another method
my_string = "1234abcd"
def reverse_str(my_string):
    rev_str = ''
    index = len(my_string)
    while index > 0:
        rev_str += my_string[index-1]
        index -= 1
    return rev_str
print(reverse_str(my_string))

def test_range(n):
    if n in range(1,10):
        print('%s is in the range'%str(n))
    else:
        print('%s is not present in the range')
test_range(7)

# count number of upper and lowercase number
my_string = 'The quick Brow Fox'
def up_low(my_string):
    count1=0
    count2 = 0
    index=my_string[0]
    for i in my_string:
        if i.isupper():
            count1+=1
        elif i.islower():
            count2+=1
        else:
            pass
    print('Original string :', my_string)
    print('Number of uppercase character:',count1)
    print('Number of lowercase character:', count2)
up_low(my_string)

my_list = [1, 2, 3, 3, 4, 5]
def unique_list(my_list):
    x =[]
    for i in my_list:
        if i not in x:
            x.append(i)
    return x
print(unique_list(my_list))

num = 15
def prime_num(num):
    if num==1:
        print("%s is not a prime number:"%str(num))
    elif num==2:
        print("%s is prime number:" % str(num))
    else:
        for x in range(2,num):
            if (num % x==0):
                print("%s is not a prime number:" % str(num))
        else:
            print("%s is prime number:" % str(num))

prime_num(num)

# even number or not
my_list = [1, 2, 3, 4, 5, 6, 7, 8,9]
def even_num(my_list):
    my_list2 = []
    for i in my_list:
        if i % 2==0:
            my_list2.append(i)
    return my_list2
print(even_num(my_list))

# perfect number or not
def perfect_num(num):
    sum=0
    num = int(input("enter number: "))
    for i in range(1,num):
        if num % i==0:
            sum+=i
    return sum==num
print(perfect_num(num))

# palandrome or not
my_string1 = 'madam'
def paladrome(my_string1):
    my_string2 =my_string[::-1]
    if my_string1==my_string2:
        print("%s is a palandrome"%str('madam'))
    else:
        print("%s is not a palandrome"%str('madam'))

paladrome(my_string1)
















