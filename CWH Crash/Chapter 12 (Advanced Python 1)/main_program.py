def Ridhav():
    print("My World !")

# print(f"You are running the program function from {__name__}")


if  __name__ == "__main__":
    # If this code is directly executed by running the file its present in then run this if statement
    print("This part of code will only be executed by running the main_program.")
    Ridhav()
    print(__name__)
    
# * The lines of code which we don't want it to execute when the file is imported, that part of code is written in => if __name__ == "__main__"
    
