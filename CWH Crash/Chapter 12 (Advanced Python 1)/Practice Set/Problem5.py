# Store the multiplication table generated in problem 3 in a file named Table.txt

try:
    n = int(input("Enter a number: "))
    table = [(n * i) for i in range(1, 11)]
    
    with open("Table.txt", "a") as file:
        file.write(f"Table of {n}: {str(table)}\n")
        
except ValueError:
    print("Invalid input. Please enter a integer number.")
    
except:
    print("An unexpected error occurred.")
