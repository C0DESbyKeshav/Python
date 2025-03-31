# Function created using an expression using 'lambda' keyword.


# * Our usual method to create and call a function
def square(n):
    return n * n


print(square(5))

# * Using lambda function to create and call the same function
power = lambda n, e: n ** e
# NOTE: The above line says that there is a lambda function 'power' which takes 'n' and 'e' as arguments and returns the result value of {n ** e}
print(power(5, 3))
