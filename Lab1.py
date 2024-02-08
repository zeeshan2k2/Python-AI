
# for multiplication
number = int(input("Enter a number: "))
for num in range(11):
    print(f"{number} x {num} = {number * num}")
print()


# for factorial
def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)

print(f"Factorial of {number} is", factorial(number))
print()

# to check if number is prime or not
if number == 1 or number == 0:
    exit(print("input correct number"))
elif number > 1:
    if number == 2:
        print("2 is a prime number")
        exit()
    elif number != 2:
        for i in range(2, number):
            if number % i == 0:
                statusP = False
                break
            else:
                statusP = True

        if statusP:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")