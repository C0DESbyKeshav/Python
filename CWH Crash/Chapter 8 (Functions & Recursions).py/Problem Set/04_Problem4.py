# Write a recursive function to calculate the first n natural numbers.


def add(n):
    if (n == 1):
        return 1
    return (add(n - 1) + n)


try:
    n = int(input("Enter the limit: "))
    if n <= 0: 
        print("Please Enter a natural integer...")
    else:
        print(f"The sum of first {n} natural numbers is: {add(n)}")
except ValueError:
    print("Please Enter an Integer value...")

'''
try:
    n = int(input("Enter the limit: "))
    if(n < 0):
        print("Please enter a non - negative integer...")
    else:
        add = 0
        for i in range(1, n + 1):
            add += i
        print(add)
except ValueError:
    print("Please Enter an Integer value...")
'''
