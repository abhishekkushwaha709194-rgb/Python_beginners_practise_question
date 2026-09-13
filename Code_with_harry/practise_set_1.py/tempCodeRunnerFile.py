n= int(input("Enter first number: "))
m= int(input("Enter second number: "))
if n > m:
    greater = n
else:
    greater = m
while True:
    if greater % n == 0 and greater % m == 0:
        lcm = greater
        break
    greater += 1
print("LCM is", lcm)
