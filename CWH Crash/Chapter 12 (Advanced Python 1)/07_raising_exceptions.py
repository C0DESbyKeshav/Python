# Sometimes we want that the program should crash when it encounters only that one specific error instead of just continuing further after printing the error message.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if (num2 == 0):
    # We're going to raise a custom exception here
    raise ZeroDivisionError("Cannot divide by zero")
else:
    print("The result of division is:", num1 / num2)
