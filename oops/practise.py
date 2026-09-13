# class student:
#     name="Abhishek"
#     age=25
#     def show(self):
#         print(f"student name is {self.name} and his age is {self.age}")

# s1=student()
# s1.show()


# class car:
#     brand="tata"
#     model="sierra"
#     def brand1(self):
#         print(f"the car brand is {self.brand}")
#     def model1(self):
#         print(f"and the model is {self.model}")

# CAR=car()
# CAR.brand1()
# CAR.model1()


# class rectangle:
#     length=5
#     width=7

#     def area(self):
#         print(f"the rectangle length is {self.length} and width is {self.width}")
#         return self.length*self.width
        

# Area=rectangle()
# print(Area.area())

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area_circu(self):
#         print(f"the area of circle is {3.14*self.radius**2}cm^2")
#         print(f"the circumferance of circle is {2*3.14*self.radius}cm^2")

# circle=Circle(7)
# circle.area_circu()

# class Employee:

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def detail(self):
#         print(f"the name of the employee is {self.name} and the salary is {self.salary}")


# e1=Employee("bittu",300000)
# e2=Employee("Abhishek",40000)
# e1.detail()
# e2.detail()

class BankAccount:

    def __init__(self, ac_num, balance):
        self.ac_num = ac_num
        self.balance = balance

    def show_balance(self):
        print(f"Account balance is ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Deposit successful")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")

    def details(self):
        print(f"Account number: {self.ac_num}")
        print(f"Current balance: ₹{self.balance}")


# Object
customer1 = BankAccount(1111, 5000)

customer1.details()
customer1.deposit()
customer1.withdraw()
customer1.show_balance()