# A program to check whether a number is Even or Odd.

# NOTE: Definitions of Even and Odd is only defined for Whole Numbers.

num = int(input("Enter a number: "))
if num > 0:
    if ((num % 2) == 0):
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")
else:
    print(f"{num} is not a whole number.")
