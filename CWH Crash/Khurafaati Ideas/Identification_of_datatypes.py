# A python program to identify the type of the entered variable.
a = input("Enter a value:")
print(len(a))
verify = 0
i=0
j =0

for i in range(len(a)):
    if a[i]=='.':
        for j in range(len(a)):
            if j!= i and a[j].isdigit():
                verify = 2
    elif a[i].isdigit():
        verify = 1
    else:
        verify = 3
        
if verify == 1:
    print(f"The entered variable '{a}' is an integer data type")
elif verify == 2:
    print(f"The entered variable '{a}' is a float data type")
elif verify == 3:
    print(f"The entered variable '{a}' is a string data type")
