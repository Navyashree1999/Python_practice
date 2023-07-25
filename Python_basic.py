# check whether the number is even or not
def even_num():
    num = float(input("enter number:"))
    if num % 2==0:
        print("%s is a even number" %str(num))
    else:
        print("%s is odd number" % str(num))

# Python program to convert the temperature in degree centigrade to Fahrenheit

def cel_fah():
    c = int(input("enter temperature in degree celsius:"))
    f = (9/5*c)+32
    print("Temperature in Fahrenheit is: ", f)

#Python program to find out the average of a set of integers
def avg_num():
    i=0
    sum = 0
    count = int(input("Enter count of number:"))
    for i in range(count):
        num = float(input("Enter a number:"))
        sum+=num
    avg=sum/count
    print("The average is: ", avg)

#Python program to find the product of a set of real numbers
def real_num():
    product = 1
    count = int(input("Enter count of number:"))
    for i in range(count):
        real_num = float(input("Enter number:"))
        product*=real_num
    print('The product of real number:',product)

#Python program to find the circumference and area of a circle with a given radius
import math
def circum():
    radius = float(input("Enter radius of circle:"))
    circumference = 2*math.pi*radius
    print("Circumference of circle is:",circumference)

# 7. Python program to check whether the given integer is a multiple of 5
def mult_five():
    num = float(input("Enter number:"))
    if num % 5==0:
        print("%s is a multiple of 5"%str(num))
    else:
        print("%s is not a multiple of 5" % str(num))
#  Python program to check whether the given integer is a multiple of both 5 and 7
def mult_of():
    try:
        num = float(input("Enter number:"))
        if ((num % 5==0) and (num % 7==0)):
            print('%s is multiple of 5 and 7'%str(num))
        else:
            print('%s is not a multiple of 5 and 7' % str(num))
    except Exception:
        print("Value entered should not be string")

# 9. Python program to find the average of 10 numbers using while loop
def average_num():
    i=0
    z=10
    sum=0
    while i<z:
        num = float(input("Enter integer:"))
        sum+=num
        i+=1
    average=sum/z
    print("The average of numbers:",average)

#10. Python program to display the given integer in a reverse manner
def reverse_num():
    number =int(input(" enter integer"))
    rev = 0
    while number!=0:
        new_number = number % 10
        rev=(rev*10)+new_number
        number//=10
    print("Reverse o a given number:",rev)

#Python program to find the geometric mean of n numbers
import math
def geo_mean():
    count = int(input("Enter count of number"))
    product = 1
    for i in range(count):
        num = float(input("Enter number:"))
        product*=num
    geometric_mean=math.sqrt(product)
    print("Geometric mean of numbers:",geometric_mean)

#12. Python program to find the sum of the digits of an integer using a while loop
def sum_of():
    sum = 0
    num = float(input("Enter number:"))
    while num != 0:
        new_num = num%10
        sum+=new_num
        num//=10
    print("The sum of given digit :",sum)

#Python program to display all the multiples of 3 within the range 10 to 50
def mul_three():
    for i in range(10,50):
        if i % 3==0:
            print("multiple of 3 is :",i)

#14. Python program to display all integers within the range 100-200 whose sum of digits is an even number
def demo1():
    for i in range(100, 200):
        num = i
        sum = 0
        while num != 0:
            digit = num % 10
            sum = sum + digit
            num = num // 10
        if (sum % 2 == 0):
            print(i)

# 15. Python program to check whether the given integer is a prime number or not
def prime_num():
    number = int(input("enter number:"))
    if number==1:
        print("Not a prime number")
    elif number>1:
        for i in range(2,number):
            if number%i==0:
                print("Not a prime number")
                break
        else:
            print("It is a  prime number")


# 16. Python program to generate the prime numbers from 1 to N
def demo2():
    num = int(input("Enter range:"))
    for n in range(2,num):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)

# 17.python program to display the sum of n numbers in a list
def list_ex():
    numbers = []
    num = int(input("How many numbers:"))
    for i in range(num):
        sum = 0
        x = float(input("Enter number:"))
        numbers.append(x)
        sum+=numbers[i]
    print("sum of numbers:",sum)

# python program to find the odd numbers in an array
def array_odd():
    numbers = [8, 3, 1, 6, 2, 4, 5, 9]
    count = 0
    for i in numbers:
        if i%2!=0:
            count+=1
    print("The number of odd numbers in  a list:",count)

# 18. python program to find largest number in a list without using built in function
def large_num():
    numbers = [3, 8, 1, 7, 2, 9, 5, 4]
    max_num = numbers[0]
    position = 0
    for i in range(len(numbers)):
        if numbers[i]>max_num:
            max_num = numbers[i]
            position = i
    print("The largest element is ",max_num,"Which is found at position",position)

# 19. python program to insert a number to any position in a list
def insert_num():
    numbers = [3, 4, 1, 9, 6, 2, 8]
    digit = float(input("Enter number:"))
    numbers.insert(2,digit)
    print(numbers)

# 20 python program to delete an element from a list by index
def delete_num():
    numbers = [3, 4, 1, 9, 6, 2, 8]
    x = int(input("Enter the position of the element to be deleted:"))
    numbers.pop(x)
    print(numbers)








































