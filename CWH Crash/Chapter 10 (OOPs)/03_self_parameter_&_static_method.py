# 'self' parameter:
# Self refers to the instance of the class.
# It is automatically passed with a function call from an object.
# NOTE: 'self' is just a name, you can change it to anything even your own name but then don't forget to replace that word everywhere.

# Static method:
# Sometimes we need a function that doesn't use the self parameter. We can define a static method like the one below.


class Arithmetic:
    a = 10
    b = 20

    def add(self):
        print(f"{self.a} + {self.b} = ", self.a + self.b)
    # Whether we use the method or not but we have to pass the argument 'self'
    
    @staticmethod  # decorator to mark greet as a static method
    def greet():
        print("Hello, Happy Coding :)")

    
keshav = Arithmetic()
keshav.greet()
keshav.add()
Arithmetic.add(keshav)