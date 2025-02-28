# Write a python program using function to convert Fahrenheit to degree Celsius.

F = float(input("Enter the temperature in °F: "))


def convert(F):
    C = 5 * (F - 32) / 9
    return C


print(f"{F} °F is : {convert(F)} °C")
