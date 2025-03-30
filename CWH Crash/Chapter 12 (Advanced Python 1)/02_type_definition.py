# Type Hints are added using (:) syntax for variables and the -> syntax for function return types.
# It can be done for any data type.

# Variable type hint
n: int = 35
print(type(n))
# Here, we already declare that the type of integer n is integer.


# Function type hint
def sum(a: int, b: int) -> int:
    return a + b

# Here, we have already declared that the type of integer a and b is integer and also that this function will return a value of type integer.
# sum(3, 6.3)   # this will throw an error since we are passing the second argument as a floating point number instead of an integer.


print(type(sum(25, 35)))
