# Write a program to find the greatest of four numbers entered by the user.

Lnumbers = []
print("Enter four integers:")
for i in range(4):
    Lnumbers.append(int(input()))
Tnumbers = tuple(Lnumbers)
print(Tnumbers)
print("The greatest of four numbers entered by the user is: ", max(Tnumbers))
