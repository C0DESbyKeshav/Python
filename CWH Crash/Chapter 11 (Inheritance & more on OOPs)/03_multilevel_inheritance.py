class Employee:  # Base Class
    company = "ITC"
    name = "Party"
    salary = 3500000

    def show(self):
        print(f"The employee name is: {self.name}.\nThe employee's salary is: {self.salary}")

    
class Coder(Employee):  # Derived Class for class Employee and Base Class for class Coder
    age = 35

    def show_age(self):
        print(f"The employee's age is: {self.age}")
    
    
class Programmer(Coder):  # Derived or child class
    company = "ITC Infotech Inc."

# We can use the methods in the child class same that of the base class without rewriting it again.
    def show_language(self):
        print(f"The employee name is: {self.name}.\nThe employee's language is: {self.salary}")


emp2 = Coder()
print(emp2.name)
print(emp2.company)
print(emp2.age)
print(emp2.salary)
    
emp1 = Programmer()
print(emp1.name)
print(emp1.company)
print(emp1.age)
print(emp1.salary)

