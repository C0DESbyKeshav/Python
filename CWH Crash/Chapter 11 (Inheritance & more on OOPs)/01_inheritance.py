# Inheritance is a way of creating a new class from an existing class
''' Syntax:
class Employee:     # Base Class
    # code
    
class Programmer(Employee):     # Derived or child class
    # code
'''
# We can use the methods and attributes of Employee in Programmer object.
# Also, we can overwrite or add new attributes and methods in Programmer class.

# * Types of Inheritance:
#   1. Single Inheritance
#   2. Multiple Inheritance
#   3. Multilevel Inheritance

# * Single Inheritance:
# Single inhertance occurs when child class inherits only a single parent class.
# Base class ==> Derived class

# * Multiple Inheritance:
# Multiple inheritance occurs when child class inherits from more than one parent class.
# Parent 1 ____
#              \____ Child
# Parent 2 ____/

# * Multilevel Inheritance:
# When a child class becomes a parent for another child class.
# Parent ==> Child 1 ==> Child 2


# EXAMPLE:
class Employee:  # Base Class
    company = "ITC"
    name = ""
    salary = 3500000

    def show(self):
        print(f"The employee name is: {self.name}.\nThe employee's salary is: {self.salary}")

    
class Programmer(Employee):  # Derived or child class
    company = "ITC Infotech Inc."

# We can use the methods in the child class same that of the base class without rewriting it again.
    def show_language(self):
        print(f"The employee name is: {self.name}.\nThe employee's language is: {self.salary}")

    
emp1 = Employee()
print(emp1.company)
emp1.name = "Keshav"
emp1.show()
# emp1.show_language()

emp2 = Programmer()
print(emp2.company)
emp2.name = "Ridhav"
emp2.show()
emp2.show_language()
