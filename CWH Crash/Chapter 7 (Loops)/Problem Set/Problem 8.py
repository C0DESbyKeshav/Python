# Write a program to print the left-sided star pattern:

n = int(input("Enter the limit: "))

# * Pattern I:
for i in range(1, n + 1):
    print("*" * i, end="")
    print("")

print("\n")

# * Pattern II:
for i in range(1, n + 1):
    print("* " * i, end="")
    print("")
