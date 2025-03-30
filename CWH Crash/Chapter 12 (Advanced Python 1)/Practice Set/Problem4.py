# Write a program to display a/b where a and b are integers. If b = 0, display infinite by handling the 'ZeroDivisionError'.

try:
    num1 = int(input("Enter value of num1: "))
    num2 = int(input("Enter value of num2: "))
    print(f"The division of {num1} and {num2} is: ", num1 / num2)
except ZeroDivisionError:
    print("Infinite")
except TypeError:
    print("Both inputs should be integers.")
except:
    print("An unexpected error occurred.")
