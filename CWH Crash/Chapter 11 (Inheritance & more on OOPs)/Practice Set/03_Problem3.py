# Create a class Employee and add salary and increment properties to it.
# Write a method salaryAfterIncrement with a @property decorator with a setter which changes the value of increment based on the salary


class Employee:
    salary = 234
    increment = 20
    
    @staticmethod
    def greet():
        return "Hello! Dear Employee"

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100
        
emp = Employee()
print(emp.greet())
emp.salaryAfterIncrement = 280.8
print(emp.increment)