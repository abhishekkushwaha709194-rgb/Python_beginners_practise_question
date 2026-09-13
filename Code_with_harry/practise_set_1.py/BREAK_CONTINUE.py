# input until num is 0
# while True:
#     n = int(input("Enter a number: "))
    
#     if n == 0:
#         print("Guessed right")
#         break
#     else:
#         print("Enter number again")

#number gussing game 
# secret = 5 

# while True:
#     guess = int(input("Guess the number: "))

#     if guess == secret:
#         print("Congratulations! You guessed it right.")
#         break
#     elif guess > secret:
#         print("Too high! Try again.")
#     else:
#         print("Too low! Try again.")

#skip multiple of 3
# n=int(input("enter range "))
# for n in range(1,n):
#     if n%3==0:
#         continue
#     print(n)

#stop when no is divisible by 7
# while True:
#     n=int(input("enter a number :"))
#     if n%7==0:
#         print("no is divisible by 7")
#         break
#     else:
#         print("enter Num again :")

#calculator using match case
# a=float(input("enter a number :"))
# b=float(input("enter a number :"))
# op=input("choose operators +,-,/,*")

# match op:
# 	case "+":
# 		print(a + b)
# 	case "-":
# 		print(a - b)
# 	case "*":
# 		print(a * b)
# 	case "/":
# 		print(a / b)
# 	case _:
# 		print("Invalid operator")
    

#atm simulator 
balance = 5000

print("1. Check balance")
print("2. Withdraw balance")
print("3. Deposit")
print("4. Exit")

while True:
    n = int(input("Enter your choice: "))

    if n == 1:
        print("Current balance:", balance)

    elif n == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Withdrawal successful")
            print("Current balance:", balance)

    elif n == 3:
        deposit = int(input("Enter amount to deposit: "))
        balance += deposit
        print("Deposit successful")
        print("Current balance:", balance)

    elif n == 4:
        print("Thank you!")
        break

    else:
        print("Meowdharchod")