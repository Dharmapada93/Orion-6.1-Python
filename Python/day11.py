def print_something():
    print("hello world")

# print_something()

def add(a, b):
    return a + b

# print(add(10,20))

def devide(a,b):
    return a / b

# print(devide(10,5))
# print(devide(10,0))

# Exception Handling
# try:
#     statement
# except:
#     statement

# try: 
#     print(devide(10,0))
# except:
#     print("You cannot divide a number by zero")

# print(add(10,20))
# print_something()

# try:
#     print(devide(10,0))
# except ZeroDivisionError:
#     print("You cannot divide a number by zero")

# try:
#     print(devide(10,0))
# except Exception as e:
#     print(e)
#     print("You cannot divide a number by zero")

# try:
#     a = int(input("Enter a number: "))
#     print(10/a)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
# except ZeroDivisionError:
#     print("You cannot divide a number by zero.")   

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a/b
# except ZeroDivisionError:
#     print("You cannot divide a number by zero.")
# else:
#     print(f"The result is {result}")    

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a/b
#     print(f"The result is {result}")
# except ZeroDivisionError:
#     print("You cannot divide a number by zero.")
# finally:
#     print("Execution completed.")     

age = int(input("Enter your age: "))

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as ve:
    print(ve)
else:
    print(f"Your age is {age}")