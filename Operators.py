# Arithmetic operator
# addition(+)
a,b=10,20
c=a+b
print(c)

# subtraction(-)
a,b=10,20
c=a-b
print(c)
print(b-a)

# multiplication(*)

a,b=10,20
c=a*b
print(c)

# division (/)
a,b=10,20
c=b/a
print(c)

# modulus (%)
a,b=10,20
c=b%a
print(c)

# float division (//)
a,b=10,20
c=b//a
print(c)

a,b=5,3
c=a//b
print(c)

# exponent (**)
a,b=5,3
c=a**b
print(c)

# Assignment operator
# =
a=10
b=20
c=b
print(a,b,c)

# +=
x=5
x+=2 # x=x+2
print(x)

# _=
x=5
x-=2 # x=x-2
print(x)

# *=
x=5
x*=2 # x=x*2
print(x)

# /=
x=5
x/=2 # x=x/2
print(x)

# %=
x=5
x%=2 # x=x%2
print(x)

# //=
x=5
x//=2 # x=x//2
print(x)

# **=
x=5
x**=2 # x=x**2
print(x)

# Relational/ Comparison operator
# equals(==)
a,b=5,3
print(a==b)

# greaterthan >
a,b=5,3
print(a>b)

# greaterthan or equals to (>=)
a,b=5,3
print(a>=b)

# lessthan <
a,b=5,3
print(a<b)

# lessthan or equal to <=

a,b=5,3
print(a<b)

# not equals !=

a,b=5,3
print(a!=b)

# logical Operator
# and
a,b,c=5,3,10
print(a>b and a<c )

print(a>b and a>c)

# or
a,b,c=5,3,10
print(a>b or a<c )

print(a>b or a>c)

# not
a=7
a=not(0)
print(a)

print("\n")

# identity operators
# is returns true if both variable are the same object
# is not returns true if both objects are not true

x=2
y=3

print(x is y)
print(x==y)
print(x is not y)
y=x
print(x is y)

print('\n')

x=['navya' ,'shree']
y=['navya' ,'shree']

print(x is y)

# membership operator
# in --> return true if a sequence with a specified value is present in the object
# not in --> return true if a sequence with a specified value is not present in the object

x =['apple','banana']
print('banana' in x)

print('grapes' in x)



















