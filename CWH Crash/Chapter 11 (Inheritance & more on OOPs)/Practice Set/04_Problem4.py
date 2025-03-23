# Write a class Complex to represent Complex numbers, along with overloaded operators + and * which adds and multiplies them


class Complex:

    def __init__(self, real, imag):
        self.r = real
        self.i = imag
        
    def __add__(self, other):
        # return f"{self.r + other.r} + {self.i + other.i}i"
        return Complex(self.r + other.r, self.i + other.i)
    #* It will now go to __str__() dunder to print it into the form of a Complex number

    def __mul__(self, other):
        # return f"{(self.r * other.r) - (self.i * other.i)} + {(self.r * other.i) + (self.i * other.r)}i"
        return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)
    #* It will now go to __str__() dunder to print it into the form of a Complex number
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

a = Complex(4, 2)
b = Complex(3, 1)
print(a + b)
print(a * b)
