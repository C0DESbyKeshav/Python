# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce


def max(x, y):
    if(x > y):
        return x
    return y


print(reduce(max, [25, 5, 35, 2, 4]))
