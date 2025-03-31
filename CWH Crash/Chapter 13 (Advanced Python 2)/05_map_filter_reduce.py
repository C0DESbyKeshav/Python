
# * MAP FUNCTION
# NOTE: Map applies a function to all the items in an input_list
# When we want to apply the same function for all the items in the list, then we need to map them.
# Purpose: Applies a given function to each item in an iterable and returns a new iterable (map object).
# * Syntax: map(function, input_list)
# where, function can be a lambda function
# NOTE: Returns: A new iterable with transformed values.

l = [1, 2, 3, 4, 5]

square = lambda x: x * x

sqList = map(square, l)
# Map function takes each item from the list 'l', passes it as an argument for the lambda function 'square' and stores the result value {x * x} to the variable 'sqList'.

print(sqList)
print(list(sqList))  # Convert the map object to a list to display the result

# * FILTER FUNCTION
# NOTE: Filter creates a list of items for which the function returns true.
# Purpose: Filters elements from an iterable based on a function that returns True or False.
# * Syntax: list(filter(function, input_list))
# where, function can be a lambda function
# NOTE: Returns: A new iterable containing only the elements for which the function returns True.

l = [1, 2, 3, 4, 5]


def even(n):
    if(n % 2 == 0):
        return True
    return False


onlyEven = filter(even, l)
# Filter function takes each item from the list 'l', passes it as an argument for the defined function 'even' and stores the result value only if the function returns true {even numbers} to the variable 'onlyEven'.
print(onlyEven)
print(list(onlyEven))

# * REDUCE FUNCTION
# NOTE: Reduce applies a rolling computation to sequential pair of elements.
# Purpose: Applies a function cumulatively to elements of an iterable, reducing it to a single value.
# * Syntax:
'''from functools import reduce
val = reduce(function, list1)
where, function can be a lambda function'''
''' If the function computes sum of two numbers and the list is [1, 2, 3, 4]
(1  +  2)    3    4
    (3   +   3)   4
        (6    +   4)
              10
'''
# NOTE: Returns: A single reduced value.

from functools import reduce

l = [1, 2, 3, 4]
add = lambda x, y: x + y    
val = reduce(add, l)
print(val)

# * One of the applications of reduce function that came into my mind - factorial of any number
num = int(input("Enter a number: "))
factorial = reduce((lambda x, y: x * y), range(1, num + 1))
print(f"The factorial of {num} is {factorial}")
