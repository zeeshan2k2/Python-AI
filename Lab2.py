# Calculator

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
print()
print("operation \n 1. addition -> + \n 2. subtraction -> - \n 3. multiplication -> x \n 4. division -> \ \n 5. modulo -> %")
operation = int(input("Enter operation number: "))
operationSymbol = ["+", "-", "*", "/", "%"]
if operation > 5:
    print("Operation not possible")
def calculation(number1, number2, operation):
    if operation == 1:
        sum = number1 + number2
        return  sum
    elif operation == 2:
        sub = number1 - number2
        return sub
    elif operation == 3:
        mul = number1 * number2
        return mul
    elif operation == 4:
        div = number1 / number2
        return div
    elif operation == 5:
        mod = number1 % number2
        return mod
    else:
        exit()

if int(number1) == float(number1):
    number1 = int(number1)

if int(number2) == float(number2):
    number2 = int(number2)

calculatedAnswer = calculation(number1, number2, operation)

if int(calculatedAnswer) == float(calculatedAnswer):
    calculatedAnswer = int(calculatedAnswer)

print(f"{number1} {operationSymbol[operation - 1]} {number2} =" , calculation(number1, number2, operation))




# Union, Compliment and Intersection
