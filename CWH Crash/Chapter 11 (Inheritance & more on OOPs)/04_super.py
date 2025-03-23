# Sometimes we want that when we call the Manager class's constructor then the constructor of its base class should also be called. This is the when the 'super' comes into play


class Employee:

    def __init__(self):
        print("Employee constructor")

        
class Programmer(Employee):

    def __init__(self):
        print("Programmer constructor")

        
class Manager(Employee):

    def __init__(self):
        super().__init__()  # This will call the constructor of Programmer class
        print("Manager constructor")

        
obj1 = Employee()  # This will only call the constructor of Employee class
obj2 = Programmer()  # This will only call the constructor of Programmer class since it does not have super in its method
obj3 = Manager()  # This will call the constructor of Employee and then Manager
