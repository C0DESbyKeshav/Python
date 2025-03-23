# A class method is a method which is bound to the class and not the object of the class.


class TestMethod:
    a = 10
    
    def show(self):
        print("The class attribute of 'a' is: ", self.a)

    @classmethod
    def display(cls):  # classmethod decorator uses cls parameter instead of self parameter
        print("The class attribute of 'a' is: ", cls.a)
    
# Let's see which one of the above methods shows the actual correct class attribute of 'a'


obj = TestMethod()

obj.a = 5

print(obj.a)

obj.show()

obj.display()
