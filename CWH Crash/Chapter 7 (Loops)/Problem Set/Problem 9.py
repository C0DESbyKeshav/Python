# Write a program to print a starred - square / rectangle

n = int(input("Enter the limit: "))

# * Pattern I:
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n:
            print("* ", end="")
        elif j == 1 or j == n:
            print("* ", end="")
        else:
            print("  ", end="")
    print("")    

print("\n")

# * Pattern II:

# Method I:
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n:
            print("*", end="")
        elif j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print("")    

print("")

# Method II:
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print("")    
