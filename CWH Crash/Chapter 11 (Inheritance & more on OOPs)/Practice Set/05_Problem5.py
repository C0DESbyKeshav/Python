# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot product of them.


class Vector:

    def __init__(self, l):
        self.l = l
        
    def __add__(self, other):
        return Vector([self.l[0] + other.l[0], self.l[1] + other.l[1], self.l[2] + other.l[2]])
    # * When we write Vector here, then while displaying the results, it follows the __str__() dunder method
    
    def __mul__(self, other):
        return (self.l[0] * other.l[0] + self.l[1] * other.l[1] + self.l[2] * other.l[2])
    
    def __str__(self):
        return f"{self.l[0]}i + {self.l[1]}j + {self.l[2]}k"

    def __len__(self):
        return len(self.l)

    
v1 = Vector([3, 1, 6])
v2 = Vector([2, 4, 5])
v3 = Vector([3, 5, 6])
print(v1 + v2)
print(v2 + v3)
print(v1 + v3)
print(v1 * v2)
print(v2 * v3)
print(v1 * v3)
print(len(v1))
print(len(v2))
print(len(v3))
