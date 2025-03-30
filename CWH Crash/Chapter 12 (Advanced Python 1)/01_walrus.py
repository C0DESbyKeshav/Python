# The walrus operator (:=) introduced in Python 3.8, allows you to assign values to variables as part of an expression.
# This operator, named for its resemblance to the eyes and tusks of a walrus, is officially called the "assignment expression".

# Using walrus operator
if(n := len([1, 2, 3, 4, 5, 6, 7, 8])) > 5:
    print(f"List is too long ({n} elements, expected <= 5)")

# Without using walrus operator
n = len([1, 2, 3, 4, 5, 6, 7, 8])
if n > 5:
    print(f"List is too long ({n} elements, expected <= 5)")

# The difference between the two examples is that the walrus operator (n := len([1, 2, 3, 4, 5, 6, 7, 8])) assigns the result of len([1, 2, 3, 4, 5, 6, 7, 8]) to the variable n. The variable n is then used in the if condition.
