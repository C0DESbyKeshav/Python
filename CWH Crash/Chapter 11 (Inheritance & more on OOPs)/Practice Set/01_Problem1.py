# Create a class C_2dVector and use it to create another class representing a 3-d vector.


class C_2dVector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    '''
    def represent(self):
        # return f"{self.x}î + {self.y}ĵ"
        return C_2dVector(self.x, self.y)
    #* When we write the return value with the class name then, before returning, it goes to the __str__() dunder method to print the result in the formatted vector form.
    '''
    
    def __str__(self):
        return f"{self.x}î + {self.y}ĵ"
    
class C_3dVector(C_2dVector):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        
    '''
    def represent(self):
        # return f"{self.x}î + {self.y}ĵ + {self.z}k̂"
        return C_3dVector(self.x, self.y, self.z)
    #* When we write the return value with the class name then, before returning, it goes to the __str__() dunder method to print the result in the formatted vector form.
    '''
    
    def __str__(self):
        return f"{self.x}î + {self.y}ĵ + {self.z}k̂"


d2 = C_2dVector(5, 9)
# print(d2.represent())
print(d2)
#* When we use __str__() to print the vector then we don't have to write or call any represent() function to print the vector.
#* We just print the object of that class and the __str__() method automatically gets called.

d3 = C_3dVector(2, 4, 6)
# print(d3.represent())
print(d3)
#* When we use __str__() to print the vector then we don't have to write or call any represent() function to print the vector.
#* We just print the object of that class and the __str__() method automatically gets called.
