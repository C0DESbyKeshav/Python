# Write a class Calculator capable of finding square, cube and square root of a number


class Calculator:

    def __init__(self, num):
        self.num = num

    @staticmethod
    def about():
        print("Hello Calculator !!")
        
    def square(self):
        return self.num ** 2
    
    def cube(self):
        return self.num ** 3
    
    def square_root(self):
        return self.num ** 0.5


obj = Calculator(2)
print(obj.square(), obj.cube(), obj.square_root())