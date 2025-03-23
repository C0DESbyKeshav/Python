# Write __str__() method to print the vector as follows:
# 7i + 8j + 10k
# Assume vector of dimension 3 for this problem.


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # def show(self):
    #     return Vector(self.x, self.y, self.z)
        
    def __str__(self):
        return f"{self.x}i + {self.y}j +  {self.z}k"


v = Vector(2, 8, 7)

print(v)
#* When we use __str__() to print the vector then we don't have to write or call any show() function to print the vector.
#* We just print the object of that class and the __str__() method automatically gets called.
