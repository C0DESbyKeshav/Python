print("\n")
print(" TUPLE ".center(200, '-'))

# *TUPLES
'''Strings -> strictly cannot be changed (immutable). Declared by using quotes. Only characters.
Lists -> can be changed (mutable) (both size and contents can be changed). Declared by box brackets. Can store any type of data.
Tuples -> cannot be changed (immutable). Declared by using round brackets. Can store any type of data.'''

'''Sometimes we need collection of elements of any data type and it should not be changed anywhere further in the program then we use tuple.'''

a = (3, 5.1, 9, True ,'One', 1, "Piece")
print("\n", a, type(a))

# Empty Tuple
b = ()
print("\n", b, type(b))

# Tuple with only one element
c = (1)     # the python interpreter will consider as an integer data type instead of tuple.
print("\n",c, type(c))

d = (1,)
print("\n",d, type(d))

# Checking immutability
# a[0] = 5      # this will throw an error.

print("\n")
print(" TUPLE METHODS ".center(200, '-'))

#* TUPLE METHODS
#* 1. count(value)     # Returns the number of times a specified value appears in the tuple.
print("\n", a)
print("The number of times 9 occurred in the tuple is ",a.count(9));

#* 2. index(value, start, stop)
'''
value: The element you want to find in the tuple.
start (optional): The position in the tuple to start searching from (default is 0).
stop (optional): The position in the tuple to stop searching (it won’t include this index).'''

# Example 1: Without start and stop
my_tuple = (10, 20, 30, 10, 20, 30)
print(my_tuple)
# Find the first index of 20
print(my_tuple.index(20))  # Output: 1 (20 is at index 1)

print("\n")

# Example 2: With start
my_tuple = (10, 20, 30, 10, 20, 30)
# Start searching for 20 from index 2
print(my_tuple.index(20, 2))  # Output: 4 (20 is found at index 4 after index 2)

print("\n")

# Example 3: With start and stop
my_tuple = (10, 20, 30, 10, 20, 30)
# Search for 20 between index 2 (inclusive) and index 5 (exclusive)
print(my_tuple.index(20, 2, 5))  # Output: 4 (20 is found at index 4 within the range)

print("\n")

# Example 4: Value not found within the range
# If the value is not in the specified range, Python raises a ValueError:
my_tuple = (10, 20, 30, 10, 20, 30)
# Try searching for 20 between index 0 and 1
'''print(my_tuple.index(20, 0, 1))  # ValueError: 20 is not in the range'''

''' Key Notes:
The start is inclusive, meaning the search starts at the specified index.
The stop is exclusive, meaning the search ends before the specified index.
If the value doesn’t exist in the range, a ValueError is raised.'''

#* 3. len(tuple): Returns the number of items in a tuple.
my_tuple = (1, 2, 3)
print(f"\n{my_tuple}\nThe length of the tuple is {len(my_tuple)}")  # Output: 3

#* 4. max(tuple): Returns the largest item in a tuple.
print(f"\n{my_tuple}\nThe largest number present in the tuple is {max(my_tuple)}")  # Output: 3

#* 5. min(tuple): Returns the smallest item in a tuple.
print(f"\n{my_tuple}\nThe smallest number present in the tuple is {min(my_tuple)}")  # Output: 1

#* 6. sum(tuple): Returns the sum of all elements in a tuple (elements must be numeric).
print(f"\n{my_tuple}\nThe total sum of all the numbers present in the tuple is {min(my_tuple)}")  # Output: 6

#* 7. tuple(sequence): Converts a sequence (e.g., list, string) into a tuple.
li = ['Luffy', 25, 9.43, 0, True]
print(f"\n{li}\nAfter converting the above list into a tuple: {tuple(li)}")

#* 8. in and not in: Check for membership.
my_tuple = (1, 2, 3)
print(2 in my_tuple)   # Output: True
print(4 not in my_tuple)  # Output: True

print("\n")
print(" TUPLE OPERATIONS ".center(200, '-'))

#* OPERATIONS ON TUPLE
# 1. Slicing: Extract a portion of a tuple using slicing.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[:3])   # Output: (10, 20, 30)
print(my_tuple[::2])  # Output: (10, 30, 50)