# try:
#     num=int(input("enter a no "))
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# except ValueError:
#     print("invalid num")

#question no 2
# try:
#     num=int(input("enter a no :"))
#     if num>0:
#         print("positive no")
#     elif num<0:
#         print("negative no")
#     elif num==0:
#         print("zero")
# except ValueError:
#    print("invalid value")

#questionno3
# n = int(input("Enter n: "))
# for i in range(1, n+1):
#     print(i, end=" ")

#questionno 4
# n = int(input("Enter n: "))
# for i in range(n, 0, -1):
#     print(i, end=" ")

#question no 5
# sum = 0
# num = int(input("Enter num: "))
# for i in range(1, num + 1):
#     sum = sum + i   
# print("The sum of first n natural numbers is", sum)

# #method 2
# num = int(input("Enter num: "))
# sum = num * (num + 1) // 2
# print("The sum of first n natural numbers is", sum)

#question no 6
# try:
#     num=int(input("enter a no :"))
#     if num<0:
#         print("factorial not posible :")
#     else:
#         fact=1
#         for i in range (1,num+1):
#             fact=fact*i
#         print("factorial is ",fact)
# except ValueError:
#     print("invalid no")

#question no 7
# num=int(input("enter a number :"))
# if num%1==1 and num%num==0:
#     print("prime no")
# else:
#     print("not a prime no")

#question no 8
# num = int(input("Enter any number to reverse: "))
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print("Reversed number is:", rev)


#method 2
# num = input("Enter a number: ")
# rev = num[::-1]
# print("Reversed number is:", rev)

#question no 9
# num=int(input("Enter number to check palindrome :"))
# original=num
# rev=0

# while num > 0:
#     digit=num%10
#     rev=rev*10+num
#     num=num//10

# if original==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

#method 2
# num=(input("enter a no to check palindrome"))
# if num==num[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#question no 10 
# num = int(input("Enter num to count digits: "))
# original = num
# count = 0

# while num > 0:
#     count += 1
#     num //= 10
# print("Total digits:", count)


#question no 11
# num=int(input("enter a num"))
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)

#using while loop
# num = int(input("enter num: "))
# i = 1
# while i <= 10:
#     print(num, "x", i, "=", i * num)
#     i += 1

# question no 12
# for i in range(1,101):
#     if i%2!=0:
#         continue
#     print("even no",i)

#using input
# num=int(input("enter num"))
# for num in range(1,num):
#     if num%2!=0:
#         continue
#     print("even no",num)

#using while 
# num=int(input("enter any no :"))
# i=1
# while i<=num:
#     if i%2!=0:
#         i += 1
#         continue
#     print("even no", i)
#     i +=1

#question no 13
# for i in range(1,100):
#     if i%2==0:
#         continue
#     print(i)


# num=int(input("enter any no"))
# for num in range(1,num):
#     if num%2==0:
#         continue
#     print(num)

# num =int(input("enter any no"))
# i=1
# while i<=num:
#     if i%2==0:
#         i +=1
#         continue 
#     print(i)
#     i +=1

#question no 14
# num = int(input("Enter a number to find the sum: "))

# if num < 0:
#     print("Please enter a positive number.")
# else:
#     total = 0
#     for i in range(1, num + 1):
#         total += i

#     print("Sum is:", total)

#using while 
# num=int(input("enter any num "))

# if num<0:
#     print("enter positive no")
# else:
#     total=0
#     i=1
#     while i<=num:
#         total += i
#         i += 1

#     print("sum is",total)

#question no 15
# num=int(input("enter a num"))
# total=0
# for i in range(1,num):
#     if i%2!=0:
#         continue
#     total=total+i
# print(total)

#using while 
# num=int(input("enter num :"))
# total=0
# i=1
# while i<=num:
#     if i%2!=0:
#         total=total+i
#     i += 1
    
# print(total)

#question no 16
# a=int(input("enter num a"))
# b=int(input("enter num b"))
# c=int(input("enter num c"))

# if a>b and a>c:
#     print("a is biggest")
# elif b>a and b>c:
#     print("b is biggest")
# else:
#     print("c is biggest")

#question no 16
# for i in range(1,5):
#     print("*"*i)

# n=int(input("enter no of rows"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# n=int(input("enter no of outer loop"))
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# n=6
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

