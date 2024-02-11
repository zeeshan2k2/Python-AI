import calendar

# Calculator

# number1 = float(input("Enter first number: "))
# number2 = float(input("Enter second number: "))
# print()
# print("operation \n 1. addition -> + \n 2. subtraction -> - \n 3. multiplication -> x \n 4. division -> \ \n 5. modulo -> %")
# operation = int(input("Enter operation number: "))
# operationSymbol = ["+", "-", "*", "/", "%"]
# if operation > 5:
#     print("Operation not possible")
# def calculation(number1, number2, operation):
#     if operation == 1:
#         sum = number1 + number2
#         return  sum
#     elif operation == 2:
#         sub = number1 - number2
#         return sub
#     elif operation == 3:
#         mul = number1 * number2
#         return mul
#     elif operation == 4:
#         div = number1 / number2
#         return div
#     elif operation == 5:
#         mod = number1 % number2
#         return mod
#     else:
#         exit()
#
# if int(number1) == float(number1):
#     number1 = int(number1)
#
# if int(number2) == float(number2):
#     number2 = int(number2)
#
# calculatedAnswer = calculation(number1, number2, operation)
#
# if int(calculatedAnswer) == float(calculatedAnswer):
#     calculatedAnswer = int(calculatedAnswer)
#
# print(f"{number1} {operationSymbol[operation - 1]} {number2} =" , calculation(number1, number2, operation))






# Union, Compliment and Intersection
# array1 = [1, 1, 3, 9, 5, 2]
# array2 = [2, 3, 8, 9, 7, 2]
# array1WithoutDuplicates = []
# array2WithoutDuplicates = []
# arraySolution = []
#
# print(f"array1 = {array1}")
# print(f"array2 = {array2}")
# def removingDuplicates():
#     for i in array1:
#         if i not in array1WithoutDuplicates:
#             array1WithoutDuplicates.append(i)
#
#     for j in array2:
#         if j not in array2WithoutDuplicates:
#             array2WithoutDuplicates.append(j)
#
# def clearingAllArrays():
#     array1WithoutDuplicates.clear()
#     array2WithoutDuplicates.clear()
#     arraySolution.clear()
#
# def resetAll():
#     clearingAllArrays()
#     removingDuplicates()
#
# def operationSet():
#     removingDuplicates()
#
#     for k in array1WithoutDuplicates:
#         if k not in array2WithoutDuplicates:
#             array2WithoutDuplicates.append(k)
#
#     array2WithoutDuplicates.sort()
#     # Solution for Union
#     print(f"union is {array2WithoutDuplicates}")
#
#     resetAll()
#
#     for i in array1WithoutDuplicates:
#         for j in array2WithoutDuplicates:
#             if i == j:
#                 arraySolution.append(i)
#
#     # solution for intersection
#     arraySolution.sort()
#     print(f"intersection is {arraySolution}")
#
#     resetAll()
#
#     for i in array2WithoutDuplicates:
#         if i not in array1WithoutDuplicates:
#             arraySolution.append(i)
#
#     print(f"compliment of array1 with respect to array 2 {arraySolution}")
#
#     resetAll()
#
#     for i in array1WithoutDuplicates:
#         if i not in array2WithoutDuplicates:
#             arraySolution.append(i)
#
#     print(f"compliment of array2 with respect to array1 {arraySolution}")
#
#     resetAll()
#
#     for i in array1WithoutDuplicates:
#         for j in array2WithoutDuplicates:
#             if i == j:
#                 arraySolution.append(i)
#
#     array2WithoutDuplicates.clear()
#     for i in array1WithoutDuplicates:
#         if i not in arraySolution:
#             array2WithoutDuplicates.append(i)
#
#
#     # solution for intersection
#     arraySolution.sort()
#     print(f"Difference of array1 - array2 is {array2WithoutDuplicates}")
#
#     resetAll()
#
#     for i in array2WithoutDuplicates:
#         for j in array1WithoutDuplicates:
#             if i == j:
#                 arraySolution.append(i)
#
#     array1WithoutDuplicates.clear()
#     for i in array2WithoutDuplicates:
#         if i not in arraySolution:
#             array1WithoutDuplicates.append(i)
#
#     # solution for intersection
#     arraySolution.sort()
#     print(f"Difference of array2 - array1 is {array1WithoutDuplicates}")
#
# operationSet()




# # Calender
# yy = int(input("Enter valid year: "))
# mm = int(input("Enter valid month: "))
# print(calendar.month(yy, mm))

