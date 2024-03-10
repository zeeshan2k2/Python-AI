# 1.Program to find minimum and maximum value from a list using in-built functions.

arr1 = [13, 3, 5, 2, 8]

print(f"This is the given array: {arr1}")
print(f"This is the minimum value: {min(arr1)}")
print(f"This is the maximum value: {max(arr1)}")

print()

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

print()

# 3.Linear Search

arr3 = [4, 1, 73, 21, 12, 89, 8]

numToFind = int(input("Enter the number you want to find: "))
counter = 0
foundNum = False
for i in arr3:
    if numToFind == i:
        print(f"Found at index {counter} of array {arr3}")
        foundNum = True

    counter += 1

if foundNum == False:
    print("Number not found!")

print()

# 4.Binary Search

arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
numberInput = int(input("Enter a number you'd like to find: "))

lower = 0
upper = len(arr4) - 1
mid = (lower + upper) // 2
midVal = arr4[mid]

if numberInput < arr4[lower] or numberInput > arr4[upper]:
    print("Number not in array")
elif numberInput == midVal:
    print(f"{numberInput} found at index {mid}")
else:
    while numberInput != midVal:
        mid = (lower + upper) // 2
        midVal = arr4[mid]
        if numberInput == midVal:
            print(f"{numberInput} found at {mid}")
        elif numberInput > midVal:
            lower = mid + 1
        elif numberInput < midVal:
            upper = mid - 1
















