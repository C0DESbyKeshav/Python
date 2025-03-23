# Operators in python can be overloaded using dunder methods. 
# These methods are called when a given operator is used on the objects.
# p1 + p2 --> p1.__add__(p2)
# p1 - p2 --> p1.__sub__(p2)
# p1 * p2 --> p1.__mul__(p2)
# p1 / p2 --> p1.__truediv__(p2)
# p1 // p2 --> p1.__floordiv__(p2)

# Other dunder / magic methods in python
# __str__() -> used to set what gets displayed upon calling str(obj)
# __len__() -> used to set what gets displayed upon calling __len__() or len(obj)


class Number:

    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        return self.n - num.n
    
    def __mul__(self, num):
        return self.n * num.n
    
    def __truediv__(self, num):
        return self.n / num.n
    
    def __floordiv__(self, num):
        return self.n // num.n

    def __str__(self):
        return f"Number(firstNumber= {self.n})"

    
a = Number(13)
b = Number(4)
print(a + b)
# When we try to add two objects, it will throw an error as it is not allowed
# To avoid that error and to able to add both the objects, we have to overload the + operator
# The above line when executed, calls the __add__() dender method which does the work of overloading the plus operator by adding both the objects

print(a - b)
print(a * b)
print(a / b)
print(a // b)

print(str(a))  # No need to call a method explicitly
print(a)
# Both does the same thing
# A more pythonic way and a good practice of printing a string through object
