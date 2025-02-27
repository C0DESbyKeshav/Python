# Write a program to find the sum of first n natural numbers using while loop.

sum_till = int(input("Enter the limit for summation of natural numbers: "))

add = 0
i = 1

while (i <= sum_till):
    add += i
    i += 1

print(f"The sum of first {sum_till} natural numbers is: {add}")
