# Write a program to print multiplication table of a given number using for loop

num = int(input("Enter a number: "))
j = 1

if(num == 0):
    print("Please Enter a non-zero value")
else:
    if(num < 0):
        limit = (num * 10) - 1
    else:
        limit = (num * 10) + 1
    
    print("\nMultiplication table of ", num)
    for i in range(0, limit, num):
        if(i == 0):
            continue
        else:
            print(f"{num} x {j} = ", i)
            j += 1

print("\nDone !!")
