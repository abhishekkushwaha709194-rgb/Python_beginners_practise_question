# def greet():
#     print("hello, python learner")
#     return 
# greet()

# def square(num):
#     a=num**2
#     print(a)
#     return a
# square(3)

# def full_name(first,last):
#     return f"{first} {last}"

# print(full_name("abhishek","kushwaha"))

# def area(length,width=10):
#     '''area of a rectangle'''
#     return length*width

# print(area(10,20))

# add = lambda x, y: x+y
# print(add(4,5))

# square =lambda x:x*x
# list1=[1,2,3,4,5,6,7,8,9]

# print(list(map(square,list1)))

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return factorial(n-1)*n

# print(factorial(5))

# def sum_of_digits(n):
#     if n==0:
#         return 0
#     return n%10 + sum_of_digits(n//10)

# print(sum_of_digits(6543))

# import math
# print(math.sqrt(18))
# print(math.radians(90))

# import requests
# response = requests.get("https://api.github.com")
# print(response.json())

# def increment():
#     counter=0
#     counter+=1
#     print(counter)

# increment()
# increment()
# increment()
# increment()
# increment()


# def multiply(a, b):
#     """Multiply two numbers and return the result."""
#     return a * b

# print(multiply(4, 6))
# print(multiply.__doc__)


# def fibonacci(n):
#     if n==0 or n==1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))

# def multiply(a,b):
#     if b==0:
#         return "cannot divide"
#     return a*b

# print(multiply(4,7))

# import my_utils
# print(my_utils.is_even(4))
# print(my_utils.is_even(7))
