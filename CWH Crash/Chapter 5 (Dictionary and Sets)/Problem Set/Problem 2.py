# Write a program to input 8 numbers from the user and display all the unique numbers (once)

s = set()
print("Enter 8 integers: ")
for i in range(8):
    num = input()
    s.add(int(num))
print(s)
