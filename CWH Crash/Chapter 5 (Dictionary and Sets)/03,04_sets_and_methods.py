# Set is a collection of non-repetitive elements.

s = {264, 50, True, 50, 37, "Keshav", 1, 1, 60}

# Since, set and dictionary uses the same curly braces {}, so to create an empty set:
e = set()  # Don't use s = {} as it will create an empty dictionary.

# * Repetition of elements is not allowed in sets. It ignores the repeated elements.
# * Order of the elements in the set is not maintained in the output. If you want that the order should be maintained then use list. But, if you want that the elements should not be repeated then use sets.
print(s)

print("\n")

# * PROPERTIES OF SETS:
'''1. Sets are unordered.   // Element's order does'nt matter
2. Sets are unindexed.      // Cannot access elements by index
3. Sets cannot contain duplicate values.
4. Python sets are unordered, mutable, and do not allow duplicate elements.'''

# * OPERATIONS ON SETS:
# 1️⃣ Creating a Set
s = {1, 2, 3, 4}
s2 = set([5, 6, 7])  # Using set() constructor
print(s, s2)

# copy()	Returns a shallow copy of the set	
new_set = s.copy()
print(new_set)

print(len(s))  # This function works for all lists, tuples, dictionaries and sets

print("\n")

# 2️⃣ Adding & Removing Elements
s = {1, 2, 3}
s.add(4)  # Adds 4
s.remove(2)  # Removes 2 (Error if not found)
s.discard(5)  # No error if 5 is missing
print(s)  # Output: {1, 3, 4}

print("\n")

# 3️⃣ Union of Sets (| or union())
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)  # Output: {1, 2, 3, 4, 5}
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5}

print("\n")

# 4️⃣ Intersection of Sets (& or intersection())
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)  # Output: {3, 4}
print(s1.intersection(s2))  # Output: {3, 4}

print("\n")

# 5️⃣ Difference of Sets (- or difference())
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
print(s1 - s2)  # Output: {1, 2} (Elements only in s1)
print(s1.difference(s2))  # Output: {1, 2}

print("\n")

# 6️⃣ Symmetric Difference (^ or symmetric_difference())
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 ^ s2)  # Output: {1, 2, 4, 5} (Elements not common)
print(s1.symmetric_difference(s2))  # Output: {1, 2, 4, 5}

print("\n")

# 7️⃣ Checking Subset & Superset
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # Output: True
print(b.issuperset(a))  # Output: True

print("\n")

# 8️⃣ Checking Disjoint Sets
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  # Output: True (No common elements)

print("\n")

# 9️⃣ Updating a Set
# This is possible only due to the mutability property of set.
s = {1, 2, 3}
s.update([4, 5, 6])  # Adds multiple elements
print(s)  # Output: {1, 2, 3, 4, 5, 6}

print("\n")

# 🔟 Deletion of elements
s.pop()  # Removes and returns a random element	s.pop()
print(s)
s.clear()  # Removes all elements from the set	s.clear()
print(s)
