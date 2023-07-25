# An exception is a event ,which occurs during the execution of a program that stops the normal flow of program
# syntax
# try:
#   <statement which causes exception>
# except:
#   <solution for exception>
# else:
#   <statement> ---> else statement occurs after execution of try statement
# finally:
#   <statement> ---> finally block execute even though exception occurs or not

# Zero division error
def div_num(x, y):
    try:
        z=x%y
        print(z)
    except Exception:
        print("Zero division error")
    finally:
        print('Sucessfull')
div_num(10, 0)

# Index error
my_list = [1, 2, 3, 4, 5, 6]
def example(my_list):
    try:
        x = my_list[6]
        print(x)
    except Exception:
        print("Index error")
example(my_list)

# Name error
def name_error():
    try:
        x
        print(x)
    except Exception:
        print("sorry!,variable should be initialize ")
name_error();

def demo():
    try:
        even_numbers = [2, 4, 6, 8]
        print(even_numbers[5])
    except ZeroDivisionError:
        print("Denominater cannot be 0.")
    except IndexError:
        print("Index out of bound")
    finally:
        print("Exception handeled sucessfully")
demo()

# try with else statement
def demo2():
    try:
        number = int(input("Enter number:"))
        assert number%2==0
    except Exception:
        print("Not a even number")
    else:
        reciprocal = 1/number
        print(reciprocal)
demo2()





