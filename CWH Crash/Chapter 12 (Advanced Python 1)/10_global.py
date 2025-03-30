# 'global' keyword is used to modify the variable outside of the current scope.

a = 35


def fun1():
    a = 25
    print(a)

    
fun1()
print(a)

print("\n")


def fun2():
    global a
    # This will overwrite the global value of 'a'
    a = 25
    print(a)

    
fun2()
print(a)
