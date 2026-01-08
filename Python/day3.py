# Comparision Operators
a = 10
b = 20
c = 10
# print(a==b)
# print(a==c)
# print(a!=b)
# print(a!=c)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a>=c)
# print(a<=b)
# print(a<=c)

# Logical operators
x = True
y = False
z = True
# print(x and y)
# print(x and z)
# print(x or y)
# print(x or z)
# print(y or y)
# print(not x)
# print(not y)
# print(not z)

# Identity Operators
a = 10
b = 20
c = a
# print(a is b)
# print(a is c)
# print(a is not b)
# print(a is not c)

# Membership Operators
lst = [1, 2, 3, 4, 5]
# print(3 in lst)
# print(6 in lst)
# print(3 not in lst)
# print(6 not in lst)



# Conditional Statements
# if statement
# if condition:
#     statement

# age = 16
# if age>=18:
#     print("You are eligible to vote")

# if-else Statement
# if condition:
#     statements
# else:
#     statements

# age = 16
# if age>= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# if-elif-else statement
# age = 27
# if age < 18:
#     print("Your are kid")
# elif age < 30:
#     print("You are Adult")
# elif age < 60:
#     print("You are Senior Citizen")
# else:
#     print("You are old")


# 1. Write a program to check whether a number is positive, negative or zero.
# number=-9
# positive=number>0
# print(positive)
# negative=number<0
# print(negative)

# n = 0
# if n >0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# else:
#     print("Zero")

# 2. WAP to calculate area of a triangle
b = 10
h = 20
area = (h*b)/2
# print(area)

# 3. WAP to check whether a number is even or odd
num = 90
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4. WAP to check whether a year is leap year or not
year = 400

if (year %4 ==0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a leap year")