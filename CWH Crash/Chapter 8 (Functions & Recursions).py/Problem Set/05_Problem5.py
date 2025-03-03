# Write a python function to print first n lines of the inverse star pyramid.


def inv_py(n):
    # for i in range(n):
        # print('* ' * (n - i), end='')
        # print('')
        if(n == 0): return
        print('* ' * n)
        inv_py(n - 1)


try:
    n = int(input("Enter the limit: "))
    if(n <= 0): print("Please Enter a positive integer natural number...")
    else: inv_py(n)
except ValueError:
    print("Please Enter an integer number...")
