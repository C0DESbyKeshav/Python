# Write a program to print the pyramid star pattern.

# * Pattern 1:
limit = int(input("Enter the limit: "))

i = 1
j = 1
k = limit - 1;
pattern = ""

for i in range(limit):
    for j in range(((limit * 2) - 1) + (2 * i)):
        if (j < (2 * k) or ((j > (2 * k)) and (j % 2 != 0))):
            pattern += " "
        else:
            pattern += "*"
    k -= 1
    pattern += "\n"
print(pattern)

# * Pattern 2:

# Method 1:
pattern = ""

for i in range(1, limit + 1):
    k = 1
    for j in range(1, limit + (i - 1) + 1):
        if (k <= limit - i):
            pattern += " "
            k += 1
        else:
            pattern += "*"
    pattern += "\n"
print(pattern)

# Method 2:
for i in range(1, limit + 1):
    print(" " * (limit - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")
# (end = "") argument of print() function removes the default new line after each print
    
