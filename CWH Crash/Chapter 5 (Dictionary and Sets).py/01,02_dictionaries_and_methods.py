# Dictionary is a collection of key-value pairs.
a = {"key": "value",
     "Password": 'Pas@123',
     "marks": 100,
     "list": [1, 2, 9],
     0: '''Aisa bhi
     Ho sakta hai'''}

print(a)
print(type(a))

dic = {}  # Empty dictionary

print("\n")

# print(a[2])   // You can't access the elements of a dictionary like a list.
print(a['marks'])
print(a[0])
# print(a[100])   // You can't access the elements of a dictionary by its 'value'. It has to 'key'

print("\n")

# * Properties of Python Dictionaries:
'''1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys.'''

# * DICTIONARY METHODS:
# 1. clear() – Remove all items
d = {'a': 1, 'b': 2}
d.clear()
print(d)  # Output: {}

print("\n")

# 2. copy() – Create a shallow copy
d1 = {'x': 10, 'y': 20}
d2 = d1.copy()
print(d2)  # Output: {'x': 10, 'y': 20}

print("\n")

# 3. fromkeys() – Create a dictionary with default values
keys = ['name', 'age', 'city']
d = dict.fromkeys(keys, 'N/A')
print(d)  # Output: {'name': 'N/A', 'age': 'N/A', 'city': 'N/A'}

print("\n")

# 4. get() – Retrieve a value safely
d = {'name': 'Alice', 'age': 30}
print(d.get('name'))  # Output: Alice
print(d.get('city', 'Not Found'))  # Output: Not Found

print("\n")

# The difference between get() and normal access method:
print(a.get("Password"))
print(a["Password"])
print(a.get("Keshav"))  # This method returns 'None' if the key is not present in the dictionary instead of throwing an error.
# print(a["Keshav"])     // This method throws an error if the key is not present in the dictionary.

print("\n")

# 5. items(), keys(), values()
d = {'name': 'Bob', 'age': 25}
print(d.items())  # Output: dict_items([('name', 'Bob'), ('age', 25)])
print(d.keys())  # Output: dict_keys(['name', 'age'])
print(d.values())  # Output: dict_values(['Bob', 25])

print("\n")

# 6. pop() – Remove and return a key
d = {'a': 1, 'b': 2, 'c': 3}
print(d.pop('b'))  # Output: 2
print(d)  # Output: {'a': 1, 'c': 3}

print("\n")

# 7. popitem() – Remove and return the last (key, value)
d = {'x': 10, 'y': 20}
print(d.popitem())  # Output: ('y', 20)
print(d)  # Output: {'x': 10}

print("\n")

# 8. setdefault() – Insert if key is missing
d = {'name': 'John'}
print(d.setdefault('name', 'Unknown'))  # Output: John
print(d.setdefault('age', 25))  # Output: 25 (Key added)
print(d)  # Output: {'name': 'John', 'age': 25}

print("\n")

# 9. update() – Merge dictionaries
# Update is possible because the dictionaries are mutable.
# The key which is absent in the defined dictionary and is being updated, gets added into the dictionary as a new key-value pair. 
d = {'name': 'Emma'}
d.update({'age': 28, 'city': 'New York'})
print(d)  
# Output: {'name': 'Emma', 'age': 28, 'city': 'New York'}
