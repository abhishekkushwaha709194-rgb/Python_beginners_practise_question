# nums =[1,2,3,4,6]
# nums.reverse()
# print("Reversed list:", nums)

# num =[34,98,0,23,44]
# if num[0] > num[1] and num[0] > num[2] and num[0] > num[3] and num[0] > num[4]:
#     largest = num[0]
# elif num[1] > num[0] and num[1] > num[2] and num[1] > num[3] and num[1] > num[4]:
#     largest = num[1]
# elif num[2] > num[0] and num[2] > num[1] and num[2] > num[3] and num[2] > num[4]:
#     largest = num[2]    
# elif num[3] > num[0] and num[3] > num[1] and num[3] > num[2] and num[3] > num[4]:
#     largest = num[3]    
# else:
#     largest = num[4]
# print("Largest number is:", largest)
num = [34, 98, 0, 23, 44]

largest = num[0]          # assume first is largest

for n in num:             # go through list
    if n > largest:       # only ONE condition
        largest = n

print("Largest number is:", largest)
