# Write a program to accept marks of 6 students and display them in a sorted manner.

# * METHOD I: By accepting the name of fruits one by one
marks = []
m1 = int(input("Enter the marks obtained by 1st student: "))
marks.append(m1)
m2 = int(input("Enter the marks obtained by 2nd student: "))
marks.append(m2)
m3 = int(input("Enter the marks obtained by 3rd student: "))
marks.append(m3)
m4 = int(input("Enter the marks obtained by 4th student: "))
marks.append(m4)
m5 = int(input("Enter the marks obtained by 5th student: "))
marks.append(m5)
m6 = int(input("Enter the marks obtained by 6th student: "))
marks.append(m6)
marks.sort()
print(marks)

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
print(values)'''

marks = list(map(int, input("Enter the marks obtained by each student (space seperated): ").split()))
marks.sort()
print(marks)

print("\n")

# * METHOD III: Using the most important property of mutability of list
marks = [0, 0, 0, 0, 0, 0]
for i in range(6):
    marks[i] = int(input(f"Enter the marks of student {i+1}: "))
marks.sort()
print(marks)
