# Write a python function to print multiplication table of a given number.


def mul(n):
    for i in range(1, 11):
        if(n == int(n)): 
            print(f"{int(n)} x {i} = {int(n*i)}")
        else: 
        
            print(f"{n} x {i} = {n*i}")


n = float(input("Enter a non-negative integer: "))
mul(n)
