# __init__() Constructor
# It is a special method which is first run as soon as the object is created.
# This method is also known as constructor.
# It takes self argument and can also take further arguments.
# Methods starting with double underscore in python are the special types of methods which is called "dunder".


class Arithmetic:
    a = 10
    b = 20

    def __init__(self, name, language, num1, num2):  # dunder method which is automatically called
        self.name = name
        self.language = language
        self.a = num1
        self.b = num2
        print("I am creating an object")

    def add(self):
        print(f"{self.a} + {self.b} = ", self.a + self.b)
    # Whether we use the method or not but we have to pass the argument 'self'
    
    @staticmethod  # decorator to mark greet as a static method
    def greet():
        print("Hello, Happy Coding :)")
    
'''
keshav = Arithmetic()  # by writing this, the dunder automatically gets called
keshav.greet()
print(keshav.a, keshav.b)
keshav.add()
Arithmetic.add(keshav)

obj = Arithmetic()  # by writing this, the dunder automatically gets called
'''

# The efficient way to use constructor:
obj2 = Arithmetic("Keshav", "Maths", 25, 35)    # Object can be instantiated using constructor like this
obj2.greet()
print(obj2.name, obj2.language, obj2.a, obj2.b)
obj2.add()
