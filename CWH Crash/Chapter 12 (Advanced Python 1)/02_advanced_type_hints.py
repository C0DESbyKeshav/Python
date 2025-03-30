# Python's typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.

from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
print(type(numbers), numbers)

# Tuple of a string and an integer
person: Tuple[str, int] = ("Ridhav", 35)
print(type(person), person)

# Dictionary of string keys and integer values
scores: Dict[str, int] = {"Keshav": 25, "Ridhav": 35}
print(type(scores), scores)

# Union type for variables that can hold multiple types
identifier: Union[str, int] = "ID2535"
identifier = 2535  # Also valid
print(type(identifier), identifier)

# These annotations helps in making the code self-documenting and allow developers to understand the data structure used at a glance.
