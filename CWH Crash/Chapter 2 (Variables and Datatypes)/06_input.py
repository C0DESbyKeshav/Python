
# *INPUT() FUNCTION
# This function allows the user to take input from the keyboard as a string.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
''' If here, 'int' is not written (i.e. the typecasting is not done into int)
then by default the input function takes the input in string type
and while addition of a and b, it will concatenate the strings
instead of performing an arithmetic addition operation.'''

print("Number a is: ", a)
print("Number b is: ", b)
print("Sum of a and b is: ", a+b)

# NOTE: It is important to note that the output of input is always a string
# (even if a number is entered).
