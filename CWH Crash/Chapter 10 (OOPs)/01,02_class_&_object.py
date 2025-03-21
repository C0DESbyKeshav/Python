# There are two approaches to write a python program -> Function approach and the OOPs
# OOPs --> The Object Oriented Porgramming Approach
# OOPs is all about the classes and objects.
# Classes --> blueprint for creating objects
# ex.: Class --> an empty form for a certain entrance exam so the class contains a template for the object (i.e. the name_of_the_student, address, age, etc.)
#      Object --> a student names "XYZ" fills up the form so the object is name_of_the_student = "XYZ", address = "Taj road" age = 18. In this way, we can efficiently create as many objects as we need using the same template for different students.

# Solving a problem by creating objects is one of the most popular approaches in programming. This is calles "Object Oriented Programming"
# This concept focuses on using resuable code. 
'''Implements DRY principle:
    - Don't Repeat Yourself.
    - This means that the code should have a single, well-defined responsibility.
    - In other words, the code should be divided into functions or methods that perform a single task.
'''
# CLASS: A class is a blueprint for creating objects.
'''Syntax: 
class Employee:             [classname is written in Pascal case]
    # methods & variables
'''

# OBJECT:
# An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object installation.
# Objects of a given class can invoke the methods available to it without revealing the implementation details to the user........>  [Abstraction and Encapsulation]

# Modelling a problem in OOPs
'''We identify the following in our problem:
Noun -> Class -> Employee
Adjective -> Attributes -> name, age, salary
Verbs -> Methods -> getSalary(), increment()
'''

# Class Attributes: An attribute that belongs to the class rather than a particular object.

# Instance Attributes: An attribute that belongs to the Instance (object).
# NOTE: Instance attributes take preference over class attributes during assignment & retreival.


# EXAMPLE:
class Employee:
    name = "Employee"
    age = 18
    language = ""
    speciality = "Captivated"

    
obj1 = Employee()  # object instantiation
obj1.name = "Keshav"
obj1.language = "C++"
print(obj1.name, obj1.age, obj1.language, obj1.speciality)
# Here, the name attribute is present both in object and in class so, the preference will be given to the instance attribute.

obj = Employee()  # object instantiation
obj.language = "Python"
print(obj.name, obj.age, obj.language, obj.speciality)
# Here, the attribute name is not present in the object so the preference will go to the name attribute present in class

obj2 = Employee()  # object instantiation
obj2.name = "Ridhav"
obj2.language = "Smile"
Employee.speciality = "Ignorance"  # changing class attribute
print(obj2.name, obj2.age, obj2.language, obj2.speciality)
# Here, the name attribute is present both in object and in class so, the preference will be given to the instance attribute.

# Here, names are the instance (i.e. object) attributes whereas the age, language, speciality are the class attributes as it directly belongs to the class.
