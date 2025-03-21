# Add a static method in problem 2 to greet the user with hello


class Calculator:

    def __init__(self, num):
        self.num = num

    @staticmethod
    def about():
        print("Hello User !!")
        
    def square(self):
        return self.num ** 2
    
    def cube(self):
        return self.num ** 3
    
    def square_root(self):
        return self.num ** 0.5


obj = Calculator(2)
obj.about()
print(obj.square(), obj.cube(), obj.square_root())
