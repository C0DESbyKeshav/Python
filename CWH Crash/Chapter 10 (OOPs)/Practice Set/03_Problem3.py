# Create a class with a class attribute a ; create an object from it and set a directly using object.a = 0. Does this change the class attribute ?


class TestClass:
    a = 1


obj = TestClass()
print(obj.a)
obj.a = 0
print(obj.a)

# As, the instance attribute has higher precedence than the class attribute, so, the value of 'a' got set to 0
