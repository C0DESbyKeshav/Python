# Write a program to find the greatest of four numbers entered by the user.

num = []

print("Enter four distinct numbers: ")
for i in range(4):
    num.append(int(input()))

# METHOD I:

if ((num[0] > num[1]) and (num[0] > num[2]) and (num[0] > num[3])):
    print(f"{num[0]} is the greatest number")
elif ((num[1] > num[0]) and (num[1] > num[2]) and (num[1] > num[3])):
    print(f"{num[1]} is the greatest number")
elif ((num[2] > num[0]) and (num[2] > num[1]) and (num[2] > num[3])):
    print(f"{num[2]} is the greatest number")
else:
    print(f"{num[3]} is the greatest number")

# METHOD II:
greatest = max(num)
print(f"{greatest} is the greatest number")
