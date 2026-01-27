# def calculator(num1,num2):
#     if num1 + num2:
#         return(f"add:{num1+num2}")   
#     if num1 - num2:
#         return(f"sub:{num1-num2}")
#     if num1 * num2:
#         return(f"mul:{num1*num2}")
#     if num2!=0:
#         return(num1 /num2)
#     else:
#         return("error!Division by zero'")
# obj=calculator(5,4)
# print(obj)


# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = input("Enter an operator (+, -, *, /): ")

# def calculator(num1, num2, op):
#     if c == '+':
#         print(a+b)
#     elif c == '-':
#         print(a-b)
#     elif c == '*':
#         print(a*b)
#     elif c == '/':
#         print(a/b)
#     else:
#         print("Invalid operator")

# calculator(a, b, c)


# file = open('example.txt', 'r')
# print(file.read())
# content = file.read()
# print(content)

# file.close()

with open('PracticeSet1.txt', 'r') as f:
    content = f.readline(20)
    print(content)