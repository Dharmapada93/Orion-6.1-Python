# Write a program to create a user-defined exception.
# class MyError(Exception):
#     pass
# raise MyError("This is a user-defined exception")

# raise Exception("This is a custom exception")

# Write a program to create a list of prime numbers between 1 and 100.

# primeNumbers=[]

# for n in range(2,101):
#     for i in range(2, n):
#         if n % i ==0:
#             break
#     else:
#         primeNumbers.append(n)
        
# print(primeNumbers)

# Write a program to handle file also handle if the file is not found.

# try:
#     with open('Python\example.txt', 'r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found")

import os
# if os.path.exists('Python\example.txt'):
#     with open('Python\example.txt', 'r') as f:
#         content = f.read()
#         print(content)
# else:
#     print("File not found")

# if os.path.exists('Python\example.txt'):
#    os.remove('Python\example.txt')
#    print("File deleted")
# else:
#     print("File not found")

os.rename('Python\example.txt', 'Python\example1.txt')

# l1 = [1,2,3,6,7,2,10,5,8,9]
# # l1.sort(reverse=True)
# l1.sort()
# print(l1[-2])