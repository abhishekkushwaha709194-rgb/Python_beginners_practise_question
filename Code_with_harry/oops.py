# class Car:
#     def drive(self):
#         print("you are driving")

# car1 = Car()
# car1.drive()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def detail(self):
#         print(f"The person {self.name} age is {self.age}")

# # Create an object
# person1 = Person("amit", 25)

# # Call the method
# person1.detail()

class Animal:
    def __init__(self, sound):
        self.sound = sound
        print("Some sound")

class Dog(Animal):
    def __init__(self, sound):
        super().__init__(sound)  # Call parent constructor

    def bark(self):
        print(f"The dog says: {self.sound}")

# Example usage
dog1 = Dog("Woof!")
dog1.bark()