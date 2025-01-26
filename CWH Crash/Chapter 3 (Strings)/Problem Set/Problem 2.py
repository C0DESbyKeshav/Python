# Write a program to fill in a letter template given below with name and date.
from datetime import date
NAME = input("Enter your full name: ")
DATE = date.today()  # Output: YYYY-MM-DD
print(f'''
Dear {NAME},
You are selected!
''', DATE)