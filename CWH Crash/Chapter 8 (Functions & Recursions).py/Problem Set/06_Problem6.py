# Write a python function that converts inches to cms.


def convert(inch):
    return (2.54 * inch)


try:
    inch = float(input("Enter the measurement in inches: "))
    if inch < 0:
        print("Measurements cannot be negative.")
    else: print(f"{inch} = {convert(inch)} cms.")
except ValueError:
    print("Invalid measurements")
