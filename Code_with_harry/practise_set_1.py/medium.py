# Check Armstrong number.
# Print Fibonacci series up to N terms.
# Find GCD of two numbers.
# Find LCM of two numbers.
# Check if a number is perfect number.
# Find second largest number (without list, only variables).
# Count frequency of a digit in a number.

#check armstrong number
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if num == sum:
#     print(num, "is an Armstrong number")
# else:    
#     print(num, "is not an Armstrong number")

# #fibonacci series
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# count = 0
# if n <= 0:
#     print("Please enter a positive integer.")
# elif n == 1:
#     print("Fibonacci sequence up to", n, "term:")
#     print(a)
# else:
#     print("Fibonacci sequence up to", n, "terms:")
#     while count < n:
#         print(a, end=' ')
#         a, b = b, a + b
#         count += 1

# #gcd of two numbers
# n= int(input("Enter first number: "))
# m= int(input("Enter second number: "))
# while m:
# 	temp = m
# 	m = n % m
# 	n = temp
# print("GCD is", n)

# #lcm of two numbers
# n= int(input("Enter first number: "))
# m= int(input("Enter second number: "))
# if n > m:
#     greater = n
# else:
#     greater = m
# while True:
#     if greater % n == 0 and greater % m == 0:
#         lcm = greater
#         break
#     greater += 1
# print("LCM is", lcm)

# #perfect number
# num = int(input("Enter a number: "))
# divisor_sum = 0
# for i in range(1, num):
#     if num % i == 0:
#         divisor_sum += i
# if divisor_sum == num:
#     print(num, "is a perfect number")
# else:
#     print(num, "is not a perfect number")
    
#second largest number
# n = int(input("Enter the number of elements: "))
# first = second = float('-inf')
# for i in range(n):
#     num = int(input("Enter a number: "))
#     if num > first:
#         second = first
#         first = num
#     elif first > num > second:
#         second = num
# if second == float('-inf'):
#     print("There is no second largest number.")
# else:
#     print("The second largest number is:", second)

#frequency of a digit in a number
# num = int(input("Enter a number: "))
# digit = int(input("Enter a digit to count: "))
# count = 0
# while num > 0:
#     last_digit = num % 10
#     if last_digit == digit:
#         count += 1
#     num //= 10
# print("The digit", digit, "appears", count, "times in the number.")

