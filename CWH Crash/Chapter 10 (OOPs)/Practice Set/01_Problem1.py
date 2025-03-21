# Create a class programmer for storing information of few programmers working at microsoft.


class Programmers:
    company = "Microsoft"

    def __init__(self, name, age, gender, language):
        self.name = name
        self.age = age
        self.gender = gender
        self.language = language
        
    @staticmethod
    def greet():
        print("Hello, I'm a programmer!")
        
    def display(not_self):
        print(not_self.company, not_self.name, not_self.age, not_self.gender, not_self.language)

        
programmer1 = Programmers("Keshav", 18, "male", "C++")
programmer1.greet()
programmer1.display()

programmer2 = Programmers("Ridhav", 18, "female", "Python")
programmer2.greet()
programmer2.display()
