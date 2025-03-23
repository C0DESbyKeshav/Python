# Create a class Pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.


class Animals:

    def __init__(self):
        self.legs = 4
        self.eyes = 2
        self.ears = 2
        self.teeth = "true"
    

class Pets(Animals):

    def __init__(self):
        super().__init__()
        self.behaviour = "obedient"

        
class Dog(Pets):

    def __init__(self):
        super().__init__()
        self.sound = "bark"
        
    @staticmethod
    def bark():
        print("Woof!")
        print("Bow Wow !!")
        
    def characters(self):
        print(f"This dog has {self.legs} legs, {self.eyes} eyes, {self.ears} ears, and {self.teeth} teeth.")
        print(f"It is an {self.behaviour} animal.")
        print(f"It makes a {self.sound} sound.")


domestic = Dog()
domestic.characters()
domestic.bark()
