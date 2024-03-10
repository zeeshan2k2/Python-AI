# 1.Program to find minimum and maximum value from a list using in-built functions.

arr1 = [13, 3, 5, 2, 8]

print(f"This is the given array: {arr1}")
print(f"This is the minimum value: {min(arr1)}")
print(f"This is the maximum value: {max(arr1)}")


# 2.Program to find minimum and maximum value from a list without using in-built functions.

arr2 = [13, 3, 5, 8, 2, 16, 14]


maxVal = arr2[0]
minVal = arr2[0]


for i in arr2:
    if i > maxVal:
        maxVal = i
    elif i < minVal:
        minVal = i


print(f"This is the given array: {arr2}")
print(f"This is the maximum value: {maxVal}")
print(f"This is the minimum value: {minVal}")

