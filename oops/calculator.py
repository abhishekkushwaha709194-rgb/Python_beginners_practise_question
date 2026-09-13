class calulator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b!=0:
            return a/b
        return "invalid approach"
    
calc=calulator()

while True:
    print("1 Add\n 2 subtract\n 3 multiply\n 4 divide\n 5 exit\n ")
    
    choice=int(input("enter your choice :"))
    if choice == 5:
        print("Exit succesfull ")
        break 
    a=int(input("enter first number "))
    b=int(input("enter second number "))


    match choice:
            case 1:
                print("result",calc.add(a,b))
            case 2:
                print("result",calc.subtract(a,b))
            case 3:
                print("result",calc.multiply(a,b))
            case 4:
                print("result",calc.divide(a,b))
            case _:
                print("invalid choice ")