# list1 =[1,2,3,4,5,]
# print(list1[0],list1[4])

nums =[10,20,30,40,50]
total =0
for i in nums:
    total += i
print("Total:", total)
# list2 =[]
# list2.append(int(input("Enter a number: ")))
# list2.append(int(input("Enter 2nd number: ")))
# list2.append(int(input("Enter 3rd number: ")))
# list2.append(int(input("Enter 4th number: ")))
# list2.append(int(input("Enter 5th number: ")))
# print("List elements are:",list2)

list3 = [5, 10, 15, 20, 25]
even = [i for i in list3 if i % 2 == 0]
odd = [i for i in list3 if i % 2 != 0]
print("Even numbers:", even)
print("Odd numbers:", odd)
