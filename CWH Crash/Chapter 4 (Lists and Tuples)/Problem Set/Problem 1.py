# Write a program to store seven fruits in a list entered by the user.

# * METHOD I: By accepting the name of fruits one by one
fruits = []
f1 = input("Enter a fruit name: ")
fruits.append(f1)
f2 = input("Enter a fruit name: ")
fruits.append(f2)
f3 = input("Enter a fruit name: ")
fruits.append(f3)
f4 = input("Enter a fruit name: ")
fruits.append(f4)
f5 = input("Enter a fruit name: ")
fruits.append(f5)
f6 = input("Enter a fruit name: ")
fruits.append(f6)
f7 = input("Enter a fruit name: ")
fruits.append(f7)
print(fruits)

print("\n")

# * METHOD II: By accepting multiple inputs in a single line (RECOMMENDED)
'''The most commonly used method for accepting multiple inputs in a single line in Python is:
✅ Using split() with map() for type conversion'''

'''ACCEPTING INPUTS AS LIST FOR INTEGERS:
# Convert input values to integers
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)'''

'''ACCEPTING INPUTS AS LIST FOR STRINGS:
# Accept space-separated values and store them as a list
values = input("Enter numbers: ").split()
OR
values = list(map(str, input("Enter numbers: ").split()))
print(values)'''

fruits = list(map(str, input('Enter the name of seven fruits (space seperated): ').split()))
# fruits = input("Enter the name of seven fruits (space seperated): ").split()
print(fruits)

print("\n")

# * METHOD III: Using the most important property of mutability of list
fruits = ['', '', '', '', '', '', '']
for i in range(7):
    fruits[i] = input(f"Enter the name of fruit {i+1}: ")
    # fruits[i] = input("Enter a fruit name: ")
print(fruits)
