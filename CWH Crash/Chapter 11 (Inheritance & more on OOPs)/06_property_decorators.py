# Consider the following class:


class Employee:
    a = 35
    
    # Constructor - Whenever the object of this class is created, the constructor is called.
    def __init__(self):
        print("Good Morning :)")
        
    # Static Method - if any method has no use of any variable then declare it as a static method by using @staticmethod decorator
    @staticmethod
    def greet():
        print("Hello !!")
        
    # Class Method - if we want the method to strictly use the value of the variable assigned to it in class and give it preference over the instance assignment then use @classmethod with the parameter 'cls'
    @classmethod
    def classValue(cls):
        print("The class attribute of 'a' is: ", cls.a)
    
    # Property decorator - by doing this, we can use the name function as a property without calling is as a function we will call it as a property like obj.name. It should always have a setter.
    @property
    def name(self):
        return f"Your first name is: {self.fname}\nAnd your last name is: {self.lname}"
    
    # @getters and @setters
    # The method name with @property decorator is called getter method.
    # We can define a function+@name.setter decorator like below:
    # * @setter method does all the processing work for the property method and the property method just returns the final result processed by the setter method
    # * We don't have to call the setter method we just the call the property method and all the processing part is done by the setter method internally. Setter method takes the argument from the property method to evaluate a result.
    @name.setter
    def name(self, orgName):
        self.fname = orgName.split(" ")[0]
        self.lname = orgName.split(" ")[1]
        # orgName.split(" ") function splits the passed name "Keshav Mandal" from the space and converts it into a list of two separate words like ["Keshav", "Mandal"] and thus when we write that [0] index number at the end it means the element at the 0th position in the list i.e. "Keshav"

# Abstraction means we have hidden the implementation details from the user.
# Encapsulation means we have packed all the working components into one particular unit which in this case is class.

    
emp = Employee()
emp.greet()
emp.classValue()
emp.name = "Keshav Mandal"
print(emp.name)
print(emp.fname, emp.lname)
