# String is a datatype in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways:

# *Declaration of types of strings
a = 'Keshav Mandal'     # Single quoted string
b = "keshav"            # Double quoted string
c = '''keshav'''        # Triple quoted string

# Strings are inmutable
# .i.e. we can't change any character in between from a string.

# *String Slicing
print("\nTo shorten the length of string")
nameshort = a[0:4]  # Start from 0 all the way till 4 (excluding 4)
# NOTE: first index is included but the last index is not included.
print(nameshort)
print(a[0:6])
print(a[7:13])
print("\nDefault index:")
print(a[:4])    # By default 0
print(a[0:])    # By default length, where length=13

# *Accessing the characters of a string through index number
print("\nAccessing the characters of a string through index number")
for i in range(6):
    print(a[i])

# Negative Slicing
print("\nNegative Slicing")
# 'K     e     s     h     a     v     _     M     a     n     d     a     l'
#  -13  -12   -11   -10    -9   -8    -7    -6    -5   -4    -3     -2    -1
print(a[-13:-7])
print(a[7:13])

# *Slicing with skip value
print("\nSlicing with skip value")
d = "abcdefghijklmnopqrstuvwxyz"
print(d[1:9:4])
# first number -> starting index number for slicing.
# second number -> ending index number for slicing (excluded).
# third number -> no of characters to be skipped.
