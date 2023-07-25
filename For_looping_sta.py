# looping statements
# For loop
# Simple for loop

x = [1,2,3,4,5,6,7,8,9,10]
for i in x:
    print(i)
print('\n')

x = list(range(1,20))
for x in x:
    print(x)

print('\n')

x = ['apple', 'mango', 'banana', 'grapes']
for i in x:
    print(i)
print('\n')

for i in 'banana':
    print(i)

print('\n')

for i in range(3):
    print(i)
print("\n")

my_string = "Hello, World!"
reversed_string = ""
for char in my_string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)
print("\n")

# for loop with if condition statement
# if the given number is even number print it

num = list(range(1,20))
for i in num:
    if(i%2==0):
        print(i)
print('\n')

x = [1,2,3,4,5,6,7,8,9,10]
sum=0
for i in x:
    sum=sum+i
print(sum)
print('\n')

# finding a specific character in a given string
name='navya'
chr='v'
for i in name:
    if i==chr:
        print('Character found')
        break
else:
    print('Character not found')

# finding maximum number
my_list = [1,7,48,9,3,0]
max_num = my_list[0]
for num in my_list:
    if num>max_num:
        max_num = num
print("The maximum number is:", max_num)

# counting a number of vowels  present in a given string
my_string = 'Hello, World'
vowels = 'aeiouAEIOU'
count=0
for char in my_string:
    if char in vowels:
        count+=1
print('number of vowels',count )

# looping using nested for loop

for i in range(1,6):
    for j in range(1,6):
        product=i*j
        print(product, end='\t')
    print()

for i in range(5):
    for j in range(i):
        print("*", end=" ")
    print()

chr = 'a'
for i in 'banana':
    if i==chr:
        continue
    print(i)

for i in range(6):
    if i==3:
        break
    print(i)
else:
    print('sucessfull')




























