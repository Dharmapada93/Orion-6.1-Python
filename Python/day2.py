# Boolean Types
a = True
b = False
# print(type(a))
# print(type(b))
# print(a)
# print(b)

# Sequence Types
# String
s = "Hello"
# print(s)
# print(type(s))
# print(s[0])  # H
# print(s[4])  # o

# List
lst = [1, 2, 3, 4, 5.5, "Python", True]
# print(lst)
# print(lst[5])
# print(type(lst))

# Tuple
tup = (1, 2, 3, 4, 5.5, "Python", True)
# print(tup)
# print(tup[4])
# print(type(tup))

# Set
set1 = {1, 2,2,2,2,1,1,2,3,4,4, 3, 4, 5.5, "Python", True}
# print(set1)
# print(type(set1))
# print(set1[0])  # Error: Set does not support indexing

# Mapping Types
# Dictionary
student = {
    "name": "John Doe",
    "age": 21,
    "is_enrolled": True,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    }
}
# print(student)
# print(type(student))
# print(student["courses"][2])
# print(student['address']['city'])

# None Type
n = None
# print(n)
# print(type(n))

# Operators
# Arithmetic Operators
# a=10
# b=4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)

# Assignment Operator
# a = 20
# print(a)
# a+=5 # a = a +5
# print(a)
# a -= 10 # a = a - 10
# print(a) #10
# a *= 2 # a = a * 2
# print(a)
# a /=3  # a = a / 3
# print(a)
# a //= 2 # a = a // 2
# print(a)
# a %= 3 # a = a % 3
# print(a)
# a **=2
# print(a)

b = 15
b -=3
b*=2
b+=3
b//=2
b+=3
b*=3
print(b)