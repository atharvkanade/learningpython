"""Swapping of two number without using third varible"""
a = int(input("Enter first number :"))
b = int(input("Enter first number :"))

print("Before swappig value of a is :", a)
print("Before swappig value of b is :", b)

a = a + b
b = a - b
a = a - b

print("After swappig value of a is :", a)
print("After swappig value of b is :", b)
