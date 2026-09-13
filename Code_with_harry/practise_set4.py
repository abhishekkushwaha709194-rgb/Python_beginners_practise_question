# fruits = ["apple", "banana", "cherry"] 
# print(fruits[0])
# fruits[1]="orange"
# print(fruits)
# print(len(fruits))

# num=[1,2,3,4,5,6,7,8,9,10]
# print(num[0:3])
# print(num[-3:])

# numbers = [5, 2, 9, 1, 7]
# numbers.append(10)
# numbers.sort()
# print(numbers)
# numbers.remove(2)
# print(numbers)

# names = ["Alice", "Bob", "Charlie"]
# names.insert(1,"david")
# print(names)

# coordinates = (10, 20)
# print(coordinates)

# # Convert tuple into list
# list1 = list(coordinates)

# # Modify the first element
# list1[0] = 50

# # Convert list back into tuple
# coordinates = tuple(list1)

# print(list1, type(list1))   # Shows the modified list
# print(coordinates, type(coordinates))  # Shows the modified tuple

# my_set = {1, 2, 3, 3, 4}
# my_set.add(5)
# my_set.remove(2)
# print(my_set)
# if 4 in my_set:
#     print("4 is present in the set")
# else:
#     print("4 is not present in the set")


# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# student = {"name": "John", "age": 20, "grade": "A"}
# print(student["name"])
# student["grade"]="A+"
# print(student)
# student["city"]="delhi"
# print(student)

#Write a program that takes a list of numbers and removes all duplicates using  a set.
# numbers=[1,3,5,67,76,44,33,44,0]
# unique_numbers=list(set(numbers))
# unique_numbers1=set(numbers)
# print(type(unique_numbers1))
# print("original list",numbers,type(numbers))
# print("list with unique numbers",unique_numbers,type(unique_numbers))

# products = {
#     "Laptop": 75000,
#     "Phone": 50000,
#     "Tablet": 30000,
#     "Monitor": 20000
# }

# highest_product = ""
# highest_price = 0

# for product in products:
#     if products[product] > highest_price:
#         highest_price = products[product]
#         highest_product = product

# print("Products:", products)
# print("Product with highest price:", highest_product)
# print("Price:", highest_price)


# dict1={"hello" : 21, "abhishek": 21}
# print(type(dict1))
# dict2={"name" : "abhishek", "age" : 21}

# merge=dict1 | dict2
# print(merge)