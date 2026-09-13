age =20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

num =7
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

marks =55
if marks >= 90:
    grade ="A"
elif marks >= 80:
    grade ="B"
elif marks >= 70:
    grade ="C"
else:
    grade ="fail"
print(f"Your grade is {grade}.")

name ="admin"
if name == "admin":
    print('login successful')
else:
    print('login failed')

s ="python"
if 'y' in s:
    print("found")
else:
    print("not found")

s =""
if s:
    print("not empty")
else:
    print("empty string")

s ="hello"
if len(s)>3 and s[0] =="h":
    print("yes")
else:
    print("no")

s ="Python"
if s.lower() =="python":
    print("match")
else:
    print("no match")

name ="abhi"
age  =17
if name =="abhi" or age >=18:
    print("eligible")
else:
    print("not eligible")