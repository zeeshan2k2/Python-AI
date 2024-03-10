# # 1.Program to find minimum and maximum value from a list using in-built functions.
#
# arr1 = [13, 3, 5, 2, 8]
#
# print(f"This is the given array: {arr1}")
# print(f"This is the minimum value: {min(arr1)}")
# print(f"This is the maximum value: {max(arr1)}")
#
# print()
#
# # 2.Program to find minimum and maximum value from a list without using in-built functions.
#
# arr2 = [13, 3, 5, 8, 2, 16, 14]
#
#
# maxVal = arr2[0]
# minVal = arr2[0]
#
#
# for i in arr2:
#     if i > maxVal:
#         maxVal = i
#     elif i < minVal:
#         minVal = i
#
#
# print(f"This is the given array: {arr2}")
# print(f"This is the maximum value: {maxVal}")
# print(f"This is the minimum value: {minVal}")
#
# print()
#
# # 3.Linear Search
#
# arr3 = [4, 1, 73, 21, 12, 89, 8]
#
# numToFind = int(input("Enter the number you want to find: "))
# counter = 0
# foundNum = False
# for i in arr3:
#     if numToFind == i:
#         print(f"Found at index {counter} of array {arr3}")
#         foundNum = True
#
#     counter += 1
#
# if foundNum == False:
#     print("Number not found!")
#
# print()

# 4.Binary Search
arr4 = [4, 1, 73, 21, 12, 89, 8]
numToFind = int(input("Enter the number you want to find: "))

sortedArr = arr4.sort()



