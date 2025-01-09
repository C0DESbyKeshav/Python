
# *ARITHMETIC OPERATORS (+, -, *, /, %)
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

print("\n")

# *ASSIGNMENT OPERATORS(=, +=, -=, *=, /=)
a = 5 - 8  # Assign subtraction of 5 and 8 to 'a'
print(a)

a += 1  # Increments the value of 'a' by 1 and again assigns it to 'a'.
# It means a = a + 1.
print(a)

a -= 1  # Decrements the value of 'a' by 1 and again assigns it to 'a'.
# It means a = a - 1.
print(a)

a *= 1  # Multiplies the value of 'a' by 1 and again assigns it to 'a'.
# It means a = a * 1.
print(a)

a /= 1  # Divides the value of 'a' by 1 and again assigns it to 'a'.
# It means a = a / 1.
print(a)

print("\n")

# *COMPARISON OPERATORS (==, >, >=, <, <=, !=)
if a == b:
    print(a + b)

if a > b:
    print(a + b)

if a >= b:
    print(a + b)

if a < b:
    print(a + b)

if a <= b:
    print(a + b)

if a != b:
    print(a + b)

print("\n")

# *LOGICAL OPERATORS (and, or, not)
# Truth Table of 'and'
print("True and True is ", True and True)
print("True and False is ", True and False)
print("False and True is ", False and True)
print("False and False is ", False and False)

print("\n")

# Truth Table of 'or'
print("True or True is ", True or True)
print("True or False is ", True or False)
print("False or True is ", False or True)
print("False or False is ", False or False)

print("\n")

# Truth Table of 'not'
print(not (True))
print(not (False))
