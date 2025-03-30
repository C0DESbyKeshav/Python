# New operators | and |= allows for merging and updating dictionaries.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2
print(merged)

dict2 |= {"one": 25 + 35}
print(dict2)
