# There are many built-in exceptions which are raised in python when something goes wrong.
# Exception in python can be handled using a try statement.
# The code that handles the exception is written in the except clause.

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    div = num1 / num2
    print("The result of division is:", div)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print(e)
except:
    print("An unexpected error occurred.")
    # All other exceptions are handled here.
else:
    print("Success !!")
    # The else clause is executed only if no exception is raised.

# When the exception is handled, the code flow continues without program interruption.
# i.e. the program does not crashes at any line of code due to any kind of error, instead it prints the exception message and then contunues to execute the further lines of code.
