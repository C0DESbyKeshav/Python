# FORMAT METHOD (STRINGS)
# Formats the values inside the string into a desired output.
# Nowadays, we get to use the f literal string to print our desired output but earlier there were no such things so you may encounter this method in some old programs, so you must understand this.

iAmThankful = "My {} is my {}".format("Mom", "God")
print(iAmThankful)

# "My {0} is my {1}".format("Mom", "God")
# By default, the index numbers are 0, 1, 2,.... and so on.
# We can change that according to our convienience.

iAmThankful = "My {1} is my {0}".format("Mom", "God")
print(iAmThankful)