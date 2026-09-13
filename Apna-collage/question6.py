# num1 =int(input("enter first number: "))
# num2 =int(input("enter second number: "))
# sum = num1 + num2   
# print("the sum of", num1, "and", num2, "is", sum)
#why this code give error
a = input()
b = input()
print(a + b)
#because input function take input as string by default so when we add two strings it concatenates them
#and we have to add the no not concatenate them so we have to convert the input to int or float
#correct code is a =int(input())
# b =int(input())