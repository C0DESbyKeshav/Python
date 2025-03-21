# Can you change the slf parameter inside a class to something else (say 'keshav'). Try changing slf to 'slf' or 'keshav' and see the effects.


class Calculator:

    def __init__(slf, num):
        slf.num = num

    @staticmethod
    def about():
        print("Hello Calculator !!")
        
    def square(slf):
        return slf.num ** 2
    
    def cube(slf):
        return slf.num ** 3
    
    def square_root(slf):
        return slf.num ** 0.5


obj = Calculator(2)
obj.about()
print(obj.square(), obj.cube(), obj.square_root())
