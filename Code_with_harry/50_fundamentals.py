# a=int(input("enter a number :"))
# b=int(input("enter another number "))
# operator=input("enter any operator ")

# match operator:
#     case '+':
#         print("sum=",a+b)
#     case '-':
#         print("diffrence=",a-b)
#     case '*':
#         print("multiply =",a*b)
#     case '/':
#         print("division=",a/b)
#     case '':
#         print("invalid output")


# #swapping no without using third variable
# a=int(input("enter a "))
# b=int(input("enter b "))
# a=a+b
# b=a-b
# a=a-b
# print("a=",a, "b=",b)

# #celcious to farenheit
# celcious=int(input("enter temperature "))
# farenheit=(celcious*1.8)+32
# print(farenheit)

#square and cube 
# num=int(input("enter any number "))
# square=num**2
# cube=num**3
# print(square)
# print(cube)


#simple intrest 
# principle=int(input("enter principle amount "))
# rate=int(input("enter rate "))
# time=int(input("enter time period "))
# #SI= simple intrest
# SI=(principle*rate*time)/100
# print("simple intrest =",SI)

#checking f a no is even or odd
# def even_odd(num):
#     if num%2==0:
#         print("even no")
#     else:
#         print("odd no")

# while True:
#     num1=input("enter any number or enter quit to exit ")
#     if num1.lower()=="quit":
#         print("program stopped ")
#         break
#     else:
#         number=int(num1)
#         even_odd(number)

#checking if a number is positive negative or zero 
# def check_pos_neg_zero(num):
#     if num>0:
#         print("positive number ")
#     elif num<0:
#         print("negative number ")
#     else:
#         print("zero ")

# while True:
#    try:
#     num1=input("enter any number to check or q to quit ")
#     if num1=="q":
#         print("programmed stopped ")
#         break
#     else:
#         number=int(num1)
#         check_pos_neg_zero(number)
#    except ValueError:
#     print("invalid input")


#find the largest number amoung three 
# def largest(a, b, c):
#     if a >= b and a >= c:
#         print(a, "is the largest number")
#     elif b >= a and b >= c:
#         print(b, "is the largest number")
#     elif c >= a and c >= b:
#         print(c, "is the largest number")
#     else:
#         print("Some numbers are identical")

# while True:
#     a = input("Enter number a (or q to quit): ")
#     if a.lower() == "q":
#         print("Program stopped")
#         break
#     b = input("Enter number b: ")
#     c = input("Enter number c: ")

#     try:
#         a = int(a)
#         b = int(b)
#         c = int(c)
#         largest(a, b, c)
#     except ValueError:
#         print("Invalid input, please enter numbers only")

#check if a no is divide by both 3 and 5
# def check_divide(num):
#     if num%3==0 and num%5==0:
#         print("input number is divided by both 3 and 5")
#     else:
#         print("input number is not divide by both 3 and 5")

# while True:
#    try:
#     num1=input("enter any number (or q to exit )")
#     if num1=="q":
#         print("program stopped ")
#         break
#     else:
#         number=int(num1)
#         check_divide(number)
#    except ValueError:
#      print("invalid input")

# #check if a year is leap year or not 
# import calendar
# year=int(input("enter year"))
# print(calendar.isleap(year))

# Check if a person can vote (age ≥ 18 AND citizen).
# def adult(age):
#     if age >=18:
#         print("you can vote ")
#     else:
#         print("you can't vote ")
# while True:
#     age1=input("enter your age :(or quit to exit )")
#     if age1=="quit":
#         print("succesfully exit")
#         break
#     else:
#         age2=int(age1)
#         adult(age2)



# Check if a number is between 10 and 100.
# def check_between(num):
#     if num >=10 and num<=100:
#         print("number is in 10 and 100")
#     else:
#         print("no is not in between 10 and 100 ")

# while True:
#     num1=input("enter any no to check (or quit to exit )")
#     if num1=="quit":
#         print("succesfully exit ")
#         break
#     else:
#         number=int(num1)
#         check_between(number)

# Check if a number is not divisible by 7.
# def divisible_7(num):
#     if num%7==0:
#         print("entered no is divisible by 7")
#     else:
#         print("not divisible by 7 ")

# while True:
#     num=input("enter any number or quit to exit  ")
#     if num=="quit":
#         print("succesfully exit ")
#         break
#     else:
#         number=int(num)
#         divisible_7(number)

# Check if a student passes (marks ≥ 40).
# def marks(num):
#     if num>=40:
#         print("student passed the exam  ")
#     else:
#         print("fail ")
# while True:
#     mark=input("enter your marks (or quit to exit )")
#     if mark=="quit":
#         print("succesfully exit ")
#         break 
#     else:
#         marks1=int(mark)
#         marks(marks1)

# Check if a number is multiple of 2 OR 5
# def multi_check(num):
#     if num%2==0 and num%5==0:
#         print("entered number is divisible by both 2 and 5 ")
#     else:
#         print("not divisible by 2 and 5")
# while True:
#     num1=input("enter any number ( or quit for exit )")
#     if num1 =="quit":
#         print("succesfully exit ")
#         break
#     else:
#         number=int(num1)
#         multi_check(number)

# Print numbers from 1 to N.
# def loop1(num):
#     if num<0:
#         print("enter a positive number ")

#     else:
#         for i in range(1,num+1):
#             print(i)

# while True:
#     n=input("enter range (or type end to stop the program :)")
#     if n=="end":
#         print("programme stopped ")
#         break
#     else:
#         number=int(n)
#         loop1(number)


# def loop1(num):
#     if num>=0:
#      for i in range (0,num):
#         print(i)
#     else:
#        for i in range(0,num-1,-1):
#           print(i)
# while True:
#     n=input("enter range (or type end to stop the program :)")
#     if n=="end":
#         print("programme stopped ")
#         break
#     else:
#         number=int(n)
#         loop1(number)




# Print even odd  numbers from 1 to 100.
# def odd_even_range(num, choice):
#     if choice == "even":
#         for i in range(1, num+1):
#             if i % 2 == 0:
#                 print(i)

#     elif choice == "odd":
#         for i in range(1, num+1):
#             if i % 2 != 0:
#                 print(i)


# while True:
#     n = input("Enter range (or q to exit): ")

#     if n == "q":
#         print("Stopped")
#         break

#     choice = input("Type odd or even: ")

#     number = int(n)
#     odd_even_range(number, choice)

# Print multiplication table of a number.
# def table(num):
#     if num>0:
#      for i in range(1,11):
#         print(num*i)
#     else:
#        print("enter positive number ")
# n=int(input("enter a num for table "))
# table(n)

# Find sum of first N numbers.
# def sum_0f_n(num):
#     if num<=0:
#         print("enter positive number ")
#     else:
#         total=0
#         for i in range (1,num+1):
#             total +=i
#         print(total)
# while True:
#     n=input("enter your range for n number or type q to exit ")
#     if n=="q":
#         print("exit succesfull ")
#         break
#     else:
#         number=int(n)
#         sum_0f_n(number)


# Find factorial of a number.
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)


# while True:
#     n = input("Enter number (or q to exit): ")

#     if n == "q":
#         print("Program stopped")
#         break

#     number = int(n)
#     print("Factorial =", factorial(number))


# Reverse a number.
# def reverse(num):
#     rev = 0

#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10

#     return rev


# print(reverse(543))


# Count digits of a number.
# def count_digit(num):
#     count=0
#     while num!=0:
#         num=num//10
#         count +=1
#     print(count)

# count_digit(1234)



# Find sum of digits of a number.
# def sum_digit(num):
#     digit=0
#     rev=0
#     while num!=0:
#         rev=num%10
#         digit=digit+rev
#         num=num//10

#     return digit

# while True:
#     n=input("Enter number or q to exit ")
#     if n=='q':
#         print("stopped")
#         break
#     else:
#         number=int(n)
#         print(sum_digit(number))



# Check if a number is palindrome.
# def palindrome(num):
#     rev = 0
#     original = num
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10
#     if original == rev:
#         print("Entered number is a palindrome")
#     else:
#         print("Entered number is not a palindrome")

# while True:
#     n = input("Enter number or q to exit: ")
#     if n == "q":
#         print("Stopped")
#         break
#     else:
#         number = int(n)
#         palindrome(number)


# Print numbers from N to 1.
# def number(n):
#     while n>=0:
#         print(n)
#         n -=1

# number(7)

# Check if a number is prime.
# num = int(input("Enter a number: "))

# if num <= 1:
#     print(f"{num} is not a prime number.")
# else:
#     i = 2
#     is_prime = True
#     while i * i <= num:  
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1

#     if is_prime:
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")
        

# Print all prime numbers between 1 and N.
# n = int(input("Enter a number: "))

# num = 2

# while num <= n:
#     i = 2
#     is_prime = True

#     while i * i <= num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1

#     if is_prime:
#         print(num)

#     num += 1


# Print Fibonacci series up to N terms.
# def fibonacci(num):
#     if num<0:
#         print("enter a positive number ")

#     else:
#         a,b=0,1
#         for i in range(num):
#             print(a,end=' ')
#             next_val=a+b
#             a=b
#             b=next_val
#         print()
        

# while True:
#     n=input("enter number or q to exit ")
#     if n=='q':
#         print("stopped")
#         break
#     else:
#         number=int(n)
#         fibonacci(number)

# Check if number is Armstrong number.
# def armstrong(num):
#     if num <0:
#         print("enter positive number ")
#     else :
#         total=0
#         original=num
#         while num>0:
#             rev=num%10
#             total=total+rev**3
#             num=num//10
#     if original==total:
#         print("number is armstrong ")
#     else:
#         print("number is not armstrong ")

# while True:
#     n=input("enter number or q to exit ")
#     if n=="q":
#         print("stopped")
#         break
#     else:
#         number=int(n)
#         armstrong(number)

#armstrong number to n terms
# n = int(input("Enter a number: "))

# for num in range(1, n + 1):
#     temp = num
#     power = len(str(num))
#     total = 0

#     while temp > 0:
#         digit = temp % 10
#         total += digit ** power
#         temp //= 10

#     if total == num:
#         print(num)

# Find GCD of two numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD =", a)