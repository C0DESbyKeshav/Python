# The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.
# For example:

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

# In this case, a and b are two separate lists that have the same values, so == returns True. However, a and b are not the same object in memory, so is returns False.

# One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, is and == will always return the same result:

a = "ridhav"
b = "ridhav"
print(a == b)  # True
print(a is b)  # True

a = 5
b = 5
print(a == b)  # True
print(a is b)  # True

# In these cases, a and b are both pointing to the same object in memory, so is and == both return True.

# * For mutable objects such as lists and dictionaries, is and == can behave differently. In general, you should use == when you want to compare the values of two objects, and use is when you want to check if two objects are the same object in memory.

# NOTE - MOST IMP: 
'''What is integer interning?
Python pre-creates (or "caches") small integers in memory, so they can be reused. This range is usually:
-5 to 256
That means, anytime you use a number within this range, Python reuses the same memory object instead of creating a new one.

-5 to 256 → Python caches those integers → same memory = is gives True
Outside that range → new objects each time → is gives False
'''
